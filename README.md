# LocalLLM-2

This project provides a simple web interface to interact with a local Large Language Model running via [Ollama](https://github.com/jmorganca/ollama) on your machine. It consists of a Python Flask backend and a minimal HTML frontend.

## Setup

1. Ensure that Ollama is installed and running on your Mac. By default the API is accessible at `http://localhost:11434`.
2. Create a Python environment and install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open `http://localhost:5000` in your browser to interact with the local LLM.

## Repository Rename

The original repository has been renamed to **LocalLLM-2** to reflect its new purpose as an interface for a local LLM instead of the previous balance game example.
