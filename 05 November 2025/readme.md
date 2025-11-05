🌟 ProjectMate — Internal Project Recommender & Growth Companion

💼 Empowering employees to find the right internal projects, grow their skills, and connect with AI-driven learning insights.

🚀 Overview

ProjectMate is an internal web application built for tech companies to help employees:

Discover active internal projects they can join.

Get AI-powered recommendations based on their skills.

Identify skill gaps and receive upskilling suggestions.

Chat with an AI career companion for personalized advice.

Built using FastAPI (Python) for the backend and React (Lovable) for the frontend, it’s designed to be simple, smart, and scalable.

🧠 Features
Category	Features
👤 Employee Management	Add new employees, validate unique IDs, and view existing employee profiles.
💼 Project Recommender	AI-based skill matching recommends best-fit projects for employees.
📈 Skill Growth	Displays trending skills and learning resources.
💬 Chat Assistant	Friendly chatbot that guides users through skill growth and project discovery.
🗂️ Database Integration	Uses SQLite (dynamic) — updates automatically when new employees are added.
🧠 AI Integration	Semantic project matching powered by Sentence Transformers.
☁️ Deployment-Ready	Backend deployable on Render, frontend on Vercel.
🏗️ Tech Stack
🧩 Frontend

React (Lovable-generated UI)

TailwindCSS

ShadCN UI components

React Query for API integration

Vite build tool

⚙️ Backend

FastAPI

SQLAlchemy + SQLite

Uvicorn

Sentence Transformers (for AI matching)

TensorFlow (optional for advanced AI)

🧱 Database

SQLite (local)

PostgreSQL (recommended for cloud deployment)

📂 Project Structure
ProjectMate/
│
├── backend/
│   ├── main.py              # FastAPI app
│   ├── database.py          # DB setup
│   ├── models.py            # Employee & Project schemas
│   ├── recommender.py       # AI-based recommender logic
│   ├── chatbot.py           # Chat assistant logic
│   ├── data/
│   │   └── projects.json    # Sample projects
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
└── requirements.txt

⚡ Setup & Installation
🧱 Backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend will run on:
👉 http://127.0.0.1:8000

Interactive Docs:

📘 Swagger UI: http://127.0.0.1:8000/docs

💻 Frontend (React)
cd frontend
npm install
npm run dev


Frontend will run on:
👉 http://localhost:5173

🔗 API Endpoints
Endpoint	Method	Description
/api/employees	GET	Get all employees
/api/employees	POST	Add a new employee
/api/projects	GET	Fetch all active projects
/api/employees/{name}/recommendations	GET	Get project recommendations
/api/chat	POST	Chatbot interaction
/api/status	GET	Health check
🧠 AI-Powered Recommendation Engine

Uses Sentence Transformers (all-MiniLM-L6-v2) to compute semantic similarity between:

Employee skills

Project requirements

It returns the best-matching projects with a similarity score (in %).

💬 Chat Assistant

The in-app chatbot helps employees by:

Answering questions about available projects

Recommending trending skills

Motivating and guiding career growth

🧩 Example Workflow

Add yourself as an employee (with your skills).

Browse recommended internal projects.

Chat with the assistant to learn what skills to upgrade.

Apply or upskill based on your recommendations.

🧾 Sample API Request
Add Employee
POST /api/employees
{
  "id": 101,
  "name": "Charvi Jain",
  "email": "charvi@company.in",
  "skills": "python, react, data analysis"
}

Get Recommendations
GET /api/employees/Charvi Jain/recommendations


Response:

{
  "employee": "Charvi Jain",
  "recommendations": [
    {
      "project_name": "AI Automation Platform",
      "description": "Develop an AI assistant for workflows",
      "match_score": 92.5
    }
  ]
}

🧰 Troubleshooting
Issue	Fix
numpy.dtype size changed	Downgrade NumPy to 1.26.4
MessageFactory has no attribute GetPrototype	Downgrade protobuf to 3.20.3
Employee not showing in list	Refresh frontend / ensure API re-fetch
Chatbot generic replies	Update chatbot.py logic
☁️ Deployment (Optional)
Component	Platform	Command
Backend	Render.com
	Deploy FastAPI
Frontend	Vercel
	Connect GitHub repo
Database	NeonDB / Supabase
	Use PostgreSQL
❤️ Contributing

Pull requests are welcome!
If you’d like to suggest a feature or fix a bug:

Fork the repo

Create a new branch

Commit changes

Submit a PR 🎉

🧑‍💻 Author

Charvi Jain
👩‍💻 AI & Software Enthusiast
💬 “Building tools that help people grow while they work.”
