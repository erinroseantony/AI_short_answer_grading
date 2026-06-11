import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()


def calculate_similarity(reference_answer, student_answer):
    embeddings = model.encode([reference_answer, student_answer])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity

def keyword_score(reference, student):
    ref_words = set(reference.lower().split())
    stu_words = set(student.lower().split())

    if len(ref_words) == 0:
        return 0

    match = ref_words.intersection(stu_words)
    return len(match) / len(ref_words)

def hybrid_score(similarity, reference, student):
    k_score = keyword_score(reference, student)

    final_score = (
        0.7 * similarity +
        0.3 * k_score
    )

    return final_score


def assign_marks(score, max_marks):
    marks = round(score * max_marks, 2)

    if marks > max_marks:
        marks = max_marks

    return marks

def generate_feedback(score):
    if score >= 0.85:
        return "Excellent answer. Strong understanding of the concept."
    elif score >= 0.70:
        return "Good answer. Minor improvements needed."
    elif score >= 0.50:
        return "Average answer. Missing some key points."
    else:
        return "Poor answer. Major concepts are missing or incorrect."


st.set_page_config(
    page_title="AI Short Answer Grading System",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI-Based Automated Short Answer Grading System")

question = st.text_input("Question")
reference_answer = st.text_area("Reference Answer", height=150)
student_answer = st.text_area("Student Answer", height=150)
max_marks = st.number_input("Maximum Marks", min_value=1, max_value=100, value=10)


if st.button("Grade Answer"):

    if not reference_answer or not student_answer:
        st.warning("Please enter both Reference and Student answers.")
        st.stop()

    similarity = calculate_similarity(reference_answer, student_answer)

    final_score = hybrid_score(
        similarity,
        reference_answer,
        student_answer
    )

    marks = assign_marks(final_score, max_marks)
    feedback = generate_feedback(final_score)
    st.success("Evaluation Completed")


    col1, col2 = st.columns(2)

    with col1:
        st.metric("Semantic Similarity", f"{similarity:.2%}")

    with col2:
        st.metric("Final Score", f"{final_score:.2%}")

    st.metric("Marks Obtained", f"{marks}/{max_marks}")

    st.subheader("Feedback")
    st.write(feedback)

    result_df = pd.DataFrame({
        "Question": [question],
        "Similarity": [round(similarity, 4)],
        "Final Score": [round(final_score, 4)],
        "Marks": [marks],
        "Feedback": [feedback]
    })

    st.subheader("Result Summary")
    st.dataframe(result_df)