# 📊 ISEA Finals Dashboard

A professional, responsive data dashboard built with **Streamlit** featuring multi-page navigation, interactive visualizations, and dataset exploration capabilities.

**Author**: Gian Roilo P. Salen  
**Project**: ISEA Finals 2026

---

## 📁 Project Structure

```
ISEA_finals/
├── app.py                          # Main dashboard entry point (Home page)
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                          # Multi-page app pages (auto-discovered by Streamlit)
│   ├── 01_Home.py                 # Home page with overview
│   ├── 02_Visualizations.py       # Data visualization creation page
│   └── 03_Dataset_Explorer.py     # Dataset browsing and exploration
│
├── assets/                         # Images, logos, custom CSS (if needed)
│   └── (Add images here)
│
├── data/                           # Dataset storage
│   └── (Add CSV, Excel, etc. here)
│
└── utils/                          # Utility functions and helpers
    └── (Add helper functions here)
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

### 4. **Add Your Data**
Place your CSV, Excel, or other data files in the `/data/` folder.

### 5. **Run the Dashboard**
```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

---

## 📦 Dependencies

- **streamlit**: Web app framework for data apps
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive visualizations
- **openpyxl**: Excel file support (optional)

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 📄 Pages Overview

### 🏠 Home Page (`01_Home.py`)
- Dashboard overview
- Quick statistics
- Feature highlights
- Quick navigation buttons

### 📊 Visualizations Page (`02_Visualizations.py`)
- Create interactive charts
- Support for multiple chart types:
  - Line charts (trends)
  - Bar charts (comparisons)
  - Scatter plots (correlations)
  - Pie charts (proportions)
  - Heatmaps (patterns)
- Customizable settings
- Chart gallery

### 🔍 Dataset Explorer Page (`03_Dataset_Explorer.py`)
- Browse datasets
- View data statistics
- Filter and search data
- Data quality reports
- Upload new datasets
- Column statistics

---

## 🎨 Features

✅ **Professional Styling**
- Custom CSS with modern design
- Consistent color scheme
- Responsive layout
- Interactive components

✅ **Multi-Page Navigation**
- Automatic page discovery
- Easy navigation between pages
- Sidebar controls

✅ **Data Management**
- Support for multiple file formats (CSV, Excel, Parquet, JSON)
- Data upload capability
- Data statistics and quality metrics

✅ **Interactivity**
- Real-time filters
- Dynamic visualizations
- Hover tooltips
- Download capabilities

---

## 🔧 Customization

### Change Colors
Edit the CSS in `app.py` (lines starting with `st.markdown("""<style>...`)

### Add New Pages
1. Create a new file in `pages/` folder: `04_YourPage.py`
2. Name it with a number prefix for ordering (e.g., `04_`, `05_`)
3. Use the same structure as existing pages
4. It will automatically appear in the sidebar!

### Add Utilities
Create helper functions in `utils/` folder and import them:
```python
from utils.helpers import your_function
```

---

## 📊 Supported Data Formats

- **CSV** (.csv)
- **Excel** (.xlsx, .xls)
- **Parquet** (.parquet)
- **JSON** (.json)

---

## 💡 Usage Tips

1. **Add Data**: Place your datasets in the `/data/` folder
2. **Reload Dashboard**: Streamlit auto-reloads when you save files
3. **Share Dashboard**: Run with `--logger.level=error` to hide logs
4. **Export Views**: Use Streamlit's built-in download buttons

---

## 🐛 Troubleshooting

**Issue**: "No datasets loaded"
- **Solution**: Add data files to the `/data/` folder and refresh the page

**Issue**: Pages not showing in sidebar
- **Solution**: Ensure page files are in `/pages/` folder with correct naming (e.g., `01_Name.py`)

**Issue**: Streamlit not found
- **Solution**: Install dependencies: `pip install -r requirements.txt`

---

## 📝 License

ISEA Finals 2026 Project

---

## 🤝 Support

For issues or customizations, refer to:
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)