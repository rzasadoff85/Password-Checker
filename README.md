
# Password Leak Checker 🔐

A simple and secure cybersecurity tool written in Python that checks if a password has been compromised in known data breaches. 

This tool uses the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3) to securely verify passwords without exposing your actual password to the internet.

## 🛡️ How is it secure? (k-Anonymity)
For security reasons, this tool **never** sends your actual password over the internet. Instead, it:
1. Hashes your password using the SHA-1 algorithm.
2. Sends only the **first 5 characters** of the hash to the API.
3. The API returns a list of all leaked hashes starting with those 5 characters.
4. The script checks locally if the rest of your hash matches any of the results.

## 🚀 Features
- Fast and lightweight.
- Secure password checking using k-Anonymity.
- Easy to use via the command line.

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/rzasadoff85] 
