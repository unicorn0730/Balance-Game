import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx
import uvicorn

app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.getenv("OLLAMA_MODEL", "mistral")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.post("/ask")
async def ask(data: dict):
    prompt = data.get("prompt", "")
    payload = {"model": MODEL, "prompt": prompt, "stream": False}

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(OLLAMA_URL, json=payload)
            resp.raise_for_status()
            answer = resp.json().get("response", "")
        except Exception as e:
            raise HTTPException(
                status_code=502, detail=f"Error contacting LLM: {e}"
            ) from e

    return {"response": answer}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
