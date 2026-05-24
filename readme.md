# 🤖 Chat IA com Groq + FastAPI + Streamlit

Aplicação de Inteligência Artificial com:

- Frontend usando Streamlit
- Backend usando FastAPI
- Busca web com DuckDuckGo
- LLM hospedada na Groq
- Arquitetura separada frontend/backend

---

# 🚀 Tecnologias utilizadas

## Frontend
- Python
- Streamlit

## Backend
- FastAPI
- Uvicorn

## IA
- Groq API
- Modelo `openai/gpt-oss-120b`

## Busca Web
- DuckDuckGo Search (DDGS)

---

# 📂 Estrutura do Projeto

```bash
projeto/
│
├── backend/
│   ├── venv/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Instalação

## 1. Clone o projeto

```bash
git clone URL_DO_PROJETO
```

---

## 2. Entre na pasta

```bash
cd projeto
```

---

## 3. Crie o ambiente virtual

### Windows

```bash
python -m venv backend/venv
```

---

## 4. Ative o ambiente virtual

### PowerShell

```bash
.\backend\venv\Scripts\activate
```

---

# 📦 Instale as dependências

```bash
pip install fastapi uvicorn streamlit requests groq ddgs python-dotenv
```

---

# 🔑 Configuração da API Key

Crie um arquivo `.env`

```env
GROQ_API_KEY=SUA_CHAVE_AQUI
```

---

# ▶️ Executando o projeto

## Backend

```bash
uvicorn backend.main:app --reload
```

API disponível em:

```bash
http://localhost:8000
```

---

## Frontend

Em outro terminal:

```bash
streamlit run frontend/app.py
```

Frontend disponível em:

```bash
http://localhost:8501
```

---

# 🧠 Como funciona

Fluxo da aplicação:

```text
Usuário
   ↓
Streamlit (Frontend)
   ↓
FastAPI (Backend)
   ↓
DuckDuckGo Search
   ↓
Groq LLM
   ↓
Resposta gerada
   ↓
Frontend
```

---

# 💬 Interface estilo ChatGPT

A aplicação utiliza:

- `st.chat_input()`
- `st.chat_message()`
- `st.session_state`

Para criar:
- histórico de conversa
- memória temporária
- interface moderna estilo chat

---

# 🔍 Funcionalidades

- Pesquisa web em tempo real
- Integração com LLMs
- Histórico de conversa
- Interface moderna
- Backend desacoplado
- Estrutura escalável

---

# 📌 Melhorias futuras

- [ ] Memória contextual
- [ ] Streaming de respostas
- [ ] Upload de PDF
- [ ] Embeddings
- [ ] Banco vetorial
- [ ] Sistema RAG
- [ ] Deploy no Render
- [ ] Docker
- [ ] Autenticação

---

# 👨‍💻 Autor

Desenvolvido por Felipe Alves 🚀
