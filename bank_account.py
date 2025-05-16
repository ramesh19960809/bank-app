import random
from datetime import datetime

Account = {}


#-------------------- User Account --------------------

def login():
    username = input ("Enter Your Name: ")
    password = input ("Enter Your Password: ")

    try:
        with open("login.txt","r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 3:
                    saved_user, saved_pass, role = parts
                    if username == saved_user and password == saved_pass:
                        print(f"Login Successfully. Welcome...{username}")
                        return role, username
            print("Invalid UserName or Password")
            return None, None
    except FileNotFoundError:
        print("Error")
        return None, None

                
#----------------------- Admin Menu -------------------------

def Adminmenu():
    while True:
        print("\n====== Admin Banking Menu ======")
        print("Account Creation. ==========[1]")
        print("Deposit Money. =============[2]")
        print("Withdraw Money. ============[3]")
        print("Check Balance. =============[4]")
        print("Transaction History. =======[5]")
        print("Transer Money. =============[6]")
        print("Change Password. ===========[7]")
        print("Exit. ======================[8]")



        Choice = input("Choose your choice (1-8):")
        if Choice == "1":
            Account_Creation()
        elif Choice == "2":
            Deposit_Money()
        elif  Choice == "3":
            Withdraw_Money()
        elif Choice == "4":
            Check_Balance()
        elif Choice == "5":
            Transaction_History()
        elif Choice == "6":
            Transer_Money()
        elif Choice == "7":
            Change_Password()
        elif Choice == "8":
            print("Thank You.")
            break
        else:
            print("Invalid Chice")


#------------------------ User Menu --------------------------------

def Usermenu():
    while True:
        print("\n====== User Banking Menu ======")
        print("Deposit Money ===============[1]")
        print("Withdraw Money ==============[2]")
        print("Check Balance ===============[3]")
        print("Transaction History =========[4]")
        print("Transer Money ===============[5]")
        print("Exit ========================[6]")


        Choice = input("Choose your choice (1-6):")
        if Choice == "1":
            Deposit_Money()
        elif  Choice == "2":
            Withdraw_Money()
        elif Choice == "3":
            Check_Balance()
        elif Choice == "4":
            Transaction_History()
        elif Choice == "5":
            Transer_Money()
        elif Choice == "6":
            print("Thank You.")
            break
        else:
            print("Invalid Chice")


#--------------------------- Account Creation -------------------------

def Account_Creation ():
    name = input("Enter Your Name:")
    user_name = input("Entert Your User Name: ")
    user_password = input("Eanter Your Password: ")

    while True:
        try:
            Minimum_Balance = float(input("Enter Your Minimum Balance: "))
            if Minimum_Balance < 0:
                print("Minimum Balance Must be non - nagative: ")
                continue
            break
        except ValueError:
            print("Enter The Number only: ")


    account_number = str(random.randint(10000, 99999))
    while account_number in Account:
        account_number = str(random.randint(10000, 99999))

    Account[account_number] = {
        "Name": name,
        "Balance": Minimum_Balance,
        "Transactions": []
        }
    save_account_to_file(account_number,name,user_name,user_password, Minimum_Balance)
    append_login_creadentials(user_name, user_password)

def save_account_to_file(account_number, name, user_name, user_password, Minimum_Balance):
    with open("create.txt", "a") as file:
        file.write(f"{account_number}:{name}:{user_name}:{user_password}:{Minimum_Balance:.2f}\n")
    
    print(f"Account created syccessfullu.Account Number: {account_number}")

def append_login_creadentials(usernane, password, role="user"):
    with open ("login.txt", "a") as file:
        file.write(f"{usernane}:{password}:{role}\n")



#----------------------------- Deposit Money ----------------------------

def Deposit_Money():

    account_number = input("Enter your Account Number: ")
    if account_number not in Account:
        print("Account Not Available")
        return
    
    try:
        amount = float(input("Enter your Amount to for Deposit: "))
        if amount <= 0:
            print("Amount Must be Greater than 0")
            return
        Account[account_number]["Balance"] += amount
        Account[account_number]["Transactions"].append(f"Deposited ${amount:.2f}")
        print(f"Deposited Successfully. New Balance: ${Account[account_number]["Balance"]:.2f}")
    except ValueError:
        print("Invalid Amount")


#----------------------------- Withdraw Money ------------------------------

def Withdraw_Money():

    account_number = input("Enter Your Account Number: ")
    if account_number not in Account:
        print("Account not amount.")
        return
    try:
        amount = float(input("Enter Your Withdraw: "))
        if amount <= 0:
            print("Amount Must be Greater than 0")
            return
        if amount > Account[account_number]["Balance"]:
            print("No Balance")
            return
        Account[account_number]["Balance"] -= amount
        Account[account_number]["Transactions"].append(f"Withdrew ${amount:.2f}")
        print(f"Withdrawal successful. New Balance: ${Account[account_number]["Balance"]:.2f}")
    except ValueError:
        print("Invalid Amount")
 


#-------------------------------- Check Balance -------------------------------

def Check_Balance():

    try:
        with open("create.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 5:
                    acc_no, name, user, pwd, balance = parts
                    Account[acc_no] = {
                        "Name": name,
                        "Balance": float(balance),
                        "Transactions": []
                    }
    except FileNotFoundError:
        print("Account data file not found.")
        return

    account_number = input("Enter your Account Number: ")
    if account_number not in Account:
        print("Account not Available")
        return
    print(f"Current Balance: ${Account[account_number]['Balance']:.2f}")


#------------------------------ Transaction History ----------------------------

def Transaction_History():

    account_number = input("Enter Your Account Number: ")
    if account_number not in Account:
        print("Account not Available")
        return

    transaction = Account[account_number]["Transactions"]
    if not transaction:
        print("Can Not Trasactions")
        return
    print("Transaction History: ")
    for t in transaction:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{now}- {t}")


#--------------------------------- Transer Money -------------------------------

def Transer_Money():

    try:
        with open("create.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 5:
                    acc_no, name, user, pwd, balance = parts
                    Account[acc_no] = {
                        "Name": name,
                        "Balance": float(balance),
                        "Transactions": []
                    }
    except FileNotFoundError:
        print("Account data file not found.")
        return

    from_acc = input("Enter your Account Number: ")
    if from_acc not in Account:
        print("Sender Account Number is Wrong.")
        return

    to_acc = input("Enter Recipient Account Number: ")
    if to_acc not in Account:
        print("Recipient Account Number is Wrong.")
        return

    try:
        amount = float(input("Enter Amount to Transfer: "))
        if amount <= 0:
            print("Amount Must be Greater than 0.")
            return
        if amount > Account[from_acc]["Balance"]:
            print("Insufficient Balance on Account")
            return

        Account[from_acc]["Balance"] -= amount
        Account[to_acc]["Balance"] += amount
        Account[from_acc]["Transactions"].append(f"Transferred ${amount:.2f} to {to_acc}")
        Account[to_acc]["Transactions"].append(f"Received ${amount:.2f} from {from_acc}")
        print(f"Transfer Successful. ${amount:.2f} transferred from {from_acc} to {to_acc}")
    except ValueError:
        print("Invalid Amount.")




#--------------------------- Change Password ----------------------------

def Change_Password():
    UserNAME = input("Enter Your User Name: ")
    Old_Password = input("Ender Your Old Password: ")

    updated_lines = []
    found = False

    try:
        with open ("login.txt","r")as file:
            for line in file:
                parts = line.strip().split(':')

                if len(parts) !=3:
                    updated_lines.append(line)
                    continue

                saved_user, saved_pass, role = parts
                if UserNAME == saved_user and Old_Password == saved_pass:
                    New_Password = input("Enter Your New Password: ")
                    updated_lines.append(f"{UserNAME}:{New_Password}:{role}\n")
                    found = True
                else:
                    updated_lines.append(line)

        if found:
            with open("login.txt", "w") as file:
                file.writelines(updated_lines)
                print("Password Changed Successfully")
        
        else:
            print("Incorrect User Name or Password.")

    except FileNotFoundError:
        print("Something Error Plese Try Again")


#---------------------- Calling Main ------------------------------------

def main():
    role, username = login()
    if role is None:
        print("Login failed.Exiting. ")
        return
    if role == "admin":
        Adminmenu()
    elif role == "user":
        Usermenu()
    else:
        print("Invalid User Name Password.")

main()