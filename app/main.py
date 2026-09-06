from fastapi import FastAPI, UploadFile
from agents.manager import Manager
from tools.loader import load_file
from tools.chunker import chunk_docs

app = FastAPI()
manager = Manager()

@app.post("/upload")
async def upload(file: UploadFile):
    path = f"data/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    docs = load_file(path)
    chunks = chunk_docs(docs)
    return {"msg": "uploaded"}

@app.post("/query")
def query(q: str, role: str):
    return {"response": manager.handle(q, role)}