// const express = require("express");
// const fs = require("fs");
// const cors = require("cors");
// const bodyParser = require("body-parser");
// const qrcode = require("qrcode");
// const QRCodeReader = require("qrcode-reader");
// const Jimp = require("jimp");

// const QR_DIR = `${__dirname}/qr_codes`;

// // Ensure the QR codes directory exists
// if (!fs.existsSync(QR_DIR)) {
//     fs.mkdirSync(QR_DIR, { recursive: true });
// }

// const app = express();
// app.use(cors());
// app.use(bodyParser.json());

// const DB_FILE = "./database.json";

// if (!fs.existsSync(DB_FILE)) fs.writeFileSync(DB_FILE, JSON.stringify({ users: [] }, null, 2));

// const getUsers = () => JSON.parse(fs.readFileSync(DB_FILE)).users;
// const saveUsers = (users) => fs.writeFileSync(DB_FILE, JSON.stringify({ users }, null, 2));

// // User Registration
// app.post("/register", async (req, res) => {
//     console.log("Received Data:", req.body);
//     const { name, email, phone, tokens } = req.body;
//     let users = getUsers();
//     if (users.some((u) => u.phone === phone)) return res.status(400).json({ error: "Phone already registered" });

//     const qrData = JSON.stringify({ name, phone, tokens });
//     const qrCodePath = `${QR_DIR}/${phone}.png`;

//     try {
//         await qrcode.toFile(qrCodePath, qrData);
//     } catch (error) {
//         console.error("QR Code Generation Failed:", error);
//         return res.status(500).json({ error: "QR Code generation failed" });
//     }

//     users.push({ name, email, phone, tokens, qrCodePath });
//     saveUsers(users);

//     res.json({ message: "User registered", user: { name, email, phone, tokens, qrCode: qrCodePath } });
// });

// // User Login
// app.post("/login", (req, res) => {
//     const { phone } = req.body;
//     let users = getUsers();
//     let user = users.find((u) => u.phone === phone);
//     if (!user) return res.status(404).json({ error: "User not found" });

//     res.json({ name: user.name, email: user.email, phone: user.phone, tokens: user.tokens, qrCode: user.qrCodePath });
// });

// // Admin Redeem Tokens via QR Code
// app.post("/admin/redeem", async (req, res) => {
//     const { qrCodePath, tokensToRedeem } = req.body;

//     try {
//         const image = await Jimp.read(qrCodePath);
//         const qr = new QRCodeReader();
//         const value = await new Promise((resolve, reject) => {
//             qr.callback = (err, decoded) => (err ? reject(err) : resolve(decoded.result));
//             qr.decode(image.bitmap);
//         });

//         const qrData = JSON.parse(value);
//         let users = getUsers();
//         let user = users.find((u) => u.phone === qrData.phone);

//         if (!user) return res.status(400).json({ error: "User not found" });

//         if (user.tokens < tokensToRedeem) return res.status(400).json({ error: "Not enough tokens" });

//         user.tokens -= tokensToRedeem;
//         saveUsers(users);

//         res.json({ message: `Redeemed ${tokensToRedeem} tokens`, remainingTokens: user.tokens });
//     } catch (error) {
//         console.error("QR Code Scan Failed:", error);
//         return res.status(500).json({ error: "QR code scanning failed" });
//     }
// });

// app.listen(5000, () => console.log("✅ Server running on port 5000"));


//2 ---------------------------------------------------- ------------------------------

// const express = require("express");
// const fs = require("fs");
// const cors = require("cors");
// const bodyParser = require("body-parser");
// const qrcode = require("qrcode");
// const Jimp = require("jimp");
// const QRCodeReader = require("qrcode-reader");

// const QR_DIR = "./qr_codes";
// const DB_FILE = "./database.json";

// if (!fs.existsSync(QR_DIR)) fs.mkdirSync(QR_DIR, { recursive: true });
// if (!fs.existsSync(DB_FILE)) fs.writeFileSync(DB_FILE, JSON.stringify({ users: [] }, null, 2));

// const getUsers = () => JSON.parse(fs.readFileSync(DB_FILE)).users;
// const saveUsers = (users) => fs.writeFileSync(DB_FILE, JSON.stringify({ users }, null, 2));

// const app = express();
// app.use(cors());
// app.use(bodyParser.json());

// // Register User
// app.post("/register", async (req, res) => {
//     const { name, email, phone, tokens } = req.body;
//     let users = getUsers();
//     if (users.some((u) => u.phone === phone)) return res.status(400).json({ error: "Phone already registered" });

//     const qrData = JSON.stringify({ name, phone, tokens });
//     const qrCodePath = `${QR_DIR}/${phone}.png`;
    
//     try {
//         await qrcode.toFile(qrCodePath, qrData);
//         users.push({ name, email, phone, tokens, qrCodePath });
//         saveUsers(users);
//         res.json({ name, email, phone, tokens, qrCode: qrCodePath });
//     } catch (error) {
//         res.status(500).json({ error: "QR Code generation failed" });
//     }
// });

// // Login User
// app.post("/login", (req, res) => {
//     const { phone } = req.body;
//     let users = getUsers();
//     let user = users.find((u) => u.phone === phone);
//     if (!user) return res.status(404).json({ error: "User not found" });
//     res.json(user);
// });

// // Admin Redeem Tokens
// app.post("/admin/redeem", async (req, res) => {
//     const { qrCodePath, tokensToRedeem } = req.body;
//     try {
//         const image = await Jimp.read(qrCodePath);
//         const qr = new QRCodeReader();
//         const value = await new Promise((resolve, reject) => {
//             qr.callback = (err, decoded) => (err ? reject(err) : resolve(decoded.result));
//             qr.decode(image.bitmap);
//         });

//         const qrData = JSON.parse(value);
//         let users = getUsers();
//         let user = users.find((u) => u.phone === qrData.phone);

//         if (!user || user.tokens < tokensToRedeem) return res.status(400).json({ error: "Invalid transaction" });
        
//         user.tokens -= tokensToRedeem;
//         saveUsers(users);
//         res.json({ message: `Redeemed ${tokensToRedeem} tokens`, remainingTokens: user.tokens });
//     } catch (error) {
//         res.status(500).json({ error: "QR code scanning failed" });
//     }
// });

// app.listen(5000, () => console.log("✅ Server running on port 5000"));

//3 ---------------------------------------------------- ------------------------------

// const express = require("express");
// const fs = require("fs");
// const cors = require("cors");
// const bodyParser = require("body-parser");
// const qrcode = require("qrcode");
// const Jimp = require("jimp");
// const QRCodeReader = require("qrcode-reader");

// const QR_DIR = `${__dirname}/qr_codes`;

// // Ensure the QR codes directory exists
// if (!fs.existsSync(QR_DIR)) {
//     fs.mkdirSync(QR_DIR, { recursive: true });
// }

// const app = express();
// app.use(cors());
// app.use(bodyParser.json());

// const DB_FILE = "./database.json";

// if (!fs.existsSync(DB_FILE)) fs.writeFileSync(DB_FILE, JSON.stringify({ users: [] }, null, 2));

// const getUsers = () => JSON.parse(fs.readFileSync(DB_FILE)).users;
// const saveUsers = (users) => fs.writeFileSync(DB_FILE, JSON.stringify({ users }, null, 2));

// // User Registration
// app.post("/register", async (req, res) => {
//     console.log("Received Data:", req.body);
//     const { name, email, phone, tokens } = req.body;
//     let users = getUsers();
//     if (users.some((u) => u.phone === phone)) return res.status(400).json({ error: "Phone already registered" });

//     const qrData = JSON.stringify({ name, phone, tokens });
//     const qrCodePath = `${QR_DIR}/${phone}.png`;

//     try {
//         await qrcode.toFile(qrCodePath, qrData);
//     } catch (error) {
//         console.error("QR Code Generation Failed:", error);
//         return res.status(500).json({ error: "QR Code generation failed" });
//     }

//     users.push({ name, email, phone, tokens, qrCodePath });
//     saveUsers(users);

//     res.json({ name, email, phone, tokens, qrCodePath });
// });

// // User Login
// app.post("/login", (req, res) => {
//     const { phone } = req.body;
//     let users = getUsers();
//     let user = users.find((u) => u.phone === phone);
//     if (!user) return res.status(404).json({ error: "User not found" });

//     res.json({ name: user.name, email: user.email, phone: user.phone, tokens: user.tokens, qrCodePath: user.qrCodePath });
// });

// // Admin Redeem Tokens via QR Code
// app.post("/admin/redeem", async (req, res) => {
//     const { phone, tokens } = req.body;
//     let users = getUsers();
//     let user = users.find((u) => u.phone === phone);

//     if (!user) return res.status(400).json({ error: "User not found" });

//     if (user.tokens < tokens) return res.status(400).json({ error: "Not enough tokens" });

//     user.tokens -= tokens;
//     saveUsers(users);

//     res.json({ message: `Redeemed ${tokens} tokens`, remainingTokens: user.tokens });
// });

// app.listen(5000, () => console.log("✅ Server running on port 5000"));



//3 ---------------------------------------------------- ------------------------------

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

// User Registration
app.post("/register", async (req, res) => {
    console.log("Received Data:", req.body);
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

    res.json({ name, email, phone, tokens, qrCodePath });
});

// User Login
app.post("/login", (req, res) => {
    const { phone } = req.body;
    let users = getUsers();
    let user = users.find((u) => u.phone === phone);
    if (!user) return res.status(404).json({ error: "User not found" });

    res.json({ name: user.name, email: user.email, phone: user.phone, tokens: user.tokens, qrCodePath: user.qrCodePath });
});

// Admin Redeem Tokens via QR Code
app.post("/admin/redeem", (req, res) => {
    const { phone, tokens } = req.body;
    let users = getUsers();
    let user = users.find((u) => u.phone === phone);

    if (!user) return res.status(400).json({ error: "User not found" });

    if (user.tokens < tokens) return res.status(400).json({ error: "Not enough tokens" });

    user.tokens -= tokens;
    saveUsers(users);

    res.json({ message: `Redeemed ${tokens} tokens`, remainingTokens: user.tokens });
});

app.listen(5000, () => console.log("✅ Server running on port 5000"));
