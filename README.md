# Profile Checker

### Developed By (in Alphabetical Order):

1. Daggupati Venkata N R Mohitananda Sanjay (mohitanandasanjay@gmail.com)
2. Mohammad Sadiq (mohammadsadiq4950@gmail.com)
3. Tanvi Kandepuneni (kandepuneni24@gmail.com)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/MdSadiqMd/profile-checker.git
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Required Dependencies
```bash
pip install flask PyPDF2 python-docx spacy
```

### 5. Download the SpaCy English Language Model
```bash
python -m spacy download en_core_web_sm
```

### 6. Run the Application
```bash
python app.py
```