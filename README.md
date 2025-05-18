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

1. Ensure required dependencies are installed
2. Run the script via terminal:

```bash
python3 tokens_scanner.py
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
pip install requests colorama
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

---

## 📄 Output Files

| File Name              | Description                             |
|------------------------|-----------------------------------------|
| `eth_new_contracts.txt`| List of new Ethereum token contracts    |
| `pol_new_contracts.txt`| List of new Polygon token contracts     |

---

## 📃 License

MIT License — see [LICENSE](LICENSE)

---

## ⚠️ Disclaimer

This software is intended for **educational and informational purposes only**.

- Many newly deployed tokens may be **scams**, **honeypots**, or contain **malicious logic**
- Always perform your own research before making any financial decisions
- The author **assumes no responsibility** for any loss, misuse, or outcomes arising from use of this software
- **Do not share your API key** — it can be abused or exploited

By using this software, you agree to all terms and accept full responsibility for your actions.

---

## 💸 Donations

If you find this tool helpful and would like to support further development:

- **Bitcoin (BTC):**  
  `1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

- **Monero (XMR):**  
  `86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

- **Dash (DASH):**  
  `XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

- **Bytecoin (BCN):**  
  `bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 Thank you for supporting independent developers and ethical technology.

> *"I morph bits not to break, but to understand."*  
> — **BitMorphX**
