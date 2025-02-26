import random
import re

roasts = ["Are you trying to speedrun the ‘Biggest Disappointment’ leaderboard? Because you’re winning.",
          "Wow, even a broken clock makes better choices than you.",
          "I’d explain what went wrong, but I don’t speak ‘clueless.’",
          "If thinking was an Olympic sport, you’d be watching from the sidelines.",
          "I’d say ‘Try again,’ but at this point, I’ve lost all hope.",
          "Your brain must be on airplane mode. Turn it back on and try again.",
          "That choice was so bad, even ChatGPT is questioning your existence.",
          "You had one chance to prove you’re smarter than a potato… and you failed.",
          "Even my RAM has better memory than you.",
          "You're the reason tutorial videos start with ‘Hello everyone, except this guy.’"]
            

class AccountManager:
    def __init__(self , filename = "Accounts.txt"):
        self.filename = filename


    def Register(self):
        userProfile ={}

        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_no = input("Enter Phone Number: ")
        while True:
            password = input("Create a Password: ")
            confirmedPassword = input("Confirm Your Password: ")

            if password == confirmedPassword:
                break 
            else:
                print("Passwords do not match! Try again.")

        userProfile["fullName"] = firstName + lastName
        userProfile["email"] = email
        userProfile["phone_no"] = phone_no
        userProfile["password"] = password

        file = open(self.filename,'a')
        file.write(str(userProfile) + "\n")
        print("Registration Successful!")
        return email


    def Login(self):
        file = open(self.filename, 'r')
        content = file.read().strip()
        file.close()
        formatted_content = "[" + content.replace("}\n{", "},\n{") + "]"
        loadedDic = eval(formatted_content)

        while True:
            email = input("Enter Your Email: ")
            password = input("Enter Your Password: ")

            for i in range(len(loadedDic)):
                if(loadedDic[i]["email"] == email and loadedDic[i]["password"] == password):
                    print("login Successfuly!")
                    return email
                
            print("invalid userName or password")


class ProjectsManager:
    numberPattern = r"^[1-9]\d*$"
    datePattern = r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/]([0-9]{4})$"

    def __init__(self , filename = "Projects.txt"):
        self.filename = filename

    def createProjects(self , loggedEmail):
        projectData = {}

        Title = input("Enter New Project Tiltle: ")
        Details = input("Enter The Project Details: ")
        while True:
            totalTarget = input("Enter Target Amount For The Project: ")
            if re.match(self.numberPattern, totalTarget):
                break
            else:
                print(random.choice(roasts))
                totalTarget = input("Enter Target Amount For The Project: ")

        while True:
            startTime = input("Enter Start Time of The Project in Form DD/MM/YYYY: ")
            if re.match(self.datePattern, startTime):
                break
            else:
                print(random.choice(roasts))
                startTime = input("Enter Start Time of The Project in Form DD/MM/YYYY: ")

        while True:
            endTime = input("Enter End Time of The Project in Form DD/MM/YYYY: ")
            if re.match(self.datePattern, endTime):
                break
            else:
                print(random.choice(roasts))
                endTime = input("Enter End Time of The Project in Form DD/MM/YYYY: ")

        projectData["Owner"] = loggedEmail
        projectData["Title"] = Title
        projectData["Details"] = Details
        projectData["totalTarget"] = totalTarget
        projectData["startTime"] = startTime
        projectData["endTime"] = endTime

        file = open(self.filename,'a')
        file.write(str(projectData) + "\n")

        print("Project Created Successfully!")

        
    def showProjects(self):
        file = open(self.filename, 'r')
        content = file.readlines()
        file.close()

        count = 1
        for line in content:
            print(f"{count} - {line.strip()}")
            count += 1
    
    def searchInProjects(self):
        keyword = input("Enter Project Start Date to search (DD/MM/YYYY or DD-MM-YYYY): ").strip()

        if not re.match(self.datePattern, keyword):
            print("Invalid date format! Please use DD/MM/YYYY or DD-MM-YYYY.")
            return

        file = open(self.filename, 'r')
        lines = file.readlines()
        file.close()

        found_lines = [line.strip() for line in lines if keyword in line]

        if found_lines:
            print(f"\nFound {len(found_lines)} match(es) for '{keyword}':")
            for line in found_lines:
                print(f"- {line}")
        else:
            print(f"No matches found for '{keyword}'.")


auth_system = AccountManager()

print("-Enter 1 For Register.")
print("-Enter 2 For Login.")
print("-Enter 3 To Exit.")
option = int(input("Choose The Number Of Action: "))
while True:
    if(option == 1):
        auth_system.Register()
        break
    elif(option == 2):
        loggedEmail = auth_system.Login()
        break
    elif(option == 3):
        exit()
    else:
        print(random.choice(roasts))
        option = int(input("Choose 1 to Register, 2 to Login , 3 to Exit: ")) 

project_system = ProjectsManager()

while True:
    print("-Enter 1 To Create New Project.")
    print("-Enter 2 To Show All Projects.")
    print("-Enter 3 To Search For Project.")
    print("-Enter 4 To Exit.")
    option = input("Choose The Number Of Action: ")

    if(option == "1"):
        project_system.createProjects(loggedEmail)
    elif(option == "2"):
        project_system.showProjects()
    elif(option == "3"):
        project_system.searchInProjects()
    elif(option == "4"):
        print("Exiting Project Management. Goodbye!")
        break
    else:
        print(random.choice(roasts))
        option = input("Choose 1 to Create New Project, 2 to Show All Projects , 3 to Search For Project , 4 To Exit: ") 

