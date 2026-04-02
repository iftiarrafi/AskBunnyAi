
🐹 AskBunny AI: High-Speed QnA Bot
AskBunny AI is a state-of-the-art conversational assistant built to demonstrate the power of Groq's LPU (Language Processing Unit) inference combined with LangChain's orchestration. This bot doesn't just answer questions—it remembers the context of your conversation for a truly interactive experience.

 Key Features
Lightning-Fast Inference: Powered by Groq Cloud to deliver responses in milliseconds.

Contextual Memory: Uses LangChain's message state management to remember previous parts of the chat.

Clean UI/UX: Built with Streamlit’s modern chat components for a native app feel.

Security First: Implements python-dotenv to keep API credentials isolated from the source code.

 Technical Stack
Frontend: Streamlit

LLM Orchestration: LangChain

Inference Engine: Groq Cloud

Model: Llama 3.3 (via Groq)

Environment Management: Conda & Dotenv

 How It Works
The application follows a Stateful Execution Flow:

Session Persistence: Streamlit's session_state acts as the primary data store, holding a list of HumanMessage and AIMessage objects.

Message History: When a user inputs a query, the script appends it to the history.

Context Injection: Instead of sending a single string, the entire history list is passed to the model. This allows the AI to understand pronouns and follow-up questions (e.g., "Who is he?" after mentioning a name).

Object-Oriented Rendering: The UI dynamically checks the type of each message object to render "user" or "assistant" chat bubbles correctly.
