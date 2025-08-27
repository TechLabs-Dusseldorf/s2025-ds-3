# Group 3 — Summer 2025 Microplastics Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-0099CC?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

## 📌 Project Overview
This project is part of the **PurePlate Initiative**, a global non-profit focused on promoting food safety and raising awareness about emerging contaminants in our diet.  
We investigate the **growing presence of microplastics in the food supply** and explore potential long-term health impacts.

Our analysis aims to:
- 📊 Identify trends in microplastic intake  
- 🥗 Pinpoint high-risk food categories  
- 🌍 Understand geographical variations in exposure  

Findings will support **public health campaigns**, inform **dietary guidelines**, and advocate for **stronger plastic regulations**.

---

## 🛠 Installation & Setup

### **System Requirements**
- Python 3.8+
- Git
- pip 
- *(Optional)* Virtual environment manager (`venv`, `virtualenv`, or `conda`)  

### **1. Clone the Repository**
```bash
git clone git@github.com:TechLabs-Dusseldorf/s2025-ds-3.git
cd s2025-ds-3
```

### **2. Create a virtual environment (optional but recommended)**

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### **3. Install dependencies**

1. Ensure you're in the project root directory.  
2. Install required packages using:

```bash
pip install -r requirements.txt
```

### 4. Running the Python Scripts

1. Run the Python scripts using:

Run calculations:

```bash
python main.py ./processed_microplastics.csv
```

Run the Streamlit Web App from the project root directory:

```bash
streamlit run 🌐_Home.py
```

---

## Authors

- [Humam](https://github.com/Humam-Hamdan)
- [Negin](https://github.com/NeginDs)
- [Nicole](https://github.com/Nicolem99)
- [Gaetano](https://github.com/Bionema)

