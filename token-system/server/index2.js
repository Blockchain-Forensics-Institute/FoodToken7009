const express = require("express");
const fs = require("fs");
const cors = require("cors");
const bodyParser = require("body-parser");
const qrcode = require("qrcode");
const QR_DIR = `${__dirname}/qr_codes`;

// Ensure the QR codes directory exists
if (!fs.existsSync(QR_DIR)) {
    fs.mkdirSync(QR_DIR, { recursive: true });
}


const app = express();
app.use(cors());
app.use(bodyParser.json());

const DB_FILE = "./database.json";

if (!fs.existsSync(DB_FILE)) fs.writeFileSync(DB_FILE, JSON.stringify({ users: [] }, null, 2));

const getUsers = () => JSON.parse(fs.readFileSync(DB_FILE)).users;
const saveUsers = (users) => fs.writeFileSync(DB_FILE, JSON.stringify({ users }, null, 2));

app.post("/register", async (req, res) => {
    console.log("Received Data:", req.body);  // Debugging line
    const { name, email, phone, tokens } = req.body;
    let users = getUsers();
    if (users.some((u) => u.phone === phone)) return res.status(400).json({ error: "Phone already registered" });

    const qrData = `User: ${name}, Phone: ${phone}, Tokens: ${tokens}`;
    const qrCodePath = `${QR_DIR}/${phone}.png`;
    try {
        await qrcode.toFile(qrCodePath, qrData);
    } catch (error) {
        console.error("QR Code Generation Failed:", error);
        return res.status(500).json({ error: "QR Code generation failed" });
    }

    users.push({ name, email, phone, tokens, qrCodePath });
    saveUsers(users);

    res.json({ message: "User registered", qrCode: qrCodePath });
    
});

app.post("/login", (req, res) => {
    const { phone } = req.body;
    let users = getUsers();
    let user = users.find((u) => u.phone === phone);
    if (!user) return res.status(404).json({ error: "User not found" });

    res.json({ name: user.name, tokens: user.tokens, qrCode: user.qrCodePath });
});

app.post("/admin/redeem", (req, res) => {
    const { phone } = req.body;
    let users = getUsers();
    let user = users.find((u) => u.phone === phone);
    if (!user || user.tokens <= 0) return res.status(400).json({ error: "Invalid user or no tokens" });

    user.tokens -= 1;
    saveUsers(users);
    res.json({ message: "Token redeemed", remainingTokens: user.tokens });
});

app.listen(5000, () => console.log("✅ Server running on port 5000"));
// console.log("Saving QR Code at:", qrCodePath);

