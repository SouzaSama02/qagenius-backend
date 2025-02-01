import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Carregar variáveis de ambiente
from dotenv import load_dotenv

load_dotenv()

# Carregar dados do prompt
prompt_file_path = "src/prompt/prompt.json"
if os.path.exists(prompt_file_path):
    with open(prompt_file_path, "r") as file:
        prompt_data = json.load(file)
else:
    prompt_data = {"instruction": "", "details": {}, "format": ""}

app = Flask(__name__)
CORS(app)

key = os.getenv("GOOGLE_GEN_AI_KEY")
if not key:
    raise ValueError("A chave da API do Google Generative AI não foi encontrada. Verifique suas variáveis de ambiente.")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/prompt", methods=["POST"])
def generate_response():
    try:
        data = request.get_json()
        input_text = data.get("inputText", "")

        prompt = (
                prompt_data["instruction"] + "\n" +
                "\n".join([f"{key}: {value}" for key, value in prompt_data["details"].items()]) + "\n" +
                f"Informação adicional: {input_text}\n" +
                f"Formato esperado: {prompt_data['format']}"
        )

        result = model.generate_content(prompt)
        response_text = result.text

        return jsonify({"response": response_text, "success": True})
    except Exception as e:
        print("Erro ao enviar resposta:", e)
        return jsonify({"response": "Erro ao processar a resposta. Tente novamente.", "success": False}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
