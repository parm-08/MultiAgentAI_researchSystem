# 🔍 Multi-Agent AI Research System

An intelligent **Multi-Agent AI Research System** that automates the complete research workflow using specialized AI agents for **web search, content extraction, report generation, and report evaluation**.

The system leverages **LangChain, Groq LLMs, Tavily Search, FastAPI, and BeautifulSoup** to generate **structured, reliable, and comprehensive research reports** through an interactive web interface.

---

## 🚀 Features

### 🌐 Web Search Agent

* Searches the internet for recent and reliable information using the **Tavily API**.
* Retrieves relevant sources based on the user's research topic.

### 📖 Reader Agent

* Scrapes and extracts meaningful content from web pages.
* Cleans and preprocesses extracted information for downstream tasks.

### ✍️ Research Writer Agent

* Generates detailed, professional, and well-structured research reports.
* Organizes findings into clear sections for better readability.

### 📝 Research Critic Agent

* Evaluates the generated report.
* Identifies strengths, weaknesses, and improvement opportunities.
* Provides constructive feedback to enhance report quality.

### ⚡ FastAPI Backend

* Exposes the complete multi-agent workflow through REST APIs.
* Enables easy integration with external applications.

### 🎨 Interactive Frontend

* Simple and user-friendly interface built with **HTML, CSS, and JavaScript**.
* Allows users to submit research queries and view generated reports seamlessly.

---

## 🏗️ System Architecture

```text
                    User Query
                         │
                         ▼
          ┌────────────────────────┐
          │   Search Agent         │
          │   (Tavily Search API)  │
          └────────────────────────┘
                         │
                         ▼
          ┌────────────────────────┐
          │    Reader Agent        │
          │ (Web Content Scraper)  │
          └────────────────────────┘
                         │
                         ▼
          ┌────────────────────────┐
          │   Writer Agent (LLM)   │
          └────────────────────────┘
                         │
                         ▼
          ┌────────────────────────┐
          │   Critic Agent (LLM)   │
          └────────────────────────┘
                         │
                         ▼
       Final Research Report + Feedback
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* Groq LLM
* Tavily API

### Frontend

* HTML
* CSS
* JavaScript

### Libraries & Tools

* BeautifulSoup4
* Requests
* Pydantic
* Uvicorn
* Python-dotenv

---

## 📂 Project Structure

```text
MultiAgentAI_researchSystem/
│
├── static/                     # Frontend files
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── agents.py                   # Search and Reader agents
├── tools.py                    # Tavily search and scraping tools
├── pipeline.py                 # Complete multi-agent workflow
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Project dependencies
├── Procfile                    # Deployment configuration
├── README.md                   # Project documentation
├── .env                        # Environment variables
│
└── venv/                       # Virtual environment (optional)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/parm-08/MultiAgentAI_researchSystem.git
cd MultiAgentAI_researchSystem
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Running the Application Locally

Start the FastAPI server:

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---


## 🚀 Deployment

The project can be deployed on platforms such as:

* Render
* Railway
* AWS
* Azure
* Google Cloud

### Live Demo

https://multiagentai-researchsystem.onrender.com/
---

## 📈 Future Enhancements

* 📄 PDF report generation
* 📝 DOCX report export
* 🔗 Automatic citation generation
* 🧠 Conversational memory
* 🌍 Multi-source web scraping
* 🤖 Multi-LLM support
* ⚡ Real-time streaming responses
* 📚 Research history tracking

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature-name
```

5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Parmpreet Kaur**

AI/ML Enthusiast | Generative AI Developer | Building Intelligent AI Systems

⭐ If you found this project useful, don't forget to star the repository.
