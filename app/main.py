from fastapi import FastAPI, UploadFile, File
from uuid import uuid4
import os


app= FastAPI()
UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    document_id=str(uuid4())
    filepath=os.path.join(UPLOAD_DIR, f"{document_id}_{file.filename}")

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "document_id": document_id,
        "filepath": filepath,
        "created_at": os.path.getctime(filepath),
        "message": "File uploaded successfully"
        }
