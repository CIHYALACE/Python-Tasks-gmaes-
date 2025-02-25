import random

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
    

    def Login(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        file = open(self.filename, 'r')
        content = file.read().strip()
        file.close()

        formatted_content = "[" + content.replace("}\n{", "},\n{") + "]"

        loadedDic = eval(formatted_content)
        for i in range(len(loadedDic)):
            if(loadedDic[i]["email"] == email and loadedDic[i]["password"] == password):
                print("login Successfuly!")
            else:
                print("invalid userName or password")
            break    

auth_system = AccountManager()

option = int(input("Choose The Number Of Action: 1-Dont Have An Account (Register) , 2-Have An Account (Login):"))
while True:
    if(option == 1):
        auth_system.Register()
        break
    elif(option == 2):
        auth_system.Login()
        break
    else:
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
            
        print(random.choice(roasts))
        option = int(input("Choose 1 to Register, 2 to Login: ")) 

