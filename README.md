# AI Agent E-commerce Backend

An AI agent powered e-commerce backend built with FastAPI.  
This project demonstrates how an AI agent can interact with backend APIs using tool calling to perform e-commerce related tasks.

The system uses a **local LLM (Ollama)** to decide which tools to call.

---

## Features

- AI Agent with tool calling
- LLM integration using Ollama (local or cloud models)
- FastAPI backend service
- Order management API
- Product query API
- Example AI-agent interaction workflow

---

## Project Structure

```
ai-agent-ecommerce-backend/
│
├── backend/
│ └── server.py
│
├── agent/
│ └── agent.py
│
├── tools/
│ └── order_tools.py
│
├── models/
│ ├── order.py
│ └── product.py
│
├── tests/
│ └── test_api.py
│
├── requirements.txt
└── README.md
```

---

## Architecture

```
User
 ↓
FastAPI API (/agent)
 ↓
LLM (Ollama)
 ↓
AI Agent Logic
 ↓
Tool Functions
 ├ get_products()
 ├ get_order()
 └ cancel_order()
 ↓
FastAPI Backend APIs
 ↓
In-memory Data Store
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourname/ai-agent-ecommerce-backend.git
cd ai-agent-ecommerce-backend
```

Create a virtual environment:

```bash
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv venv
```

Activate the environment:

Mac / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Install Ollama (Local LLM)

Install Ollama:

```bash
brew install ollama
```

Start Ollama server:

```bash
ollama serve
```

## Using Cloud Models

This project can use Ollama cloud models such as:

- gpt-oss:20b-cloud
- deepseek-v3.1-cloud

Make sure you login first:

```bash
ollama login
ollama serve
```

## Run Backend Server

Start the FastAPI server:

```bash
uvicorn backend.server:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Testing

Run agent evaluation tests:

```bash
pytest tests/test_agent.py -s
```

## Learning Objectives

This project demonstrates:

- AI agent tool calling
- Backend API interaction
- FastAPI service development
- Local LLM integration
- AI + backend architecture design

---

## Future Improvements

Potential extensions:

- PostgreSQL database
- Retrieval-Augmented Generation (RAG)
- Chat UI interface
- Authentication and user accounts
- Order tracking integration
- Customer support ticket system
