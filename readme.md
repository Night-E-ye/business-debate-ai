# 🧠 Strategy Room – AI Debate & Consensus System

Strategy Room is an AI-powered debate simulation where two autonomous agents argue **for** and **against** a business topic and then arrive at a **neutral, system-generated consensus** displayed separately from the discussion.

This project demonstrates structured multi-agent reasoning, debate orchestration, and post-debate synthesis using a locally hosted LLM.

---

## 📌 Project Overview

- **Topic**: Marketing vs Sales  
- **Agents**:
  - **Alex (FOR)** – Marketing-first strategy
  - **Sam (AGAINST)** – Sales-first strategy
- **Moderator**: Neutral AI agent (Consensus Generator)
- **Execution Mode**: Fully Local (Ollama)

---

## ⚙️ System Architecture

```text
User
 ↓
Frontend (index.html)
 ↓
Flask Backend (app.py)
 ↓
Ollama (LLaMA 3.2 Model)
```

---

## ▶️ Flow Explanation

1. Debate starts with clear role definitions
2. Agents respond turn-by-turn
3. Thinking indicators show active processing
4. Debate history is preserved
5. Moderator AI generates a shared operating model
6. Final consensus is shown in a separate panel

---

## 🛠️ Tech Stack

| Layer | Technology |
| ------------- | ------------------------------ |
| Frontend | HTML, Tailwind CSS, JavaScript |
| Backend | Python, Flask |
| AI Runtime | Ollama |
| Model | LLaMA 3.2 (1B) |
| Communication | REST API |

---

## 📂 Project Structure

```
Debatic Bots/
│
├── app.py          # Flask backend (debate + consensus)
├── index.html      # Frontend UI
├── README.md       # Project documentation
```

---

## 🚀 How to Run the Project

### Prerequisites

- Python 3.8+
- Ollama installed and running
- LLaMA 3.2 (1B) model downloaded

### Step-by-Step Instructions

#### 1️⃣ Start Ollama

Make sure Ollama is running and the model is available:

```bash
ollama run llama3.2:1b
```

#### 2️⃣ Install Dependencies

```bash
pip install flask flask-cors requests
```

#### 3️⃣ Run Backend Server

```bash
python app.py
```

Server will start at:
```
http://127.0.0.1:5000
```

#### 4️⃣ Open Frontend

Open `index.html` directly in your browser, or use a local server:

**Option 1: Direct File Access**
```
file:///path/to/your/Debatic%20Bots/index.html
```

**Option 2: Simple HTTP Server**
```bash
python -m http.server 8000
```
Then navigate to: `http://localhost:8000`

---

## 🔧 Configuration

### Change the Debate Topic

Edit `app.py` and modify the topic in the debate prompts:

```python
# Current topic: Marketing vs Sales
# Change to your preferred topic
```

### Adjust AI Model

To use a different Ollama model, update the model name in `app.py`:

```python
"model": "llama3.2:1b"  # Change to your preferred model
```



