content = '''
# CyberSecurity Defense & Blockchain Identity System

![Python Status](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white) 
![App Framework](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit&logoColor=white) 
![Security Standard](https://img.shields.io/badge/Encryption-AES_256_%7C_RSA_2048-green?style=for-the-badge) 

Welcome to the **CyberSecurity Defense Platform**, an enterprise-grade educational toolkit engineered to visualize and implement the foundational principles of Information Security. The platform focuses heavily on the **CIA Triad** (Confidentiality, Integrity, Availability) alongside Non-Repudiation techniques.

In this interactive environment, users can explore the interplay between modern cryptographic standards. User activities are securely documented into an immutable **Blockchain Ledger**, critical data is protected with **AES-GCM** symmetric encryption, and identity verification is enforced by asymmetric **RSA** signatures.

---

## 📑 Table of Contents
- [System Previews](#system-previews)
- [System Architecture & Core Capabilities](#system-architecture--core-capabilities)
- [Getting Started](#getting-started)
- [Technology Stack](#technology-stack)
- [Educational Objectives](#educational-objectives)
- [License & Author](#license--author)

---

## 🎨 System Previews

### 🛡️ Access Control & Identity Management
| **Secure Authentication (SHA-512)** | **RSA Architecture (Non-repudiation)** |
|:---:|:---:|
| <img src="img/new_login_screen.png" width="400" alt="Authentication Interface"> | <img src="img/Digital%20Signature%20(Non-repudiation).png" width="400" alt="RSA Initialization"> |
| *Zero-Knowledge Identity Validation* | *Asymmetric Key Generation* |

### 📝 Digital Signatures & Encryption
| **Signing Validation** | **Symmetric Data Vault (AES-GCM)** |
|:---:|:---:|
| <img src="img/verify_signature.png" width="400" alt="Verify Signature"> | <img src="img/new_aes_encryption.png" width="400" alt="AES Encryption Vault"> |
| *Public Key Signature Verification* | *Encrypted Zero-Knowledge Local Storage* |

### 🔒 Audit & Threat Analysis
| **Immutable Event Ledger** | **Threat Surface Analysis** |
|:---:|:---:|
| <img src="img/new_blockchain_log.png" width="400" alt="Blockchain Ledger"> | <img src="img/new_hacker_attack.png" width="400" alt="Threat Simulation"> |
| *Cryptographically Linked Audit Trails* | *Offensive Dictionary Attack Simulation* |

---

## 🏗️ System Architecture & Core Capabilities

### 1. Identity & Access Management (IAM)
* **Key Stretching & Salting:** User credentials are obfuscated via **SHA-512** and fortified with a randomized cryptographic **Salt**, mathematically rendering Rainbow Table and pre-computation attacks ineffective.
* **Authentication Pipelines:** Secure verification and active session handling using isolated state mechanics.

### 2. Data Confidentiality (Symmetric Cryptography)
* **Algorithm Standard:** Leverages **AES-GCM** (Advanced Encryption Standard with Galois/Counter Mode) for authenticated encryption.
* **Dynamic Key Generation:** Storage keys are extracted on-the-fly from user credentials through **PBKDF2HMAC** (Password-Based Key Derivation Function 2), ensuring keys are never persisted in plain text.
* **Zero-Knowledge Vault:** A compromised database yields zero useful plaintext since the underlying AES keys remain mathematically isolated.

### 3. Data Integrity (Audit Blockchain)
* **Tamper-Evident Ledger:** Every system action (Logins, Intrusions, Signature Generations) forms a distinct block in the private blockchain.
* **Cryptographic Linking:** Blocks inherently trust each other via SHA-256 dependencies. Altering historical data immediately fractures the underlying hash tree, triggering automated corruption alerts.

### 4. Non-Repudiation (Asymmetric Cryptography)
* **Digital Signatures:** Individuals maintain their own **RSA-2048** keypairs to authorize transactions or messages.
* **Distributed Verification:** Data signed by a user's Private Key can be openly authenticated via their Public Key, ensuring indisputable proof of origin.

### 5. Penetration Testing Framework
* **Red Team Dashboard:** An integrated simulation highlighting password weaknesses via localized, concurrent multiprocessing **Dictionary Attacks**.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9 or higher
* Git / Version Control
* Recommended: Virtual Environment (env or conda)

### Local Deployment Instructions

1. **Clone the Repository:**
   `ash
   git clone https://github.com/TuranAsgarov/final_exam_Data_Security.git
   cd final_exam_Data_Security
   `

2. **Install Dependencies:**
   Install required cryptography and UI packages via pip.
   `ash
   pip install -r requirements.txt
   `

3. **Initialize the Attack Dictionary (Optional):**
   Generate the local wordlists required for the threat simulation module.
   `ash
   python src/dict_generator.py
   `

4. **Launch the Dashboard:**
   Deploy the local Streamlit server.
   `ash
   streamlit run app.py
   `

---

## 🛠️ Technology Stack

- **Core Application Logic:** Python 3.9+
- **UI / Frontend Interface:** Streamlit
- **Cryptographic Engine:** cryptography library (PBKDF2, AES-GCM, RSA, SHA-512)
- **Data Engineering:** Pandas DataFrames
- **Concurrency:** multiprocessing for parallel threat simulation execution

---

## 🧠 Educational Objectives

This modular suite is crafted to demystify enterprise Information Security (InfoSec) concepts:
- Mapping the operational flow of **Asymmetric vs Symmetric Encryption Dynamics**.
- Demonstrating **Collision Resistance** in Hash Functions.
- Providing visual validity of the mathematical necessity for **Salting** mechanisms.
- Exploring **Distributed Ledger / Blockchain** architecture and local state constraints.
- Applying **Attack Vector Mapping** alongside real-time mitigation strategies.

---
*Developed by **Turan Asgarov** as part of advanced Information Security research.*
'''
open('README.md', 'w', encoding='utf-8').write(content.strip())
