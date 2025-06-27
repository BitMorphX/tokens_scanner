# 📦 Release Notes — Token Contract Scanner `v1.0.0`

**Release Date:** 2025-05-18  
**Version:** 1.0.0  
**Script Name:** `tokens_scanner.py`

---

## 🚀 Overview

This is the initial stable release of `tokens_scanner.py`, a command-line Python tool designed to monitor **newly created token contracts** on the **Ethereum** and **Polygon** blockchains using the Mobula API.

This version is optimized for live scanning and continuous updates.

---

## 🧩 Core Features

- ✅ Tracks new token contracts via Mobula API  
- ✅ Monitors both Ethereum and Polygon networks  
- ✅ Updates data every 0.5–3 seconds (randomized interval)  
- ✅ Displays real-time data in the terminal with clear formatting  
- ✅ Automatically saves results into text files  
  - `eth_new_contracts.txt`  
  - `pol_new_contracts.txt`  
- ✅ Supports terminal output in English (UTF-8, color-coded)  
- ✅ Includes strict warning/disclaimer system for users

---

## 📄 File Output

Upon running, the program creates or appends to the following output files:

- `eth_new_contracts.txt` — All newly discovered Ethereum token contracts  
- `pol_new_contracts.txt` — All newly discovered Polygon token contracts

These files include timestamps, token names, addresses, and blockchain source.

---

## 🔐 API Integration

This version uses the official **Mobula API**. Users must acquire their own API key and configure it in the script:

```python
API_KEY = "your_api_key_here"
```

Mobula documentation: [https://docs.mobula.io/introduction](https://docs.mobula.io/introduction)

---

## 📃 License

**MIT License**  
> _(Replaced with Apache 2.0 in v2.0.0 — see [LICENSE](./LICENSE))_

---

## ⚠️ Disclaimer

This tool is provided **as-is for educational purposes only**. Many listed tokens may be malicious, fake, or spam.

- Use at your own risk  
- Perform your own research before making any investment  
- Do not share your API key with others  
- The author assumes **no responsibility** for loss or misuse

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
