class body_part1:
    def __init__(self):
        self.num = ''
        self.start = ''
        self.end = ''
        self.posi = ''
        self.company = ''
        self.jobs = []
        self.role = ''
        self.organi = ''
        self.vols = []

    def job_experience(self):
        self.num = int(input("Enter how many job experiences you have (0 to skip): "))
        while self.num > 0:
            self.num -= 1
            self.start = input("Enter start date of your work: ").strip()
            self.end = input("Enter end date (or 'present'): ").strip()
            self.posi = input("Enter job position: ").strip()
            self.company = input("Enter company name: ").strip()

            self.jobs.append(f"{self.posi} | {self.company} ({self.start} - {self.end})")

    def volunteer_experience(self):
        self.num = int(input("Enter how many volunteer experiences you have (0 to skip): "))
        while self.num > 0:
            self.num -= 1
            self.role = input("Enter volunteering role: ").strip()
            self.organi = input("Enter organization name: ").strip()

            self.vols.append(f"{self.role} | {self.organi}")

    def __str__(self):
        job_section = "\n".join(self.jobs)
        vol_section = "\n".join(self.vols)
        return (f"\n--- Job Experience ---\n{job_section}"
                f"\n--- Volunteering Experience ---\n{vol_section}")


def main():
    print("\n=== Resume Input (No bullet points) ===")
    user = body_part1()
    user.job_experience()
    user.volunteer_experience()
    print(user)

if __name__ == "__main__":
    main()
