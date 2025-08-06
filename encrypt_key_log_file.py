#>>>>>>> A Script that Authenticate user credentials, set delays for too many attempts, Encrypt the log file - 
# so it can't be read in plain text>>>>>>>> 
#I'm just going to experiment it with a simple login system 

from cryptography.fernet import Fernet      # the cyrptography module gives simple, strong symmeric encryption (same key to encrypt and decrypt)
import os           #Checks if a file exists
import time         #Time module imported
import datetime     #datetime module imported



KEY_PATH = "secret.key"


#To generate the encryption key
if not os.path.exists(KEY_PATH):
    key = Fernet.generate_key()
    #this line opens and saves the secret-key to a file. - And it also opens a file in write-binary mode "(wb)"
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)

#opens th "secret.key" file if it already exist
else:
    with open(KEY_PATH, "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)


username = "******"
password = "******"
attempts = 0
max_attempts = 3



#While loop which control the repeat structure of the script begins
while attempts < max_attempts:
    #collect the user inputs
    user_inpu1 = input("Enter Username:     ")
    user_inpu2 = input("Enter Password:     ")

    #conditoinal statement to verify users inputs begins
    if user_inpu1 == username and user_inpu2 == password:
        current_time = datetime.datetime.now()
        print(f"Login Successful!", current_time)
        message = f"Login Successful! {current_time}"
        encrypted_message = fernet.encrypt(message.encode())
    
        #writing/documentin to "login_log_encryped.txt" file
        with open("login_log_encrypt.txt", "ab") as file:
            file.write(encrypted_message + b"\n")

        #writing/documenting to "login_log.txt" file
        #but this log file is not encrypted - just for my personal later use...
        with open("login_log.txt", "a") as file:
            file.write(f"(Encrypted program) - Login Successful! {current_time} \n")
            
        break
    else:
        attempts += 1
        print(f"Login Failed! You have {max_attempts - attempts} attempts left")

        if attempts == max_attempts:
            current_time = datetime.datetime.now()
            message = f"Login Failed! {current_time}"
            encrypted_message = fernet.encrypt(message.encode())

            #A message indicating that a 10 seconds wait time is coming up/on going
            print("Too many attempts. Please wait for 15 seconds and RETRY", current_time) 
            #A 15 secconds wait time     
            time.sleep(15)   
            #A notification to inform user to try inputing details agafter the 10 seconds wait   
            print("You can now retry again")

            #writing/documentin to "login_log_encryped.txt" file
            with open("login_log_encrypt.txt", "ab") as file:
                file.write(encrypted_message + b"\n")

            #writing/documenting to "login_log.txt"
            #this log file "login_log.txt" is not encrypted - just for my personal later use...
            with open("login_log.txt", "a") as file:
                file.write(f"(Encrypted program) - Login Failed! {current_time} \n")
        #break       #this break statement disables the RETRY 

#This "attemps = 0" enables the RETRY 
attempts = 0
        



