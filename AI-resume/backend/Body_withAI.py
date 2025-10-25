import openai

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

class body_part1:
    """Class to store and manage a user's job experiences."""

    def __init__(self):
        # Initialize all attributes
        self.num = ''       # Number of jobs to input
        self.start = ''     # Start date for a job
        self.end = ''       # End date for a job
        self.posi = ''      # Job position/title
        self.company = ''   # Company name
        self.jobs = []      # List to store formatted job entries

    def job_experience(self, *ui_data):
        """
        Collects job experience information from the user.
        Each entry will be stored as a string: "Position | Company (Start - End)"
        """
        try:
            self.num = int(input("Enter how many job experiences you have (0 to skip): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        while self.num > 0:
            self.num -= 1
            self.start = input("Enter start date of your work: ").strip()  # Prompt for start date
            self.end = input("Enter end date (or 'present'): ").strip()    # Prompt for end date
            self.posi = input("Enter job position: ").strip()              # Prompt for position
            self.company = input("Enter company name: ").strip()           # Prompt for company
            # Append formatted job string to the list
            self.jobs.append(f"{self.posi} | {self.company} ({self.start} - {self.end})")

    def generate_job_descriptions(self):
        """
        Uses OpenAI to generate 3 bullet point descriptions for each job experience.
        Prints AI-generated descriptions to the console.
        """
        print("\n=== AI-Generated Job Descriptions ===")
        for job in self.jobs:
            try:
                # Split the job string into position and company/date parts
                posi, rest = job.split(" | ")
                company, dates = rest.rsplit("(", 1)
                # Construct prompt for OpenAI
                prompt = (
                    f"Generate 3 professional bullet points describing the responsibilities and achievements "
                    f"for a {posi.strip()} at {company.strip()}. Keep it concise and impactful."
                )

                # Call OpenAI API to generate text
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                # Display AI-generated content
                print(f"\n🔹 {posi.strip()} at {company.strip()} ({dates.strip()}")
                print(response['choices'][0]['message']['content'])

            except Exception as e:
                print(f"Error generating description for {job}: {e}")

    def __str__(self):
        """Return a formatted string of all job experiences for display or export."""
        job_section = "\n".join(self.jobs) if self.jobs else "None"
        return f"\n--- Job Experience ---\n{job_section}"


def main():
    print("\n=== Resume Input (No bullet points) ===")
    user = body_part1()

    # Interactive input from user
    user.job_experience()

    # Print entered jobs
    print(user)
    # Generate AI descriptions
    user.generate_job_descriptions()


if __name__ == "__main__":
    main()
