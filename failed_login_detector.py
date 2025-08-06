#>>>>>>>Failed Login Attempt Detector with Alert after 3 Tries


import time
import datetime

username = "soc"
password = "soc234"
attempts = 0 
max_attempts = 3


while attempts < max_attempts:
#   Ask the user for a username and password 
    user_input1 = input("Enter Username:    ")
    user_input2 = input("Enter Password:    ")
    
    if user_input1 == username and user_input2 == password:
        current_time = datetime.datetime.now()
        print("Login Successful", current_time)

    #Writing to a file in python
        with open("login_log.txt", "a") as file:          #"a" means append mode, not overwrite
            file.write(f"Login Successful - {current_time} \n") #creating a file for new entries, as a SOC analyst i need to build my first real logging system.

        break
    else:
        attempts += 1  #Important!      Increasing the numeber of failed login attempts until it get to 3
        print(f"Login Attempt failed! You have {max_attempts - attempts} attempts left")

        if attempts == max_attempts:
            current_time = datetime.datetime.now()
            print("Account Blocked! Suspeccted brute-force attack", current_time)

        #Writing to a file in python
            with open("login_log.txt", "a") as file:          #"a" means append mode, not overwrite
                file.write(f"Account Blocked! Suspeccted brute-force attack- {current_time} \n") #creating a file for new entries, as a SOC analyst i need to build my first real logging system.
