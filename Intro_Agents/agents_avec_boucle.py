
import requests
import json
import subprocess

API_KEY = "P4R7j6HmC4zIEwVKvrWbnAMNOSiO8vYT"
API_URL = "https://api.mistral.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

functions = [
    {
        "name": "writeFile",
        "description": "Écrit un contenu dans un fichier.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Chemin du fichier"},
                "content": {"type": "string", "description": "Contenu du fichier"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "launchPythonFile",
        "description": "Lance un script Python local",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Chemin du script"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "stop",
        "description": "Indique que toutes les tâches sont terminées",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]

def writeFile(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"Fichier écrit : {path}")

def launchPythonFile(path):
    print(f"Lancement du fichier : {path}")
    subprocess.run(["python", path])

def call_llm(messages):
    body = {
        "model": "mistral-small",
        "messages": messages,
        "functions": functions,
        "temperature": 0.2
    }
    res = requests.post(API_URL, headers=headers, data=json.dumps(body))
    return res.json()

def run_agent(prompt, max_steps=5):
    messages = [{"role": "user", "content": prompt}]
    for step in range(max_steps):
        print(f"--- Étape {step+1} ---")
        response = call_llm(messages)
        choice = response["choices"][0]
        msg = choice["message"]

        if "function_call" not in msg:
            print("Pas d'appel de fonction détecté. Fin.")
            break

        name = msg["function_call"]["name"]
        args = json.loads(msg["function_call"]["arguments"])

        if name == "writeFile":
            writeFile(args["path"], args["content"])
        elif name == "launchPythonFile":
            launchPythonFile(args["path"])
        elif name == "stop":
            print("L'agent a terminé toutes les tâches.")
            break

        messages.append(msg)
        messages.append({"role": "function", "name": name, "content": "OK"})

if __name__ == "__main__":
    run_agent("Crée un fichier Python qui dit bonjour puis exécute-le. Ensuite stoppe.", max_steps=5)
