# 📘 AI-Based Automated Short Answer Grading System

## 📌 Overview
This project is an AI-powered system that automatically evaluates student short answers using Natural Language Processing (NLP). It compares student responses with reference answers and assigns marks using a hybrid approach combining semantic similarity (Sentence-BERT) and keyword matching.

The system is built using Python and deployed as an interactive web application using Streamlit.

---

## 🎯 Features
- 🧠 Semantic similarity using Sentence-BERT
- 🔑 Keyword-based scoring system
- ⚖️ Hybrid scoring (semantic + keyword)
- 📝 Automated marks generation
- 💬 AI-based feedback generation
- 🌐 Interactive Streamlit web interface
- ⚡ Fast and lightweight inference

---

## 🏗️ System Architecture

```text
Student Answer + Reference Answer
            ↓
   Text Embedding (Sentence-BERT)
            ↓
   Semantic Similarity Score
            ↓
   Keyword Matching Score
            ↓
   Hybrid Score Calculation
            ↓
   Marks + Feedback Generation
            ↓
   Streamlit Web Interface
```

---

## 🛠️ Tech Stack
- Python 🐍
- Streamlit 🌐
- Sentence-Transformers (BERT Model)
- Scikit-learn
- Pandas

---

## 📂 Project Structure

```text
AI_Short_Answer_Grading/
│
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .gitignore          # Ignored files
└── README.md           # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-short-answer-grading.git
cd ai-short-answer-grading
```

---

### 2️⃣ Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application
```bash
streamlit run app.py
```

---

## 📊 Example Output

| Metric | Value |
|--------|------|
| Semantic Similarity | 54.05% |
| Final Score | 44.26% |
| Marks Obtained | 4.43 / 10 |
| Feedback | Poor answer. Major concepts are missing or incorrect |

---

## 💡 Key Highlights
✔ Uses Sentence-BERT for semantic understanding  
✔ Hybrid scoring improves evaluation accuracy  
✔ Real-world EdTech AI use case  
✔ Lightweight and fast Streamlit deployment  
✔ Beginner-friendly yet industry-relevant project  

---

## ⚠️ Limitations
- May give moderate scores for incorrect but semantically similar answers  
- Keyword scoring is basic (can be improved further)  
- No database integration yet  
- No multi-user exam system  

---

## 🚀 Future Improvements
- 🔥 Add database (SQLite/MySQL) for storing results  
- 🤖 Improve keyword extraction using NLP techniques  
- 📊 Add performance analytics dashboard  
- 🧠 Integrate LLM-based evaluation (GPT-style scoring)  
- 🌍 Deploy on Streamlit Cloud / Render  

---

## 👨‍💻 Author
**Erin Rose Antony**  
Aspiring AI/ML Engineer  

---
 
