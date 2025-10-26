from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")  # ← Replace with your real key


class body_part1:
    """Class to store and manage a user's job experiences."""

    def __init__(self):
        self.num = ''
        self.start = ''
        self.end = ''
        self.posi = ''
        self.company = ''
        self.jobs = []

    def job_experience(self, *ui_data):
        """
        Collects job experience information from the user.
        Each entry should be a tuple: (posi, company, start, end)
        """
        try:
            self.num = int(input("Enter how many job experiences you have (0 to skip): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        while self.num > 0:
            self.num -= 1
            self.start = input("Enter start date of your work: ").strip()
            self.end = input("Enter end date (or 'present'): ").strip()
            self.posi = input("Enter job position: ").strip()
            self.company = input("Enter company name: ").strip()
            self.jobs.append(f"{self.posi} | {self.company} ({self.start} - {self.end})")

    def generate_job_descriptions(self):
        """
        Uses OpenAI to generate 3 bullet point descriptions for each job experience.
        Returns the full AI output as a string (for use in Tkinter UI or export).
        """
        output_text = "=== AI-Generated Job Descriptions ===\n"

        for job in self.jobs:
            try:
                # Split stored string: "Position | Company (Start - End)"
                posi, rest = job.split(" | ")
                company = rest.split("(")[0].strip()

                prompt = (
                    f"Generate 3 concise, professional bullet points describing the responsibilities "
                    f"and key achievements for a {posi.strip()} at {company}. "
                    f"Keep it impactful and resume-ready."
                )

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )

                ai_text = response.choices[0].message.content.strip()
                output_text += f"\n\n🔹 {posi.strip()} at {company}\n{ai_text}\n"

            except Exception as e:
                output_text += f"\nError generating description for {job}: {e}\n"

        return output_text

    def __str__(self):
        job_section = "\n".join(self.jobs) if self.jobs else "None"
        return f"\n--- Job Experience ---\n{job_section}"


def main():
    print("\n=== Resume Input (No bullet points) ===")
    user = body_part1()

    # Interactive input only
    user.job_experience()

    print(user)
    user.generate_job_descriptions()


if __name__ == "__main__":
    main()
