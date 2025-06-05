# import streamlit as st
# from openai import OpenAI
# import sympy as sp

# import os

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=st.secrets["OPENROUTER_API_KEY"]
# )


# def solve_math_problem(problem: str) -> str:
#     try:
#         x, y = sp.symbols('x y')
#         expr = sp.sympify(problem)
#         result = sp.simplify(expr)
#         return f"{result}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# st.title("🧠 Advanced Math Solver Agent (LLM-powered)")
# user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), differentiate(cos(x))):") 

# if st.button("Solve") and user_input:
#     sympy_result = solve_math_problem(user_input)

#     # LLM just explains the result
#     completion = client.chat.completions.create(
#         model="mistralai/mistral-nemo:free",
#         messages=[
#             {"role": "system", "content": "You are a helpful math expert. Given a math expression and its solution, explain it in simple terms."},
#             {"role": "user", "content": f"The user input was: {user_input}\nThe computed result is: {sympy_result}\nExplain this in simple terms."}
#         ]
#     )

#     st.markdown("### 🧮 SymPy Result:")
#     st.success(sympy_result)

#     st.markdown("### 💡 LLM Explanation:")
#     st.info(completion.choices[0].message.content)
import streamlit as st
from openai import OpenAI

# Secure API key from secrets
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

st.title("🧠 Advanced Math Solver Agent (LLM-powered only)")

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

