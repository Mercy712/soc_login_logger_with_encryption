# 🔐 Secure Login System with Encrypted Logging (Beginner SOC Project)

This is a beginner-friendly Python project that started as a **basic login authentication script** and evolved into a **simple security tool** that logs login attempts — and encrypts them for confidentiality.

It mimics how a **SOC (Security Operations Center) analyst** might monitor and protect user login activity on a local system.

---

## Key Concepts Learned

- Conditional logic and loops
- Tracking login attempts
- Using `datetime` for timestamps
- Writing logs to a file (`login_log.txt`)

---

## How It Works

-On first run, an encryption key is generated and saved.
- The user is asked to input a username and password.
- If correct:
  A “Login Successful” message is encrypted and saved to login_log_encrypt.txt
-If incorrect:
    Failed attempts are tracked.
    After 3 tries, the user is locked out for 15 seconds.
    A “Login Failed” message is encrypted and saved.
- At the end, all encrypted logs are decrypted and displayed (if valid key exists)
----

## Logging Activity

All events (success or block) are recorded in `login_log.txt` using:
```python
with open("login_log.txt", "a") as file:
    file.write(f"Login Successful - {current_time}")

This mimics how SOC analyst log authentication events.
---

## Tech Stack
- Python 3
- cryptography
-"datetime", "os", "time" (buil-in Python modules)


---

## Evolution of the Project

Step 1  Basic login script with authentication         
Step 2  Added timestamp and log saving                 
Step 3  Implemented retry + delay mechanism            
Step 4  Introduced encryption with `cryptography`      
Step 5  Built decryption tool to view encrypted logs   
Step 6  Final version with everything working together 


## 🙌 Author

Mercy712 
SOC 1 Analyst| leveraging Python to build hands-on SOC tools | Cybersecurity Learner | Curious. Persistent. Always experimenting. 
📍 Connect with me on LinkedIn via www.linkedin.com/in/mercy-ikeh-8946482aa 

