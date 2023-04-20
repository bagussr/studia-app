import uvicorn
from module import FastAPI, CORSMiddleware, BaseModel, StaticFiles, os

from app.routes.auth import router as AuthRouter
from app.service.auth.jwt import LoginRequired


app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    username: str
    hostname: str


@app.get("/", response_model=None)
def root(auth: LoginRequired):
    return "hellow"


app.include_router(AuthRouter)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
