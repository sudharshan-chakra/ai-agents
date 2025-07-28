import httpx
import operator
import ast

safe_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg
}

def safe_eval(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return safe_operators[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        return safe_operators[type(node.op)](safe_eval(node.operand))
    else:
        raise TypeError(node)

def calculate(what):
    try:
        return safe_eval(ast.parse(what, mode='eval').body)
    except (TypeError, KeyError, SyntaxError):
        return "Error: Invalid or unsafe calculation."

def wikipedia(q):
    # sourcery skip: reintroduce-else, swap-if-else-branches, use-named-expression
    try:
        response =  httpx.get("https://en.wikipedia.org/w/api.php", params={
            "action": "query",
            "list": "search",
            "srsearch": q,
            "format": "json"
        }).json()["query"]["search"][0]["snippet"]
        response.raise_for_status()
        search_results = response.json()["query"]["search"]
        if not search_results:
            return "No results found on Wikipedia."
        return search_results[0]["snippet"]
    except httpx.RequestError as e:
        return f"Error connecting to Wikipedia: {e}"
    except (KeyError, IndexError):
        return "Error parsing Wikipedia's response."


known_actions = {
    "wikipedia": wikipedia,
    "calculate": calculate,
}