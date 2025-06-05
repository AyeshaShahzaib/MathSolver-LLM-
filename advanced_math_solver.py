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
import sympy as sp
import httpx  # Use httpx for API requests

# Read API key securely from Streamlit secrets
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
MODEL = "mistralai/mistral-nemo:free"

# SymPy solver
def solve_math_problem(problem: str) -> str:
    try:
        x, y = sp.symbols('x y')  # Define symbols
        expr = sp.sympify(problem)
        result = sp.simplify(expr)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("🧠 Advanced Math Solver Agent (LLM-powered)")
user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), differentiate(cos(x))):") 

if st.button("Solve") and user_input:
    sympy_result = solve_math_problem(user_input)

    # Prepare the LLM request
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful math expert. Given a math expression and its solution, explain it in simple terms."
            },
            {
                "role": "user",
                "content": f"The user input was: {user_input}\nThe computed result is: {sympy_result}\nExplain this in simple terms."
            }
        ]
    }

    try:
        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        explanation = response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        explanation = f"API Error: {e}"

    st.markdown("### 🧮 SymPy Result:")
    st.success(sympy_result)

    st.markdown("### 💡 LLM Explanation:")
    st.info(explanation)
