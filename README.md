# 🌐 **Phishing Link Detector**
*A machine‑learning powered tool for detecting phishing URLs with both CLI and UI options.*

---

## 🔎 **Overview**
The **Phishing Link Detector** analyzes URLs and determines whether they are **legitimate**, **suspicious**, or **malicious**. It uses:

- URL feature extraction  
- A trained **Random Forest** machine learning model  
- Heuristic rules  
- A user‑friendly optional **graphical interface (UI)**  

Phishing attacks are one of the most common cybersecurity threats. This tool helps users, students, and developers quickly evaluate URLs and understand why they may be dangerous.

---

## 🚀 **Features**
- ✔️ Extracts over a dozen URL‑based features  
- ✔️ Detects suspicious patterns (IP addresses, long URLs, deceptive keywords, etc.)  
- ✔️ Machine learning classification using Random Forest  
- ✔️ Confidence score for each prediction  
- ✔️ **Two ways to use the tool:**  
  - Command‑line mode  
  - Graphical UI mode (Tkinter)  
- ✔️ Easy installation with `requirements.txt`

---

## 📁 **Project Structure**
```
/models
    best_model.joblib
/scripts
    train_model.py
    classify_url.py
phishing_features.py
ui.py
requirements.txt
README.md
```
## 🛠️ Prerequisites

Before installing or running this project, make sure you have the following installed on your machine:

### ✔️ Python 3.10+
Download from: https://www.python.org/downloads/

You can verify your version with:
```
python --version
```

### ✔️ Git (required to clone the repository)
Download Git here:  
https://git-scm.com/downloads

During installation, make sure to select:
- **“Add Git to PATH”**  
- **Use bundled OpenSSL library** (recommended)

You can verify Git is installed with:
```
git --version
```

---

# 🛠️ **Installation Guide 

### **1️⃣ Install Python**
Make sure you have **Python 3.10+** installed.

Check your version:
```
python --version
```

---

### **2️⃣ Clone the Repository**
```
git clone https://github.com/MartinV4520/CIS-260-Project
```

---

### **3️⃣ Create a Virtual Environment (Recommended)**
```
python -m venv venv
```

Activate it:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

---

### **4️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

---

### **5️⃣ Train the Model (Required Before Use)**
This generates `best_model.joblib` inside the `models/` folder.

```
python train_model.py
```

---

# 🧭 **How to Use the Tool**

You now have **two options**:

---

# 🖥️ **Option 1 — Use the Graphical UI (For Beginners)**

### **Run the UI**
```
python ui.py
```

### **What the UI Does**
- Opens a window  
- Lets you type or paste a URL  
- Runs the trained model  
- Shows:
  - ✔️ Prediction (Phishing or Legitimate)  
  - ✔️ Confidence score  
  - ✔️ Model used  

### **Perfect for:**
- Non‑technical users  
- Demonstrations  
- Class presentations  

---

# 💻 **Option 2 — Use the Command Line (For Advanced Users)**

### **Run the Classifier**
```
python classify_url.py
```

If your script asks for input, enter a URL when prompted.

### **What You Get**
- Raw prediction (0 = legitimate, 1 = phishing)  
- Confidence score  
- Model name  

### **Perfect for:**
- Developers  
- Automation  
- Integrating into other tools  

---

# 📊 **How It Works**

The detector analyzes URLs by extracting features such as:

- URL length  
- Number of dots  
- Presence of IP addresses  
- Suspicious keywords  
- Subdomain depth  
- Special characters  
- Domain structure  

These features are fed into a **Random Forest classifier**, which outputs:

- **Prediction** (phishing or legitimate)  
- **Confidence score**  
- **Model type**  

---

# 🧪 **Training the Model**
The training script:

- Loads the dataset  
- Extracts features  
- Splits into train/test  
- Trains a Random Forest  
- Evaluates accuracy, precision, recall, and F1  
- Saves the best model to `/models/best_model.joblib`

Run it anytime you want to retrain the model:
```
python train_model.py
```
