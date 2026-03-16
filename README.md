# AI Agent E-commerce Backend

An AI agent powered e-commerce backend built with FastAPI.  
This project demonstrates how an AI agent can interact with backend APIs using tool calling to perform e-commerce related tasks.

The system uses a **local LLM (Ollama)** to decide which tools to call.

---

## Features

- AI Agent with tool calling
- Local LLM using Ollama
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
Local LLM (Ollama)
↓
AI Agent
↓
Tool Functions
├ get_order()
├ cancel_order()
├ create_order()
└ get_products()
↓
FastAPI Backend
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

Download a small model:

```bash
ollama run phi3:mini
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

Run Backend Server

Start the FastAPI server:

```
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

## Running the AI Agent

Run the agent script:

```bash
python -m agent.agent
```

Example queries:

```
show products
where is my order 1001
cancel order 1002
```

The AI agent will call backend APIs using tool functions.

---

## Testing

Run API tests:

```
pytest
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
