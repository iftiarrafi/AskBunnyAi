Here’s a **sleek, modern, GitHub-ready README** with better structure, spacing, and clarity 👇

---

# 🐹 AskBunny AI

### ⚡ High-Speed Conversational QnA Bot

**AskBunny AI** is a state-of-the-art conversational assistant designed to showcase ultra-fast LLM inference using **Groq’s LPU (Language Processing Unit)** combined with **LangChain’s orchestration power**.

This isn’t just a chatbot — it **remembers context**, enabling smooth, human-like conversations.

---

## ✨ Key Features

* ⚡ **Lightning-Fast Inference**
  Powered by **Groq Cloud** for near-instant responses.

* 🧠 **Contextual Memory**
  Maintains conversation flow using **LangChain message state management**.

* 🎨 **Clean UI/UX**
  Built with **Streamlit chat components** for a sleek, app-like experience.

* 🔐 **Security First**
  Uses **python-dotenv** to securely manage API keys and environment variables.

---

## 🛠️ Tech Stack

| Layer                 | Technology           |
| --------------------- | -------------------- |
| **Frontend**          | Streamlit            |
| **LLM Orchestration** | LangChain            |
| **Inference Engine**  | Groq Cloud           |
| **Model**             | Llama 3.3 (via Groq) |
| **Environment**       | Conda + Dotenv       |

---

## ⚙️ How It Works

AskBunny AI follows a **stateful execution flow**:

### 1. 🗂️ Session Persistence

* Uses `Streamlit.session_state` as the main data store
* Stores conversation as a list of:

  * `HumanMessage`
  * `AIMessage`

### 2. 💬 Message Handling

* Each user input is appended to the message history

### 3. 🔄 Context Injection

* Entire conversation history is sent to the model
* Enables understanding of follow-ups like:

  > *“Who is he?”*

### 4. 🎭 Smart Rendering

* UI dynamically detects message types
* Renders:

  * **User messages**
  * **Assistant responses**
    as clean chat bubbles

---

## 🚀 Why AskBunny?

> **Speed + Memory + Simplicity**

* ⚡ Faster than traditional LLM setups
* 🧠 Maintains real conversational context
* 🧩 Clean and minimal architecture
* 🎯 Perfect for learning modern AI stack integration

---

## 📌 Future Improvements (Optional Ideas)

* 🔊 Voice input/output
* 🌐 Multi-language support
* 🧾 Chat export (PDF / Markdown)
* 🧠 Long-term memory (vector DB)

---

If you want, I can also:

* 🔥 Add **installation steps + run commands**
* 📦 Add **folder structure**
* 🌍 Make it **portfolio-level README (with badges + screenshots)**
