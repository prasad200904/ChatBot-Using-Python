🤖 AI Chatbot using Python & Streamlit

This project is a simple AI Chatbot built using Python and Streamlit.
It allows users to interact with an AI model through a clean web interface and receive real-time responses.

The chatbot uses the Groq API with the Llama 3.1 model to generate intelligent replies based on user input.

🚀 Features

Interactive chat interface

Real-time AI responses

Chat history management

Secure API key management using environment variables

Simple and clean Streamlit UI

Easy to run locally

🛠️ Technologies Used

Python

Streamlit

Groq API

Llama 3.1 Model

dotenv

📂 Project Structure
ChatBot-Using-Python
│
├── app.py            # Streamlit user interface
├── main.py           # AI response logic
├── requirements.txt  # Project dependencies
├── .env.example      # Example environment variables
├── README.md         # Project documentation
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/ChatBot-Using-Python.git
2️⃣ Navigate to the project folder
cd ChatBot-Using-Python
3️⃣ Create virtual environment
python -m venv env

Activate environment:

Windows
env\Scripts\activate
Mac/Linux
source env/bin/activate
4️⃣ Install dependencies
pip install -r requirements.txt
🔑 Environment Setup

Create a .env file in the project root and add your Groq API key.

GROQ_API_KEY=your_api_key_here

⚠️ Never upload your .env file to GitHub.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

or

python -m streamlit run app.py

The application will open in your browser:

http://localhost:8501
💬 How the Chatbot Works

User enters a message in the chat interface.

The message is stored in Streamlit session state to maintain chat history.

The conversation history is sent to the Groq API.

The Llama 3.1 model generates a response.

The response is displayed in the chat interface.

📸 Demo

You can add a screenshot of your chatbot interface here.

Example:

![Chatbot Screenshot](screenshot.png)
📌 Future Improvements

Chat history sidebar

Save conversations in a database

User authentication

Deploy chatbot online

Add multiple AI models

👨‍💻 Author

Prasad

AI & Machine Learning Enthusiast
Passionate about building intelligent applications using Python and AI technologies.

⭐ If you like this project

Please consider giving it a star ⭐ on GitHub.
