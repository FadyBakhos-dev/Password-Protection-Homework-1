import hashlib
import uuid
from datetime import datetime

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

t1=[]
t2=[]
t3=[]

while True:
    username=input("Enter your username ")
    passwordd=input("Enter your password ")
    user_id=str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    salt = sha256_hash(username + user_id + timestamp)

    pass_hashed=sha256_hash(passwordd)
    pass_salted=sha256_hash(salt+passwordd)

    t1.append({"user_id": user_id, "username": username, "password_plain": passwordd})

    t2.append({"user_id": user_id, "username": username, "password_hash": pass_hashed})

    t3.append({"user_id": user_id, "username": username, "timestamp": timestamp, "salt": salt, "password_salted_hash": pass_salted})

    again = input("Register another user? (y/n) ")
    if again.lower() != "y":
        break

print()
print("Table 1 Plain password ")
for row in t1:
    print("user_id:", row["user_id"])
    print("username:", row["username"])
    print("password_plain:", row["password_plain"])
    print()

print(" Table 2 Hashed password ")
for row in t2:
    print("user_id:", row["user_id"])
    print("username:", row["username"])
    print("password_hash:", row["password_hash"])
    print()

print(" Table 3 Salt + hashed password ")
for row in t3:
    print("user_id:", row["user_id"])
    print("username:", row["username"])
    print("timestamp:", row["timestamp"])
    print("salt:", row["salt"])
    print("password_salted_hash:", row["password_salted_hash"])
    print()

print("Login")
while True:
    login_username = input("Login username ")
    login_password = input("Login password ")

    result1 = "FAILED"
    for row in t1:
        if row["username"] == login_username and row["password_plain"] == login_password:
            result1 = "SUCCESS"

    result2 = "FAILED"
    typed_hash = sha256_hash(login_password)
    for row in t2:
        if row["username"] == login_username and row["password_hash"] == typed_hash:
            result2 = "SUCCESS"

    result3 = "FAILED"
    for row in t3:
        if row["username"] == login_username:
            typed_salted = sha256_hash(row["salt"] + login_password)
            if row["password_salted_hash"] == typed_salted:
                result3 = "SUCCESS"

    print("Table 1:", result1)
    print("Table 2:", result2)
    print("Table 3:", result3)
    print()

    again = input("Try another login? (y/n) ")
    if again.lower() != "y":
        break