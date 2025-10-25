class BodyPart2:
    """Class to store and manage a user's skills and certifications."""

    def __init__(self):
        """Initialize all attributes with default empty strings or lists."""
        self.num = ''               # Number of certifications
        self.date = ''              # Date of certification
        self.os = ''                # Operating system skills
        self.language = ''          # Programming languages
        self.tool = ''              # Tools known
        self.application = ''       # Applications known
        self.soft_skills = ''       # Soft skills
        self.cert_name = ''         # Certification name
        self.cert_code = ''         # Certification code
        self.cert_list = []         # List of all certifications

    def skill(self, *ui_data):
        """
        Collects skill-related information from the user.
        If data is provided via 'ui_data', it uses that instead of prompting input.

        Parameters:
        *ui_data: optional tuple containing os, language, tool, application, soft_skills
        """
        if ui_data:  # Use provided info if available
            self.os = ui_data[0]
            self.language = ui_data[1]
            self.tool = ui_data[2]
            self.application = ui_data[3]
            self.soft_skills = ui_data[4]
            return  # <-- return early to avoid asking for input again

        # Prompt the user for skill information
        self.os = input("Operating System: ").strip()
        self.language = input("Programming Language(s): ").strip()
        self.tool = input("Tool(s): ").strip()
        self.application = input("Application(s): ").strip()
        self.soft_skills = input("Soft Skills: ").strip()

    def certs(self, *ui_data):
        """
        Collects certification information from the user.
        If data is provided via 'ui_data', it uses that instead of prompting input.

        Parameters:
        *ui_data: optional tuple containing cert_name, cert_code, cert_list
        """
        if ui_data:  # Use provided info if available
            self.cert_name = ui_data[0]
            self.cert_code = ui_data[1]
            self.cert_list = ui_data[2]
            return  # <-- return early to avoid asking for input again

        # Ask how many certifications the user has
        try:
            self.num = int(input("How many certifications do you have? Enter 0 to skip: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return

        # Collect details for each certification
        while self.num > 0:
            self.date = input("Date received: ").strip()
            self.cert_name = input("Certification name: ").strip()
            self.cert_code = input("Certification code: ").strip()
            cert_info = f"{self.cert_name} ({self.cert_code}) - {self.date}"
            self.cert_list.append(cert_info)
            self.num -= 1

    def __str__(self):
        """
        Returns a formatted string representing the user's skills and certifications.
        This is used when printing the object.
        """
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
    """Main function to run the program and collect/display user's skills and certifications."""
    print("\n=== Information Entry: Skills & Certifications (Non-AI) ===")
    user = BodyPart2()  # Create a BodyPart2 object
    user.skill()        # Collect skill information
    user.certs()        # Collect certification information
    print(user)         # Print the formatted information


if __name__ == "__main__":
    """Entry point of the script."""
    main()
