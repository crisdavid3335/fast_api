from fastapi import FastAPI

app = FastAPI()
app.title = 'Mi app con platzi'
app.version = '0.0.1'

@app.get('/', tags=['home'])
def message():
    return 'Hola mundo'