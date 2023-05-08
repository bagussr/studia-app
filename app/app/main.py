import uvicorn
from module import FastAPI, CORSMiddleware, StaticFiles, os

from app.routes.auth import router as AuthRouter
from app.routes.classes import router as ClassRouter
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

app.include_router(AuthRouter)
app.include_router(ClassRouter)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
