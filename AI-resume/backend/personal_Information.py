

class Personal:
    def __init__(self):
        self.full_name = ""
        self.email = ""
        self.phone = ""
        self.email2= " "
        self.start = ''
        self.end = ''
        self.major = ''
        self.school = ''

    def collect_info(self, *ui_data): #todo ui merging
        if ui_data: #todo make sure to add this for alllllllll
            self.full_name = ui_data[0]
            self.email = ui_data[1]
            self.phone = ui_data[2]
            return
        self.full_name = input("Enter your full name: ").strip()
        self.email = input("Enter your personal email_name: ").strip()
        self.email2 = input("Enter your email provider (gmail,yahoo, outlook ): ").strip()
        self.phone = input("Enter your personal phone number: ").strip()

    def education(self, *ui_data):
        if ui_data:
            self.major = ui_data[0]
            self.start = ui_data[1]
            self.end = ui_data[2]
            self.school = ui_data[3]

        self.major = input("Enter your major: ").strip()
        self.start = input("Enter start date your major:").strip()
        self.end = input("end your major: ").strip()
        self.school = input("School attending: ").strip()

    def __str__(self):
        return (f"{self.full_name}\n "
                f" | Email: {self.email}@{self.email2}.com| Phone: {self.phone}\n"
                f"Education:  {self.major} | {self.school}                       date:{self.start}-{self.end}")


def main():
    print("\n=== Top of resume: personal information ===")
    user = Personal()
    user.collect_info()
    print("\n=== Top of resume: Education information ===")
    user.education()
    print(user)

if __name__ == "__main__":
    main()
