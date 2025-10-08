

class Personal:
    def __init__(self):
        self.full_name = ""
        self.email = ""
        self.phone = ""

    def collect_info(self):
        self.full_name = input("Enter your full name: ").strip()
        self.email = input("Enter your personal email_name: ").strip()
        self.email2 = input("Enter your email provider (gmail,yahoo, outlook ): ").strip()
        self.phone = input("Enter your personal phone number: ").strip()


    def __str__(self):
        return f"{self.full_name} | Email: {self.email}@{self.email2}.com| Phone: {self.phone}"

def main():
    print("\n=== Top of the resume: personal information ===")
    user = Personal()
    user.collect_info()
    print(user)

if __name__ == "__main__":
    main()
