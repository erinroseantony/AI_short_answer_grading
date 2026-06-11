📘 AI-Based Automated Short Answer Grading System
📌 Overview

This project is an AI-powered Short Answer Grading System that automatically evaluates student responses by comparing them with reference answers using Natural Language Processing (NLP) techniques.
It uses Sentence-BERT embeddings for semantic understanding and a hybrid scoring mechanism (semantic similarity + keyword matching) to generate accurate marks and feedback.
The system is built as an interactive web application using Streamlit.

🎯 Key Features

🧠 Semantic similarity using Sentence-BERT
🔑 Hybrid scoring (Semantic + Keyword-based evaluation)
📝 Automated marks calculation
💬 Intelligent feedback generation
🌐 Interactive web UI using Streamlit
⚡ Fast and lightweight inference

🏗️ System Architecture
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
      
🛠️ Tech Stack
Programming Language: Python
Frontend/UI: Streamlit
NLP Model: Sentence-BERT (all-MiniLM-L6-v2)
ML Libraries: Scikit-learn, Pandas
Core Concepts: NLP, Semantic Similarity, Feature Engineering

📂 Project Structure
AI_Short_Answer_Grading/
│
├── app.py                 # Main application file
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files
└── README.md              # Project documentation

🚀 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-short-answer-grading.git
cd ai-short-answer-grading
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
streamlit run app.py

📊 How It Works
User enters question, reference answer, and student answer
System converts text into embeddings using Sentence-BERT
Computes semantic similarity score
Computes keyword overlap score
Combines both using weighted hybrid formula:
Final Score = 0.7 × Semantic Similarity + 0.3 × Keyword Score
Converts score into marks
Generates performance feedback

📈 Example Output
Metric	Value
Semantic Similarity	54.05%
Final Score	44.26%
Marks	4.43 / 10
Feedback	Poor answer. Major concepts are missing or incorrect.

💡 Key Highlights
✔ Uses transformer-based NLP model (Sentence-BERT)
✔ Combines semantic + rule-based scoring
✔ Real-world EdTech use case
✔ Lightweight and fast execution
✔ Easy to extend with ML models or databases

⚠️ Limitations
May give moderate scores for incorrect but semantically similar sentences
Keyword matching is basic (can be improved using NLP extraction techniques)
No database storage implemented yet

🚀 Future Improvements
Integration with LLM-based evaluation (GPT-style scoring)
Student performance tracking database (MySQL/SQLite)
Multi-question exam evaluation system
Advanced negative marking system for wrong concepts
Deployment on cloud (Streamlit Cloud / AWS)

👨‍💻 Author
Erin Rose Antony
Aspiring AI/ML Engineer
