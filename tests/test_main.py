from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the AI Note Summarization API!"}

def test_summarize():
    test_data = {
        "text": (
            " "
            ""
        )
    }
    response = client.post("/summarize/", json=test_data)
    assert response.status_code == 200
    assert "summary" in response.json()
    assert isinstance(response.json()["summary"], str)


def test_summarize():
    input_data = {
        "text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. This is a test input to check the summarization functionality."
    }
    response = client.post("/summarize/", json=input_data)
    print("Response JSON:", response.json())  # <-- print the full response
    
    assert response.status_code == 200

    data = response.json()

    # Assert 'summarized_text' key exists and is a non-empty string
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0

    # Optional: If your API returns the original input text, assert it matches the input
    if "original_text" in data:
        assert data["original_text"] == input_data["text"]
