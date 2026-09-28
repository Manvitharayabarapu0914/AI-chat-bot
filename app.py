import streamlit as st
import ollama

# Internal CSS
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap');

* {
    font-family: 'Fredoka', sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #fff0f6, #f3e8ff);
}

/* Main title */
h1 {
    text-align: center;
    color: #d9468b;
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* Normal text */
p {
    color: #7c5470;
    font-size: 18px;
}

/* Input box */
.stTextInput input {
    background-color: #ffffff;
    color: #5b3b52;
    border: 2px solid #f3a6c8;
    border-radius: 18px;
    padding: 14px;
    font-size: 17px;
}

/* Input box when clicked */
.stTextInput input:focus {
    border-color: #d9468b;
    box-shadow: 0 0 10px rgba(217, 70, 139, 0.2);
}

/* Ask button */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #f472b6, #c084fc);
    color: white;
    border: none;
    border-radius: 20px;
    padding: 12px;
    font-size: 19px;
    font-weight: 600;
    transition: 0.3s;
}

/* Button hover */
.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0 5px 15px rgba(192, 132, 252, 0.3);
}

/* AI response */
.response-box {
    background-color: rgba(255, 255, 255, 0.85);
    border: 2px solid #f3c4dc;
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
    color: #5b3b52;
    font-size: 17px;
    box-shadow: 0 5px 20px rgba(190, 120, 170, 0.12);
}

</style>
""", unsafe_allow_html=True)


st.title("🌸 Friendly AI Bot")

st.write("✨ Ask me anything! I'm here to help 💕")

question = st.text_input("💭 Enter Your Question:")

if st.button("✨ Ask AI"):

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": """
                You are a friendly and funny AI assistant.
                Explain things in simple language.
                Be helpful and encouraging.
                """
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response["message"]["content"]

    st.write("💌 AI Response")

    st.markdown(
        f'<div class="response-box">{answer}</div>',
        unsafe_allow_html=True
    )