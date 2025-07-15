import requests
import json
import subprocess

# 1. Fonction pour appeler le LLM (Mistral via API)
def generateText(prompt: str) -> str:
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer P4R7j6HmC4zIEwVKvrWbnAMNOSiO8vYT",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-tiny",  # ou mistral-medium selon votre accès
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# 2. Fonctions disponibles pour le LLM (function calling)
def writeFile(path: str, content: str):
    with open(path, 'w') as f:
        f.write(content)

def launchPythonFile(path: str):
    subprocess.run(["python", path], check=True)

# 3. Prompt pour que le LLM appelle une fonction
function_prompt = """
Tu as accès aux fonctions suivantes :
- writeFile(path, content) : écrit dans un fichier
- launchPythonFile(path) : exécute un fichier Python

Ta réponse doit être un JSON avec deux clés :
{
  "function": "nom_de_la_fonction",
  "arguments": {
    "arg1": "valeur1",
    "arg2": "valeur2"
  }
}

Je veux que tu crées un fichier "hello.py" contenant ce code : print("hello world")
"""

# 4. Appel au LLM
response = generateText(function_prompt)
print("Réponse brute du LLM :", response)

# 5. Parsing du JSON généré par le LLM
command = json.loads(response)
function_name = command["function"]
args = command["arguments"]

# 6. Exécution de la fonction demandée par le LLM
if function_name == "writeFile":
    writeFile(**args)
elif function_name == "launchPythonFile":
    launchPythonFile(**args)
else:
    print("Fonction non reconnue.")
