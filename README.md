<p align="center">
  <img src="assets/banner.png" alt="tokens_scanner banner" width="100%" />
</p>

# 🛰️ Token Contract Scanner (`tokens_scanner.py`)

This script continuously scans and logs **newly created cryptocurrency token contracts** on the **Ethereum** and **Polygon** networks. It is designed for blockchain analysts, developers, and educators who want to monitor market activity and discover newly deployed tokens in real-time.

---

## 🛠️ Features

- Real-time contract discovery via **Mobula API**
- Tracks newly listed tokens on Ethereum and Polygon
- Displays token data in a clean, colorized terminal format
- Automatically logs contracts into separate text files:
  - `eth_new_contracts.txt`
  - `pol_new_contracts.txt`
- Auto-refreshes every 0.5 to 3 seconds
- Displays tokens in batches of 18 with scrolling updates

---

## ⚙️ How to Use

### 1. 🔐 Obtain a Mobula API Key

To use this scanner, you need a Mobula API key:

1. Visit the official documentation:  
   [https://docs.mobula.io/introduction](https://docs.mobula.io/introduction)
2. Sign in or register an account
3. Generate your personal API key
4. Open the script `tokens_scanner.py` and replace this line:

   ```python
   API_KEY = "your_api_key"
   ```

   with your actual key:

   ```python
   API_KEY = "YOUR_REAL_API_KEY"
   ```

🚫 **Never share your API key with others — it is your personal access token!**

---

## 📂 Running the Program

### Option 1 – via Python:

```bash
python tokens_scanner.py
```

### Option 2 – via `.bat` launcher (Windows):

```cmd
tokens_scanner.bat
```

The scanner will automatically:
- Connect to Mobula API
- Fetch new tokens
- Display results in your terminal
- Save contracts to:
  - `eth_new_contracts.txt`
  - `pol_new_contracts.txt`

---

## 🧪 Requirements

Install the required Python packages:

```bash
pip install requests
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

> Python 3.6+ is required.

---

## 📄 Output Files

| File Name              | Description                             |
|------------------------|-----------------------------------------|
| `eth_new_contracts.txt`| List of new Ethereum token contracts    |
| `pol_new_contracts.txt`| List of new Polygon token contracts     |

---

## 📁 Project Structure

```text
tokens_scanner/
├── assets/
│   └── banner.png
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── .github/
│   └── FUNDING.yml
├── tokens_scanner.py
├── tokens_scanner.bat
├── LICENSE
├── NOTICE
├── ETHICS.md
├── README.md
├── requirements.txt
├── RELEASE_v1.0.0.md
└── RELEASE_v2.0.0.md
```

---

### 🔁 GitHub Contribution Streak

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=BitMorphX&theme=tokyonight"/>
</p>


---

## ⚠️ DISCLAIMER

This software is intended **strictly for educational and research purposes**.

- All provided data is for informational use only and **not financial advice**  
- The creator **bears no responsibility** for losses or damages resulting from usage  
- Use it at **your own risk** and always verify independently

> **Use responsibly. Learn ethically. Contribute honestly.**

---

## ⚖️ Ethical Use

This tool is created strictly for **research and educational purposes**.  
See [ETHICS](./ETHICS.md) for the full statement.

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE)

---

## 📣 NOTICE

See [`NOTICE`](./NOTICE) for important information about attribution, DMCA protection, and reuse permissions.

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
