

class body_part2:
    def __init__(self):
        self.num = ''
        self.posi = ''
        self.company = ''
        self.major = ''
        self.start = ''
        self.end = ''

    def skill(self):

        #hardskill
        #softskiil
        #language
        #tools
        #operating system
        #application


        ...

    def certs(self):
        self.num = int(input("enter how many job certs you have, Enter integer:  enter zero to move on  "))
        while self.num < 0:
            self.num -= 1
            self.start = input("Enter start date for certs received:").strip()
            self.company = input("Enter company name").strip()
            self.num = int(input("enter how many job exprience you have, Enter integer:  enter zero to move on  "))





    def __str__(self):
        ...

def main():
    print("\n=== information in the body no AI ===")
    user = body_part2()
    user.skill()
    print(user)

if __name__ == "__main__":
    main()
