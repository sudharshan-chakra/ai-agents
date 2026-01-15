import os, re, json
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile", groq_api_key=os.getenv("GROQ_API_KEY"))

def analyze_code(code: str):
    prompt = ChatPromptTemplate.from_template("""
    Act as an expert security engineer. Analyze this Python code for vulnerabilities.
    Return ONLY a JSON object with this structure:
    {{
        "vulnerabilities": [
            {{
                "severity": "High/Medium/Low",
                "type": "Name of bug",
                "description": "Explanation",
                "patch": "Full corrected code block"
            }}
        ]
    }}
    If no bugs are found, return an empty list for vulnerabilities.
    CODE: {code}
    """)
    chain = prompt | llm
    # We use .invoke().content and then you'd normally parse the JSON string
    response = chain.invoke({"code": code})
    response.content

    try:
        # 1. Get response from Groq
        response = llm.invoke(prompt.format(code=code))
        content = response.content  # Ensure content is defined here

        # 2. Extract JSON from Markdown if the LLM wraps it in ```json ... ```
        json_match = re.search(r"```json\s*(.*?)\s*```", content, re.DOTALL)
        if json_match:
            clean_json = json_match.group(1)
        else:
            json_match = re.search(r"(\{.*\})", content, re.DOTALL)
            clean_json = json_match.group(1) if json_match else content

        return json.loads(clean_json)
    except Exception as e:
        print(f"AI Analysis or Parsing Error: {e}")
        return {"vulnerabilities": []}