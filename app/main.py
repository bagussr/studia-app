import uvicorn
from app.module import FastAPI, CORSMiddleware, StaticFiles, os, Response

from app.routes.auth import router as AuthRouter
from app.routes.classes import router as ClassRouter


app = FastAPI()

STATIC_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app.mount("/static", StaticFiles(directory=STATIC_FILE), name="static")


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


@app.get("/")
def root():
    return Response(
        """
            <div style="padding:10px">
                <h1> FastAPI Application </h1>
                <hr></hr>
                <p> Welcome to API for Studia Application, for the documentation please enter this url <a href="/docs">docs</a> </p>
            </main>
        """
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
