class Personal:
    def __init__(self):
        self.full_name = ""
        self.email = ""
        self.email_end=""
        self.phone = ""

    def collect_info(self):
        self.full_name = input("Enter your full name: ").strip()
        self.email = input("Enter your personal email: ").strip()
        self.email_end=input("Enter platform email used: yahoo? gmail?").strip()
        self.phone = input("Enter your personal phone number: ").strip()

    def __str__(self):
        return f"{self.full_name} | Email: {self.email}@{self.email_end}.com | Phone: {self.phone}"
