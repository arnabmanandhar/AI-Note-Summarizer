# AI Note Summarizer

The AI Note Summarizer is a web-based application designed to help users automatically summarize long pieces of text or notes using advanced Natural Language Processing (NLP) techniques. Built using Python and FastAPI, this project enables users to send input text and receive concise summaries via a RESTful API.A FastAPI-based REST API service that summarizes input text using state-of-the-art transformer models. This project provides a simple, efficient API to generate concise summaries from longer text inputs.

---
## Key Features

-	Accepts user input through API endpoints.
-	Returns summarized content based on the provided note.
-	Deployed online using Render with Docker support.
-	Includes automated CI/CD workflows using GitHub Actions.
- Summarize any input text with a single POST request.
- FastAPI backend for high-performance API.
- Uses Hugging Face Transformers for text summarization.
- Includes test cases with pytest.
- Docker-ready for easy deployment.

---

## Requirements

- Python 3.8+
- Poetry or pip for package management
- (Optional) Docker for containerized deployment


## Tech Stack:
•	Backend: FastAPI
•	Language: Python 3.10
•	Deployment: Docker + Render
•	CI/CD: GitHub Actions
•	Testing: Pytest


| Principle                  | How It's Followed                                                                                                 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **1. Codebase**            | A single Git repository (`main` branch), version controlled.                                                      |
| **2. Dependencies**        | Declared explicitly in `requirements.txt` and isolated using `venv` or Docker.                                    |
| **3. Config**              | Can use `.env` for config values (e.g., model names), separating config from code.                                |
| **4. Backing Services**    | No external services are hardcoded; can be extended with databases or cloud APIs as services.                     |
| **5. Build, Release, Run** | Docker supports clean separation of build (`Dockerfile`), release (image tagging), and run (container execution). |
| **6. Processes**           | The app runs as a stateless service using `uvicorn`, designed to scale horizontally.                              |
| **7. Port Binding**        | Binds to a port using `uvicorn` (`--port $PORT`), with dynamic port support on Render.                            |
| **8. Concurrency**         | FastAPI + `uvicorn` supports async requests and multiple workers for high concurrency.                            |
| **9. Disposability**       | Docker containers can be stopped and restarted easily without loss of state.                                      |
| **10. Dev/Prod Parity**    | Dev environment (local or Docker) matches production (Render deployment).                                         |
| **11. Logs**               | Render captures stdout logs; in development, logs stream to the terminal.                                         |
| **12. Admin Processes**    | One-off admin tasks (e.g., testing) can be run via CLI or `pytest`.                                               |


## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/note_summarizer.git
cd note_summarizer
````

2. Create and activate a virtual environment (recommended)

```bash
python -m venv noteenv
source noteenv/bin/activate  # On Windows use: noteenv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

2. Open your browser and visit

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI to test the API.

3. Example request to `/summarize/` endpoint

```json

{
  "text": "Long input text here..."
}
```

Response:

```json
{
  "summary": "Summarized text here..."
}
```

---

## Running Tests

Run tests with pytest:

```bash
pytest -s
```

---

## Docker (If done locally, install Docker first)

Build the Docker image:

```bash
docker build -t ai-note-summarizer .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 ai-note-summarizer
```

## Deployment on Render

### Project URL:
API Documentation: [AI Note Summarizer Docs for Testing and Demonstration ](https://ai-note-summarizer-lwwg.onrender.com/docs#/summarization/summarize_summarize__post)
            Main: [AI Note Summarizer on Render](https://ai-note-summarizer-lwwg.onrender.com/)

### Demo Video URL:
	Testing and App working Demonstration: [https://drive.google.com/file/d/1Z/view?usp=sharing](https://drive.google.com/file/d/1kLZmwkjtfk-ZOrH8LOUb9dlHrhtrPN6w/view?usp=drive_link)



---

## Project Structure

```
note_summarizer/
├── app/
│   ├── main.py
│   ├── summarizer.py
│   └── routers/
│       └── summarize.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── README.md
└── Dockerfile
```

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---
