from  fastapi import FastAPI,File, UploadFile,Form,Request
from fastapi.responses import FileResponse
import uvicorn
from tinydb import TinyDB,Query
import uuid
import os
from pydantic import BaseModel




notes = TinyDB("db/notes.json")
ext = TinyDB("db/notes_extention.json")

app = FastAPI()


@app.get("/")
def index():
    return "this is repeats backend api server"

@app.get("/api/list-notes")
def list_notes():
    return notes.all()


@app.post("/api/upload-notes")
def notes_upload(request: Request,flash:list = Form(...),qna:list = Form(...), file: UploadFile = File(...),title: str = Form(...)):
    
    _,x = os.path.splitext(file.filename)
    id = str(uuid.uuid4().hex)
    host = request.base_url
    name = id+x

    with open(f"storage/{name}", "wb") as buffer:
        buffer.write(file.file.read())

    pattern_notes = {
        "title":title,
        "id":id,
        "noFlash":(flash),
        "noQ":(qna),
        "file":name,
        "embeedURL":f"{host}api/embeed-notes?id={name}"

    }

    pattern_ext = {
        "title":title,
        "id":id,
        "flash":flash,
        "qna":qna
    }
    
    ext.insert(pattern_ext)
    notes.insert(pattern_notes)    
    
    return {"data":[pattern_ext,pattern_notes]}

@app.get("/api/embeed-notes")
async def download_notes(id: str):
    pathFile = "storage/"+id
    return FileResponse(pathFile, filename=id)

@app.get("/api/embeed-ext")
async def notes_ext(id: str,type:str):

    notes = Query()
    notes_ext = ext.search(notes.id == id)
    if type == "qna":
        pattern_ext = {
            "title":notes_ext[0]['title'],
            "id":id,
            "qna":notes_ext[0]['qna']
        }
        return pattern_ext
    
    elif type == "flash":
        pattern_ext = {
            "title":notes_ext[0]['title'],
            "id":id,
            "flash":notes_ext[0]['flash']
        }
        return pattern_ext
    
    elif type == "all":
        pattern_ext = {
            "title":notes_ext[0]['title'],
            "id":id,
            "qna":notes_ext[0]['qna'],
            "flash":notes_ext[0]['flash']
        }
        return pattern_ext
    
    return {"data":"give me something"}









if __name__=="__main__":
    uvicorn.run(app=app)