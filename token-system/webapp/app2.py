import os
import streamlit as st
import requests

SERVER_URL = "http://localhost:5000"

st.title("Food Token System")

menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Admin"])

if menu == "Register":
    st.header("User Registration")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    tokens = st.number_input("Tokens", min_value=1, step=1)
    
    if st.button("Register"):
        res = requests.post(f"{SERVER_URL}/register", json={"name": name, "email": email, "phone": phone, "tokens": tokens})
        if res.status_code == 200:
            st.success("Registered successfully")
            qr_code_path = os.path.abspath(res.json()["qrCode"])
            if os.path.exists(qr_code_path):
                st.image(qr_code_path)
            else:
                st.error("QR Code not found. Try re-registering.")
        else:
            st.error(res.json()["error"])

elif menu == "Login":
    st.header("User Login")
    phone = st.text_input("Phone")
    
    if st.button("Login"):
        res = requests.post(f"{SERVER_URL}/login", json={"phone": phone})
        if res.status_code == 200:
            data = res.json()
            st.success(f"Welcome {data['name']}, Tokens: {data['tokens']}")
            qr_code_path = os.path.abspath(data["qrCode"])
            st.image(qr_code_path)
        else:
            st.error(res.json()["error"])

elif menu == "Admin":
    st.header("Admin Login")
    admin_name = st.text_input("Admin Name")
    password = st.text_input("Password", type="password")
    
    if admin_name == "admin" and password == "Nfsu7009!":
        phone = st.text_input("User Phone to Redeem Token")
        if st.button("Redeem"):
            res = requests.post(f"{SERVER_URL}/admin/redeem", json={"phone": phone})
            if res.status_code == 200:
                st.success(res.json()["message"])
            else:
                st.error(res.json()["error"])
    else:
        st.warning("Invalid credentials")
