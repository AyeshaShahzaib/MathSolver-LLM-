import streamlit as st
from openai import OpenAI
import sympy as sp


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

st.title("🧠 Advanced Math Solver Agent (LLM-powered)")

user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), differentiate(cos(x))):")

if st.button("Solve") and user_input:
    try:
        
        completion = client.chat.completions.create(
            model="mistralai/mistral-nemo:free",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a mathematical expert. Your task is to solve math expressions like SymPy. "
                        "Return only the final simplified result. No explanation, no code. "
                        "Just return clean SymPy-style expressions like -sin(x), x**2 + 3*x + 2, etc."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )

        gpt_response = completion.choices[0].message.content.strip()

    except Exception as e:
        gpt_response = f"API Error: {str(e)}"

    st.markdown("### 💡 LLM Result:")
    st.success(gpt_response)
