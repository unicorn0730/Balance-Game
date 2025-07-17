# LocalLLM-2

This project provides a simple web interface to interact with a local Large Language Model running via [Ollama](https://github.com/jmorganca/ollama). It now uses **FastAPI** for the backend and a minimal HTML frontend.

## Setup

1. Ensure that Ollama is installed and running. By default the API is accessible at `http://localhost:11434`.
2. Install the Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   uvicorn app:app --reload
   ```
   The server listens on port `8000` by default. You can set `PORT`, `OLLAMA_URL`, or `OLLAMA_MODEL` environment variables to customise behaviour.
4. Open `http://localhost:8000` in your browser to interact with the local LLM.

## Repository Rename

The original repository has been renamed to **LocalLLM-2** to reflect its purpose as an interface for a local LLM.
