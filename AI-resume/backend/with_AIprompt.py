
class body:
    def __init__(self):
        self.num = ''
        self.posi = ''
        self.company = ''
        self.major = ''
        self.start = ''
        self.end = ''
    def job_expriecne(self):
        #can enter try and except
        self.num= int(input("enter how many job exprience you have, Enter integer:  enter zero to move on  "))
        while self.num < 0:
            self.num = int(input("enter how many job exprience you have, Enter integer:  enter zero to move on  "))
            self.num -= 1
            self.start = input("Enter start date your work:").strip()
            self.end = input("end your major: enter present").strip()
            self.posi = input("Enter position").strip()
            self.company = input("Enter company name").strip()

    def volunteer(self):
        self.num = int(input("enter how many job certs you have, Enter integer:  enter zero to move on  "))
        while self.num < 0:
            self.num -= 1
        self.posi = input("type of volunteering ").strip()
        self.company = input("Enter organization name").strip()
    def prompt(self):
        ...




def main():
    print("\n=== information in the body with AI prompt ===")
    user = body()
    user.job_expriecne()
    user.volunteer()
    print(user)

if __name__ == "__main__":
    main()
