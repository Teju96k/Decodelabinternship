# Decodelabinternship
# Cyber Security Projects — DecodeLabs

A collection of four beginner-level **Cyber Security projects** developed as part of the DecodeLabs Industrial Training Program.

These projects demonstrate practical implementation of basic cybersecurity concepts including password security, encryption and decryption, phishing detection, and system security assessment.

---

## 📌 Projects Included

| Project   | Title                          | Main Concept        |
| --------- | ------------------------------ | ------------------- |
| Project 1 | Password Strength Checker      | Password Security   |
| Project 2 | Basic Encryption & Decryption  | Cryptography        |
| Project 3 | Phishing Awareness Analysis    | Threat Detection    |
| Project 4 | System Vulnerability Checklist | Security Assessment |

---

# 🔐 Project 1 — Password Strength Checker

## Project Title

**Password Strength Checker**

## Description

The Password Strength Checker is a Python-based cybersecurity tool that evaluates the strength of a password.

The program checks:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Based on these checks, the password is classified as:

* **Weak**
* **Medium**
* **Strong**

The project demonstrates basic security logic, string handling, pattern matching, and conditional statements.

## File

```text
password_strength_checker.py
```

## How to Run

Open a terminal inside the Project 1 folder and run:

```bash
python password_strength_checker.py
```

If your system uses `python3`:

```bash
python3 password_strength_checker.py
```

## Example

```text
==================================================
        PASSWORD STRENGTH CHECKER
==================================================

Enter your password: Cyber@12345

--------------------------------------------------
PASSWORD ANALYSIS
--------------------------------------------------
Length              : 11
Uppercase Letter    : Yes
Lowercase Letter    : Yes
Number              : Yes
Special Character   : Yes

Score               : 5/5
Password Strength   : STRONG
```

---

# 🔒 Project 2 — Basic Encryption & Decryption

## Project Title

**Basic Encryption & Decryption**

## Description

This project implements a simple **Caesar Cipher** encryption and decryption technique.

The user enters:

1. A message
2. A shift key

The program then:

* Encrypts the message
* Displays the encrypted text
* Decrypts the encrypted text
* Displays the original message again
* Verifies that decryption was successful

This project demonstrates basic encryption concepts, logical programming, and data confidentiality.

## File

```text
caesar_cipher.py
```

## How to Run

```bash
python caesar_cipher.py
```

Or:

```bash
python3 caesar_cipher.py
```

## Example

```text
=======================================================
          BASIC ENCRYPTION & DECRYPTION
                CAESAR CIPHER
=======================================================

Enter the text: Hello World
Enter shift key (1-25): 3

-------------------------------------------------------
RESULT
-------------------------------------------------------
Original Text  : Hello World
Shift Key      : 3
Encrypted Text : Khoor Zruog
Decrypted Text : Hello World
-------------------------------------------------------
Verification    : SUCCESS
The encrypted text was successfully decrypted.
=======================================================
```

## Note

Caesar Cipher is a basic educational encryption technique. It should **not** be used for protecting real confidential information.

---

# 🎣 Project 3 — Phishing Awareness Analysis

## Project Title

**Phishing Awareness Analysis**

## Description

The Phishing Awareness Analyzer is a Python-based cybersecurity tool that analyzes sample emails or messages to identify possible phishing indicators.

The program checks for:

* Suspicious keywords
* Urgent language
* Requests for passwords or OTPs
* Generic greetings
* Suspicious URLs
* URLs without HTTPS
* IP addresses used instead of domain names
* Suspicious words in domains
* Unusually long URLs

The program generates a risk assessment and displays the red flags detected.

Possible results include:

```text
HIGH RISK - LIKELY PHISHING
MEDIUM RISK - SUSPICIOUS
LOW/MEDIUM RISK - VERIFY MESSAGE
LOW RISK - NO OBVIOUS RED FLAGS
```

## File

```text
phishing_analyzer.py
```

## How to Run

```bash
python phishing_analyzer.py
```

Or:

```bash
python3 phishing_analyzer.py
```

## Example

Input:

```text
Dear customer,

Your account has been suspended.
Verify your password immediately.

http://example.com/login
```

Possible output:

```text
=================================================================
                 ANALYSIS RESULT
=================================================================

Risk Assessment:
HIGH RISK - LIKELY PHISHING

Links Detected:
 - http://example.com/login

Red Flags:
 1. Suspicious keywords detected
 2. Message creates a sense of urgency
 3. Message may request sensitive information
 4. Website does not use HTTPS
 5. Domain contains suspicious word: 'login'
```

## Security Recommendation

Users should verify unexpected messages through an official communication channel before clicking links or providing sensitive information.

---

# 🛡️ Project 4 — System Vulnerability Checklist

## Project Title

**System Vulnerability Checklist**

## Description

The System Vulnerability Checklist is a defensive cybersecurity tool designed to identify basic security weaknesses.

The program performs checks related to:

* Password security
* Password length
* Uppercase and lowercase characters
* Numbers
* Special characters
* Operating system/update guidance
* Basic security/development tools
* Multi-Factor Authentication
* Software updates
* Data backups
* Suspicious links and attachments
* Trusted software sources
* Computer screen locking

The program generates an overall security score and assigns a basic risk level.

## File

```text
system_vulnerability_checker.py
```

## How to Run

```bash
python system_vulnerability_checker.py
```

Or:

```bash
python3 system_vulnerability_checker.py
```

## Example

```text
============================================================
          SYSTEM VULNERABILITY CHECKLIST
============================================================

Purpose: Identify basic security vulnerabilities
through defensive checks.

============================================================
1. PASSWORD SECURITY CHECK
============================================================

Enter a test password:

Password Analysis:
[PASS] Minimum length (8 characters)
[PASS] Contains uppercase letter
[PASS] Contains lowercase letter
[PASS] Contains number
[PASS] Contains special character

Password Security Score: 5/5
```

The program then checks the operating system, basic tools, and user security practices before producing a final assessment.

## Risk Levels

```text
80% or above  → LOW
60% - 79%     → MEDIUM
Below 60%     → HIGH
```

## Important Note

This project is a **basic defensive security checklist**. It does not exploit vulnerabilities, attack systems, or automatically modify system settings.

---

# ⚙️ Requirements

All four projects are written in **Python**.

Recommended Python version:

```text
Python 3.10+
```

No external Python packages are required for these implementations.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# 🚀 Quick Start

Clone or download the project repository.

Navigate to the required project folder.

For example:

```bash
cd Project-1-Password-Strength-Checker
```

Run:

```bash
python password_strength_checker.py
```

For Project 2:

```bash
cd Project-2-Basic-Encryption-Decryption
python caesar_cipher.py
```

For Project 3:

```bash
cd Project-3-Phishing-Awareness-Analysis
python phishing_analyzer.py
```

For Project 4:

```bash
cd Project-4-System-Vulnerability-Checklist
python system_vulnerability_checker.py
```

---

# 🧠 Skills Demonstrated

These projects demonstrate practical knowledge of:

* Python Programming
* String Manipulation
* Conditional Statements
* Regular Expressions
* Functions
* Object-Oriented Programming
* Basic Cryptography
* Encryption and Decryption
* Password Security
* Phishing Detection
* URL Analysis
* Threat Identification
* Security Awareness
* Vulnerability Assessment
* Defensive Security
* Risk Classification
* Command-Line Application Development

---

# 🎯 Learning Objectives

Through these projects, the following cybersecurity concepts are practiced:

### Project 1

Understanding password security and basic password-strength requirements.

### Project 2

Understanding the fundamental concept of reversible encryption and decryption.

### Project 3

Learning how phishing messages can be analyzed for suspicious indicators and malicious intent.

### Project 4

Learning how basic security weaknesses can be identified using a defensive checklist.

---

# ⚠️ Disclaimer

These projects are developed for **educational and cybersecurity training purposes**.

The tools are intended to be used only on systems, messages, and data for which you have permission to perform analysis.

They are not replacements for professional cybersecurity tools, enterprise security systems, or security audits.

---

# 👩‍💻 Author

**Cyber Security Student**

**DecodeLabs Industrial Training — 2026**

---

## ⭐ Portfolio Note

These projects demonstrate practical application of cybersecurity concepts rather than only theoretical knowledge.

They can be included in a GitHub portfolio to demonstrate:

> **Security Awareness → Programming → Threat Analysis → Defensive Security**
