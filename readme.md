# 🤖 Chat IA com Busca na Web

Aplicação web de IA desenvolvida com Python utilizando LLMs da Groq, integração com busca em tempo real via DuckDuckGo Search, frontend com Streamlit e backend com FastAPI.

O projeto funciona como um mini assistente de IA capaz de:

* responder perguntas
* pesquisar informações na web
* manter histórico visual de conversa
* exibir respostas em interface estilo chatbot

---

# 🚀 Demonstração

## Frontend

[https://chat-ia-frontend-msie.onrender.com](https://chat-ia-frontend-msie.onrender.com)

## Backend API

[https://agent-com-pesquisa-na-web.onrender.com/](https://agent-com-pesquisa-na-web.onrender.com/)

## Swagger Docs

[https://agent-com-pesquisa-na-web.onrender.com/docs](https://agent-com-pesquisa-na-web.onrender.com/docs)

---

# 🧠 Tecnologias utilizadas

## Frontend

* Python
* Streamlit

## Backend

* FastAPI
* Uvicorn

## Inteligência Artificial

* Groq API
* openai/gpt-oss-120b

## Busca Web

* DuckDuckGo Search (DDGS)

## Deploy

* Render

---

# 📂 Estrutura do projeto

```bash
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   └── app.py
│
├── .gitignore
└── README.md
```

---

# ⚙️ Funcionalidades

* ✅ Chat em tempo real
* ✅ Busca web integrada
* ✅ Histórico de conversa
* ✅ Interface estilo ChatGPT
* ✅ Efeito de digitação
* ✅ API REST
* ✅ Deploy em cloud
* ✅ Tratamento de erros

---

# 🖥️ Como rodar localmente

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

---

## 2. Crie o ambiente virtual

```bash
python -m venv venv
```

---

## 3. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🔑 Variáveis de ambiente

Crie um arquivo `.env`:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

# ▶️ Executando o backend

```bash
uvicorn main:app --reload
```

API disponível em:

```txt
http://127.0.0.1:8000
```

---

# ▶️ Executando o frontend

```bash
streamlit run app.py
```

Frontend disponível em:

```txt
http://localhost:8501
```

---

# 📸 Interface

O projeto possui:

* chat interativo
* efeito de digitação
* histórico de mensagens
* respostas geradas por IA
* integração com pesquisa web

---

# 📚 Aprendizados

Durante o desenvolvimento foram praticados conceitos de:

* APIs REST
* Frontend com Streamlit
* Backend com FastAPI
* Integração com LLMs
* Prompt Engineering
* Deploy em cloud
* Consumo de APIs
* Manipulação de JSON
* Tratamento de exceções
* Arquitetura cliente-servidor

---

# 🔮 Melhorias futuras

* [ ] Memória contextual real
* [ ] Streaming real de tokens
* [ ] Upload de PDFs
* [ ] RAG com embeddings
* [ ] Login de usuários
* [ ] Banco de dados
* [ ] Tema dark/light
* [ ] Múltiplos chats
* [ ] Docker

---

# 👨‍💻 Autor

Desenvolvido por Felipe Alves 🚀
