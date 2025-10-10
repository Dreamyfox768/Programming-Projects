class BodyPart2:
    def __init__(self):
        self.num = ''
        self.date = ''
        self.os = ''
        self.language = ''
        self.tool = ''
        self.application = ''
        self.soft_skills = ''
        self.cert_name = ''
        self.cert_code = ''
        self.cert_list = []

    def skill(self):
        self.os = input("Operating System: ").strip()
        self.language = input("Programming Language(s): ").strip()
        self.tool = input("Tool(s): ").strip()
        self.application = input("Application(s): ").strip()
        self.soft_skills = input("Soft Skills: ").strip()

    def certs(self):
        try:
            self.num = int(input("How many certifications do you have? Enter 0 to skip: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        while self.num > 0:
            self.date = input("Date received: ").strip()
            self.cert_name = input("Certification name: ").strip()
            self.cert_code = input("Certification code: ").strip()
            self.num -= 1
            cert_info = f"{self.cert_name} ({self.cert_code}) - {self.date}"
            self.cert_list.append(cert_info)

    def __str__(self):
        certs_formatted = "\n".join(f"- {cert}" for cert in self.cert_list) if self.cert_list else "None"
        return (
            f"\n=== Skills & Certifications ===\n"
            f"Operating System: {self.os}\n"
            f"Languages: {self.language}\n"
            f"Tools: {self.tool}\n"
            f"Applications: {self.application}\n"
            f"Soft Skills: {self.soft_skills}\n"
            f"Certifications:\n{certs_formatted}"
        )


def main():
    print("\n=== Information Entry: Skills & Certifications (Non-AI) ===")
    user = BodyPart2()
    user.skill()
    user.certs()
    print(user)


if __name__ == "__main__":
    main()
