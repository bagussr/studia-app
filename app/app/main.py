import uvicorn
from module import FastAPI, CORSMiddleware, BaseModel, HTTPBearer, Depends

from app.routes.auth import router as AuthRouter


security = HTTPBearer()


app = FastAPI()

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


@app.get("/")
def root(token=Depends(security)):
    return "hellow"


app.include_router(AuthRouter)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
