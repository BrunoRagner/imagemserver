from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.responses import FileResponse
from deta import Deta
import json









@app.get("/lista")
def list():
    lis = drive.list()
    return lis


#formu
@app.get("/", response_class=HTMLResponse)
def render():
    return FileResponse('files/index.html')


#endpont retorno de formulario
@app.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

#endpont retorno de objeto
@app.get("/download/{name}")
def buscar_img(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="image/png")



# endpont excluir de objeto
@app.delete("/excluir/{name}")
def delete_img(name: str):
    ress = drive.delete(name)
    return ress























