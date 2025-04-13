import streamlit as st
import string
import random
import re

st.title("🦾🧠 Password Strength Meter!")
st.write(" Enter your password below to check its strength🔻")

def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*"
    return "".join(random.choice(characters) for i in range(length))

def check_strength(password):
    score = 0
    common_passwords = ["111111,", "0123456789","0000000","password","1234578","pakistan123"]
    if password in common_passwords :
        return "❌Common passwod not recomended.","Weak Password"
    
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🛡 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🛡 Password should contain both uppercase and lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("🛡 Password should contain at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🛡 Password should contain at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong Password", "Strong Password"
    elif score == 3:
        return "⚠️ Medium Password", "Medium Password"
    else:
        return "\n".join(feedback), "Weak Password"
    
password = st.text_input("Enter your password", type="password")
if st.button("Check Strength"):
    if password:
        feedback, strength = check_strength(password)
        st.success(feedback)
        st.info(f"Password Strength: {strength}")
    elif password == "":
        st.warning("Please enter a password to check its strength.")

st.write("🔑 Generate a random STRONG password")
password_length = st.number_input("Enter the length of password", min_value = 8, max_value = 20 , value = 10)
if st.button("Generate Password"):
    password = generate_password(password_length)
