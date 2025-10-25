class Personal:
    """Class to store and manage personal and educational information of a user."""

    def __init__(self):
        """Initialize all attributes to empty strings by default."""
        self.full_name = ""  # User's full name
        self.email = ""  # User's email name (before the '@')
        self.phone = ""  # User's phone number
        self.email2 = " "  # Email provider (gmail, yahoo, outlook, etc.)
        self.start = ''  # Start date of education
        self.end = ''  # End date of education
        self.major = ''  # User's major/field of study
        self.school = ''  # School or university name

    def collect_info(self, *ui_data):
        """
        Collects personal information from the user.
        If data is provided via 'ui_data', it uses that instead of prompting input.

        Parameters:
        *ui_data: optional tuple containing full_name, email, and phone in that order
        """
        if ui_data:  # Use provided info if available
            self.full_name = ui_data[0]
            self.email = ui_data[1]
            self.phone = ui_data[2]
            return

        # Prompt user for information if not provided
        self.full_name = input("Enter your full name: ").strip()
        self.email = input("Enter your personal email name (before @): ").strip()
        self.email2 = input("Enter your email provider (gmail, yahoo, outlook): ").strip()
        self.phone = input("Enter your personal phone number: ").strip()

    def education(self, *ui_data):
        """
        Collects educational information from the user.
        If data is provided via 'ui_data', it uses that instead of prompting input.

        Parameters:
        *ui_data: optional tuple containing major, start date, end date, and school
        """
        if ui_data:  # Use provided info if available
            self.major = ui_data[0]
            self.start = ui_data[1]
            self.end = ui_data[2]
            self.school = ui_data[3]
            return  # <-- ensure it does not ask for input again

        # Prompt user for information if not provided
        self.major = input("Enter your major: ").strip()
        self.start = input("Enter start date of your major: ").strip()
        self.end = input("Enter end date of your major: ").strip()
        self.school = input("School attending: ").strip()

    def __str__(self):
        """
        Returns a formatted string representing the user's personal and educational information.
        This is used when printing the object.
        """
        return (f"{self.full_name}\n"
                f" | Email: {self.email}@{self.email2}.com | Phone: {self.phone}\n"
                f"Education: {self.major} | {self.school}  date: {self.start}-{self.end}")


def main():
    """Main function to run the program and collect/display user information."""
    print("\n=== Top of resume: personal information ===")
    user = Personal()  # Create a Personal object
    user.collect_info()  # Collect personal info from the user

    print("\n=== Top of resume: Education information ===")
    user.education()  # Collect education info from the user

    print(user)  # Print the formatted resume information


if __name__ == "__main__":
    """Entry point of the script."""
    main()
