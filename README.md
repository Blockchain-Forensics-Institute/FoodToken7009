🍽️ Food Token System

Overview

The Food Token System is a blockchain-based application that allows users to register, generate QR codes for food tokens, and redeem them via an admin panel. The system includes a smart contract (ERC-20) to handle token transactions and a web interface for user interactions.

Features

User Registration: Users can register with their name, email, and phone number and receive food tokens.

Login & Dashboard: Users can log in to view their token balance and generate a QR code.

QR Code Generation: A QR code is created for each registered user containing their details.

Admin Panel: Admins can scan QR codes to redeem tokens for food distribution.

Blockchain-based Token System: Smart contract implementation using ERC-20 for managing food tokens.

Tech Stack

Frontend: Streamlit (Python)

Backend: Node.js with Express.js

Blockchain: Solidity (ERC-20 token contract)

Database: JSON file-based storage

QR Code Handling: qrcode library & OpenCV

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-repo/food-token-system.git
cd food-token-system

2. Install Dependencies

Backend (Node.js)

cd backend
npm install

Frontend (Python Streamlit App)

cd token-system
pip install -r requirements.txt

3. Run the Application

Start Backend Server

cd server
node index.js

Start Frontend Streamlit App

cd webapp
streamlit run app.py

Smart Contract Deployment

Use Remix IDE to deploy token.sol.

Ensure you have a wallet connected (e.g., MetaMask).

Deploy the contract and interact with it to issue tokens.

How It Works

User Registration: Users enter their details and receive a QR code with token balance.

Login & QR Display: Users log in and see their QR code representing their tokens.

Admin Token Redemption: The admin scans QR codes and deducts tokens accordingly.

Blockchain Transaction: Token transactions occur via the deployed smart contract.

Future Enhancements

Integration with a real database (PostgreSQL or MongoDB)

Improved authentication (OAuth, JWT)

Mobile app integration

Real blockchain deployment instead of a local setup

License

This project is licensed under the MIT License.
