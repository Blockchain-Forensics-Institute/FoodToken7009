#1 ------------------------------
# import os
# import streamlit as st
# import requests
# import qrcode
# from PIL import Image
# import io

# SERVER_URL = "http://localhost:5000"

# st.title("🍽️ Food Token System")

# menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Admin"])

# def generate_qr_code(data):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image(fill="black", back_color="white")

#     # Convert QR code image to bytes for Streamlit
#     img_bytes = io.BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)
#     return img_bytes

# if menu == "Register":
#     st.header("📝 User Registration")
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#     tokens = st.number_input("Tokens", min_value=1, step=1)
    
#     if st.button("Register"):
#         res = requests.post(f"{SERVER_URL}/register", json={"name": name, "email": email, "phone": phone, "tokens": tokens})
#         if res.status_code == 200:
#             st.success("✅ Registered successfully! Redirecting to dashboard...")
#             user_data = res.json()
#             st.session_state["user"] = user_data
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# if "user" in st.session_state:
#     user = st.session_state["user"]
#     st.header(f"👤 {user['name']}'s Dashboard")
#     st.write(f"📞 Phone: {user['phone']}")
#     st.write(f"📧 Email: {user['email']}")
#     st.write(f"🔢 Tokens Left: {user['tokens']}")
    
#     qr_code_bytes = generate_qr_code(f"User: {user['name']}, Phone: {user['phone']}, Tokens: {user['tokens']}")
#     st.image(qr_code_bytes, caption="Your QR Code", use_container_width=True)

# elif menu == "Login":
#     st.header("🔑 User Login")
#     phone = st.text_input("Phone")
    
#     if st.button("Login"):
#         res = requests.post(f"{SERVER_URL}/login", json={"phone": phone})
#         if res.status_code == 200:
#             user_data = res.json()
#             st.success(f"✅ Welcome {user_data['name']}! Redirecting to dashboard...")
#             st.session_state["user"] = user_data
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# elif menu == "Admin":
#     st.header("🛠️ Admin Panel")
#     admin_name = st.text_input("Admin Name")
#     password = st.text_input("Password", type="password")
    
#     if admin_name == "admin" and password == "Nfsu7009!":
#         st.success("✅ Admin authenticated!")
        
#         uploaded_file = st.file_uploader("📷 Scan QR Code to Redeem", type=["png", "jpg", "jpeg"])
#         tokens_to_redeem = st.number_input("Tokens to Redeem", min_value=1, step=1)
        
#         if uploaded_file and st.button("Redeem Token"):
#             try:
#                 img = Image.open(uploaded_file)
#                 decoded_text = img  # QR Code decoding logic needed
                
#                 phone_number = decoded_text.split(", Phone: ")[1].split(",")[0]
#                 res = requests.post(f"{SERVER_URL}/admin/redeem", json={"phone": phone_number, "tokens": tokens_to_redeem})
#                 if res.status_code == 200:
#                     st.success(res.json()["message"])
#                 else:
#                     st.error(res.json()["error"])
#             except Exception as e:
#                 st.error("Failed to decode QR code. Please try again.")
#     else:
#         st.warning("Invalid credentials")



#2 ---------------------------------------------------- ------------------------------
# import os
# import streamlit as st
# import requests
# import qrcode
# from PIL import Image
# import io

# SERVER_URL = "http://localhost:5000"

# st.title("🍽️ Food Token System")

# menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Admin"])

# def generate_qr_code(data):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image(fill="black", back_color="white")

#     # Convert QR code image to bytes for Streamlit
#     img_bytes = io.BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)
#     return img_bytes

# if menu == "Register":
#     st.header("📝 User Registration")
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#     tokens = st.number_input("Tokens", min_value=1, step=1)
    
#     if st.button("Register"):
#         res = requests.post(f"{SERVER_URL}/register", json={"name": name, "email": email, "phone": phone, "tokens": tokens})
#         if res.status_code == 200:
#             st.success("✅ Registered successfully! Redirecting to dashboard...")
#             user_data = res.json()
#             st.session_state["user"] = user_data
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# if "user" in st.session_state:
#     user = st.session_state["user"]
#     st.header(f"👤 {user['name']}'s Dashboard")
#     st.write(f"📞 Phone: {user['phone']}")
#     st.write(f"📧 Email: {user['email']}")
#     st.write(f"🔢 Tokens Left: {user['tokens']}")
    
#     qr_code_bytes = generate_qr_code(f"User: {user['name']}, Phone: {user['phone']}, Tokens: {user['tokens']}")
#     st.image(qr_code_bytes, caption="Your QR Code", use_container_width=True)
    
#     if st.button("Logout") or st.button("Back"):
#         del st.session_state["user"]
#         st.rerun()

# elif menu == "Login":
#     st.header("🔑 User Login")
#     phone = st.text_input("Phone")
    
#     if st.button("Login"):
#         res = requests.post(f"{SERVER_URL}/login", json={"phone": phone})
#         if res.status_code == 200:
#             user_data = res.json()
#             st.success(f"✅ Welcome {user_data['name']}! Redirecting to dashboard...")
#             st.session_state["user"] = user_data
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# elif menu == "Admin":
#     st.header("🛠️ Admin Panel")
#     admin_name = st.text_input("Admin Name")
#     password = st.text_input("Password", type="password")
    
#     if admin_name == "admin" and password == "Nfsu7009!":
#         st.success("✅ Admin authenticated!")
        
#         uploaded_file = st.file_uploader("📷 Scan QR Code to Redeem", type=["png", "jpg", "jpeg"])
#         tokens_to_redeem = st.number_input("Tokens to Redeem", min_value=1, step=1)
        
#         if uploaded_file and st.button("Redeem Token"):
#             try:
#                 img = Image.open(uploaded_file)
#                 decoded_text = img  # QR Code decoding logic needed
                
#                 phone_number = decoded_text.split(", Phone: ")[1].split(",")[0]
#                 res = requests.post(f"{SERVER_URL}/admin/redeem", json={"phone": phone_number, "tokens": tokens_to_redeem})
#                 if res.status_code == 200:
#                     st.success(res.json()["message"])
#                 else:
#                     st.error(res.json()["error"])
#             except Exception as e:
#                 st.error("Failed to decode QR code. Please try again.")
#     else:
#         st.warning("Invalid credentials")



#3 ---------------------------------------------------- ------------------------------
# import os
# import streamlit as st
# import requests
# import qrcode
# from PIL import Image
# import io

# SERVER_URL = "http://localhost:5000"

# st.title("🍽️ Food Token System")

# # Sidebar Menu
# menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Admin"])

# # Auto logout if the menu is changed
# if "user" in st.session_state and menu != "Register" and menu != "Login":
#     del st.session_state["user"]
#     st.rerun()

# # QR Code Generator
# def generate_qr_code(data):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#     img = qr.make_image(fill="black", back_color="white")
#     img_bytes = io.BytesIO()
#     img.save(img_bytes, format="PNG")
#     img_bytes.seek(0)
#     return img_bytes

# # Register Page
# if menu == "Register":
#     st.header("📝 User Registration")
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#     tokens = st.number_input("Tokens", min_value=1, step=1)

#     if st.button("Register"):
#         res = requests.post(f"{SERVER_URL}/register", json={"name": name, "email": email, "phone": phone, "tokens": tokens})
#         if res.status_code == 200:
#             st.success("✅ Registered successfully! Redirecting to dashboard...")
#             st.session_state["user"] = res.json()
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# # Login Page
# elif menu == "Login":
#     st.header("🔑 User Login")
#     phone = st.text_input("Phone")

#     if st.button("Login"):
#         res = requests.post(f"{SERVER_URL}/login", json={"phone": phone})
#         if res.status_code == 200:
#             st.success(f"✅ Welcome! Redirecting to dashboard...")
#             st.session_state["user"] = res.json()
#             st.rerun()
#         else:
#             st.error(res.json()["error"])

# # User Dashboard
# if "user" in st.session_state:
#     user = st.session_state["user"]

#     if st.button("🔙 Back"):
#         del st.session_state["user"]
#         st.rerun()

#     st.header(f"👤 {user['name']}'s Dashboard")
#     st.write(f"📞 Phone: {user['phone']}")
#     st.write(f"📧 Email: {user['email']}")
#     st.write(f"🔢 Tokens Left: {user['tokens']}")

#     qr_code_bytes = generate_qr_code(f"User: {user['name']}, Phone: {user['phone']}, Tokens: {user['tokens']}")
#     st.image(qr_code_bytes, caption="Your QR Code", use_container_width=True)  # ✅ Updated parameter

#     if st.button("🚪 Logout"):
#         del st.session_state["user"]
#         st.rerun()

# # Admin Panel
# elif menu == "Admin":
#     st.header("🛠️ Admin Panel")
#     admin_name = st.text_input("Admin Name")
#     password = st.text_input("Password", type="password")

#     if admin_name == "admin" and password == "Nfsu7009!":
#         st.success("✅ Admin authenticated!")

#         uploaded_file = st.file_uploader("📷 Scan QR Code to Redeem", type=["png", "jpg", "jpeg"])
#         tokens_to_redeem = st.number_input("Tokens to Redeem", min_value=1, step=1)

#         if uploaded_file and st.button("Redeem Token"):
#             try:
#                 img = Image.open(uploaded_file)
#                 decoded_text = img  # QR Code decoding logic needed
                
#                 phone_number = decoded_text.split(", Phone: ")[1].split(",")[0]
#                 res = requests.post(f"{SERVER_URL}/admin/redeem", json={"phone": phone_number, "tokens": tokens_to_redeem})
#                 if res.status_code == 200:
#                     st.success(res.json()["message"])
#                 else:
#                     st.error(res.json()["error"])
#             except Exception as e:
#                 st.error("Failed to decode QR code. Please try again.")
#     else:
#         st.warning("Invalid credentials")


#4 ---------------------------------------------------- ------------------------------


import os
import streamlit as st
import requests
import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import io

SERVER_URL = "http://localhost:5000"

st.title("🍽️ Food Token System")

# Sidebar Menu
menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Admin"])

# Auto logout if menu is changed
if "user" in st.session_state:
    del st.session_state["user"]
    st.rerun()

# QR Code Generator
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes

# Register Page
if menu == "Register":
    st.header("📝 User Registration")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    tokens = st.number_input("Tokens", min_value=1, step=1)

    if st.button("Register"):
        res = requests.post(f"{SERVER_URL}/register", json={"name": name, "email": email, "phone": phone, "tokens": tokens})
        if res.status_code == 200:
            st.success("✅ Registered successfully! Redirecting to dashboard...")
            st.session_state["user"] = res.json()
            st.rerun()
        else:
            st.error(res.json()["error"])

# Login Page
elif menu == "Login":
    st.header("🔑 User Login")
    phone = st.text_input("Phone")

    if st.button("Login"):
        res = requests.post(f"{SERVER_URL}/login", json={"phone": phone})
        if res.status_code == 200:
            st.success(f"✅ Welcome! Redirecting to dashboard...")
            st.session_state["user"] = res.json()
            st.rerun()
        else:
            st.error(res.json()["error"])

# User Dashboard
if "user" in st.session_state:
    user = st.session_state["user"]

    if st.button("🔙 Back"):
        del st.session_state["user"]
        st.rerun()

    st.header(f"👤 {user['name']}'s Dashboard")
    st.write(f"📞 Phone: {user['phone']}")
    st.write(f"📧 Email: {user['email']}")
    st.write(f"🔢 Tokens Left: {user['tokens']}")

    qr_code_bytes = generate_qr_code(f"User: {user['name']}, Phone: {user['phone']}, Tokens: {user['tokens']}")
    st.image(qr_code_bytes, caption="Your QR Code", use_container_width=True)

    if st.button("🚪 Logout"):
        del st.session_state["user"]
        st.rerun()

# Admin Panel
elif menu == "Admin":
    st.header("🛠️ Admin Panel")
    admin_name = st.text_input("Admin Name")
    password = st.text_input("Password", type="password")

    if admin_name == "admin" and password == "Nfsu7009!":
        st.success("✅ Admin authenticated!")

        st.write("📷 **Scan QR Code using your camera**")
        cam = cv2.VideoCapture(0)

        if st.button("Start Scanning"):
            while True:
                success, frame = cam.read()
                if not success:
                    st.error("Failed to access camera.")
                    break
                
                for barcode in decode(frame):
                    qr_data = barcode.data.decode("utf-8")
                    cam.release()
                    cv2.destroyAllWindows()
                    
                    phone_number = qr_data.split(", Phone: ")[1].split(",")[0]
                    res = requests.post(f"{SERVER_URL}/admin/redeem", json={"phone": phone_number, "tokens": 1})
                    
                    if res.status_code == 200:
                        st.success(res.json()["message"])
                    else:
                        st.error(res.json()["error"])
                    break
    else:
        st.warning("Invalid credentials")
