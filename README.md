# AI Agent E-commerce Backend

An AI agent powered e-commerce backend built with FastAPI. This project demonstrates how an AI agent can interact with backend APIs using tool calling to perform e-commerce related tasks.

---

## Features

- AI Agent with tool calling
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
│   └── server.py
│
├── agent/
│   └── agent.py
│
├── requirements.txt
└── README.md
```

---

## Architecture

```
User
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

## API Endpoints

### Get Products

```
GET /products
```

### Get Order

```
GET /order/{order_id}
```

### Create Order

```
POST /order
```

### Cancel Order

```
POST /order/{order_id}/cancel
```

---

## Running the AI Agent

Run the agent script:

```bash
python agent/agent.py
```

Example queries:

```
Where is order 1001?
Cancel order 1002
What products are available?
```

The AI agent will call backend APIs using tool functions.

---

## Learning Objectives

This project demonstrates:

- AI agent tool calling
- Backend API interaction
- FastAPI service development
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
