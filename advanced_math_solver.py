
import streamlit as st
from openai import OpenAI

# Secure API key from secrets
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

st.title("🧠 Advanced Math Solver Agent (LLM-powered)")

# User input
user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), diff(cos(2*x), x), solve(x**2 - 4, x)):")

if st.button("Solve") and user_input:
    try:
        # LLM solves and explains
        completion = client.chat.completions.create(
            model="mistralai/mistral-nemo:free",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a math expert. Solve the user's math expression and explain it simply. "
                        "First give the final answer clearly, then explain it step-by-step. "
                        "Don't show any code. Use plain math notation (e.g., x**2, sin(x))."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )

        llm_response = completion.choices[0].message.content.strip()

        st.markdown("### 💡 LLM Result:")
        st.info(llm_response)

    except Exception as e:
        st.error(f"API Error: {str(e)}")

