# using a uv package it make by rust
# pip install uv

# pip install fastapi
# pip imstall fastapi uvicorn

# for uv package all packages-speed very very fast working

from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get('/')
def home():
    return {'data':'welcome to home page'}

@app.get('/contact')
def contact():
    return {'data':'welcome to contact page'}

# pip install python-multipart
@app.post('/upload')
def handleImage(files: list[UploadFile]):
    print(files)
    return {'status': 'got the file'}

import uvicorn
uvicorn.run(app)