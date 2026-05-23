# ISEA Finals Data Dashboard

Comparative Analysis of Major Philippine Companies built with **Streamlit**.

**Author**: Gian Roilo P. Salen  
**Project**: ISEA Finals 2026

---

## 📁 Project Structure

```
ISEA_finals/
├── Home.py                         # Main dashboard entry point (Home page)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                         # App pages (auto-discovered by Streamlit)
│   ├── 02_Visualizations.py       # Data visualization creation page
│   └── 03_Dataset_Explorer.py     # Dataset browsing and exploration
│
├── assets/                         # Images, logos, custom CSS
│   └──
│
├── data/                           # Dataset storage
│   └── merged_cleaned_stocks.csv   # Merged and cleaned 5 CSV files of the 5 companies
│
└── utils/                          # Utility functions and helpers
    └──
```

---

## 🚀 Quick Start

### 1. **Clone or Download the Project**
```bash
cd ISEA_finals
```

### 2. **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Run the Dashboard**
```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

---

## 📦 Dependencies

- **streamlit**: Web app framework for data apps
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive visualizations

Install all at once:
```bash
pip install -r requirements.txt
```

---


