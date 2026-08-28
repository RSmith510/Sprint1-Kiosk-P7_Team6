# BCH Software Inc. - Sprint 1: Interactive Kiosk
# Track: Python Software Engineering
<<<<<<< Updated upstream
# <<<<<<< HEAD
# 8/21 Tanner Soldinski
# =======
# 8/21/ryan
# code only prints correct ASCII format if you use 
# name = Jane Doe
# org BCH Cybersecurity Division
# contact jdoe@bchsoftware.org
# access VIP ALL-ACCESS
=======
#8/21 braylon underwood

>>>>>>> Stashed changes
def main():
    print("========================================")
    print("      BCH ENTERPRISE VISITOR KIOSK      ")
    print("========================================")
    name =""
    org = ""
    contact =""
    acces= ""
    print ("APEX VISITOR CHECK-IN")
    print("enter your full name")
    name = input()
    print("enter your organization")
    org = input()
    print("enter your email contact")
    contact = input()
    print("enter your access level")
    acces= input()

    print("+------------------------------------------+")
    print("|                     Apex visitor Pass    |")
    print("|------------------------------------------|")
    print("| ATTENDE : "+name+"                       |")
    print("| ORG     : "+org+"     |")
    print("| CONTACT : "+contact +"           |")
    print("| ACCESS  : "+acces+ "                 |")
    print("| ISSUER  : BCH Software Terminal Security |")
    print("+------------------------------------------+")

if __name__ == "__main__":
    main()
