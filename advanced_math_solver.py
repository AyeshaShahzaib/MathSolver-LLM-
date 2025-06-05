import streamlit as st
from openai import OpenAI
import sympy as sp

import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)


def solve_math_problem(problem: str) -> str:
    try:
        x, y = sp.symbols('x y')
        expr = sp.sympify(problem)
        result = sp.simplify(expr)
        return f"{result}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title("🧠 Advanced Math Solver Agent (LLM-powered)")
user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), differentiate(cos(x))):") 

if st.button("Solve") and user_input:
    sympy_result = solve_math_problem(user_input)

    # LLM just explains the result
    completion = client.chat.completions.create(
        model="mistralai/mistral-nemo:free",
        messages=[
            {"role": "system", "content": "You are a helpful math expert. Given a math expression and its solution, explain it in simple terms."},
            {"role": "user", "content": f"The user input was: {user_input}\nThe computed result is: {sympy_result}\nExplain this in simple terms."}
        ]
    )

    st.markdown("### 🧮 SymPy Result:")
    st.success(sympy_result)

    st.markdown("### 💡 LLM Explanation:")
    st.info(completion.choices[0].message.content)
# import streamlit as st
# from openai import OpenAI
# import sympy as sp

# # Direct API key usage (NOT RECOMMENDED FOR PRODUCTION)
# import openai

# openai.base_url = "https://openrouter.ai/api/v1"
# openai.api_key = "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"  # ✅ Works now
# openai.default_headers = {
#     "Authorization": f"Bearer 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"
# }


# def solve_math_problem(problem: str) -> str:
#     try:
#         x, y = sp.symbols('x y')
#         expr = sp.sympify(problem)
#         simplified = sp.simplify(expr)
#         return f"Simplified Result: {simplified}"
#     except Exception as e:
#         return f"Error: {str(e)}"

# st.title("🧠 Advanced Math Solver Agent")
# user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), solve(x**2 + 3*x + 2, x)):") 

# if st.button("Solve") and user_input:
#     completion = openai.ChatCompletion.create(
#     model="mistralai/mistral-nemo:free",
#     messages=[
#         {"role": "system", "content": "You are a helpful math expert who solves problems using SymPy."},
#         {"role": "user", "content": user_input}
#     ]
# )


#     local_result = solve_math_problem(user_input)

#     st.markdown("### 💡 Mistral's Interpretation:")
#     st.info(completion.choices[0].message.content)

#     st.markdown("### 🧮 SymPy Result:")
#     st.success(local_result)