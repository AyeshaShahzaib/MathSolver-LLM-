# import streamlit as st
# import sympy as sp
# import os
# from openai import OpenAI

# # Initialize OpenRouter client
# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key="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",  # Replace with your actual OpenRouter API key
# )

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
#     try:
#         completion = client.chat.completions.create(
#     model="mistralai/mistral-nemo:free",
#     messages=[
#         {"role": "system", "content": (
#     "You are a mathematical expert. Your task is to solve math expressions like SymPy. "
#     "Return only the final simplified result. No explanation, no code. "
#     "Just return clean SymPy-style expressions like -sin(x), x**2 + 3*x + 2, etc."
# )},
#         {"role": "user", "content": user_input}
#     ]
# )
#         gpt_response = completion.choices[0].message.content
#     except Exception as e:
#         gpt_response = f"API Error: {str(e)}"
    
#     local_result = solve_math_problem(user_input)

#     st.markdown("Result")
#     st.info(gpt_response)

    # st.markdown("### 🧮 SymPy Result:")
    # st.success(local_result)


import streamlit as st
from openai import OpenAI
import sympy as sp

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # replace with your key
)

st.title("🧠 Advanced Math Solver Agent (LLM-powered)")

user_input = st.text_area("Enter a math expression (e.g., integrate(sin(x)), differentiate(cos(x))):")

if st.button("Solve") and user_input:
    try:
        # Call to LLM via OpenRouter
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
