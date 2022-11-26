from fastapi import FastAPI
from routing import api, update, delete
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
app.include_router(update.router)
app.include_router(delete.router)


@app.get('/')
def home():
    return 'You are Home =)'
