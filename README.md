# QAGenius Backend

Este é o backend do projeto **QAGenius**, responsável por processar requisições e interagir com a API do Google Generative AI.

## 🔧 Tecnologias Utilizadas

- **Flask** – Framework web para Python
- **Flask-CORS** – Para permitir requisições entre diferentes origens
- **Google Generative AI** – Para geração de textos
- **Python-Dotenv** – Para carregar variáveis de ambiente
- **JSON** – Para manipulação de arquivos de prompt

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório
```sh
git clone https://github.com/SouzaSama02/qagenius-backend.git
cd api
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instalar as dependências
```sh
pip install -r requirements.txt
```

### 4️⃣ Criar o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:
```
GOOGLE_GEN_AI_KEY=your_api_key_here
PORT=3000  # Opcional, caso queira definir uma porta específica
```

### 5️⃣ Iniciar o servidor
```sh
python api.py
```
O backend será iniciado em `http://127.0.0.1:3000/`.

## 📌 Estrutura do Projeto
```
requerimento-backend/
│── src/
│   ├── prompt/
│   │   ├── prompt.json  # Arquivo com estrutura do prompt
│── api.py  # Código principal do backend
│── requirements.txt  # Dependências do projeto
│── .env  # Variáveis de ambiente
```

## 📌 Endpoints Disponíveis

### 🔹 `POST /prompt`
- **Descrição:** Gera uma resposta baseada no prompt pré-definido e no input do usuário.
- **Body:**
  ```json
  {
    "inputText": "Me fale sobre inteligência artificial."
  }
  ```
- **Resposta:**
  ```json
  {
    "response": "A inteligência artificial é uma área da ciência da computação...",
    "success": true
  }
  ```
- **Erros:**
  ```json
  {
    "response": "Erro ao processar a resposta. Tente novamente.",
    "success": false
  }
  ```

## 🔗 Frontend do Projeto
Este backend é utilizado pelo frontend disponível em: [QAGenius Frontend](https://github.com/SouzaSama02/qagenius-frontend)

## 🛠 Contribuição
Sinta-se à vontade para contribuir! Faça um fork do repositório, crie uma branch e envie um pull request.

## 📜 Licença
Este projeto é distribuído sob a licença MIT.
