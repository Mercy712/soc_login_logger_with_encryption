# Failed Login Attempt Detector with Brute-Force Alert (Python)

This simple Python script simulates a basic login system that:
- Allows up to 3 login attempts
- Logs successful and failed attempts
- Blocks access after 3 failed tries (simulating a brute-force alert)

---

## Key Concepts Learned

- Conditional logic and loops
- Tracking login attempts
- Using `datetime` for timestamps
- Writing logs to a file (`login_log.txt`)

---

## How It Works

- User enters a username and password.
- If correct: login is successful and logged.
- If wrong: attempts increase until 3 tries.
- On 3 failed attempts: access is blocked and logged as a potential brute-force attack.

---

## Logging Activity

All events (success or block) are recorded in `login_log.txt` using:
```python
with open("login_log.txt", "a") as file:
    file.write(f"Login Successful - {current_time}")

This mimics how SOC analyst log authentication events.
---

What's Next?
-Add encryption to log data
-Consider addding a delay time and retry feature rather than a total blockout.
 


----


---

## 🙌 Author

Mercy712 
SOC Analyst in Training | Cybersecurity Learner | Python Learner  
📍 Connect with me on LinkedIn via www.linkedin.com/in/mercy-ikeh-8946482aa 

