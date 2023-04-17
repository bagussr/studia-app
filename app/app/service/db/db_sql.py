from app.module import declarative_base, create_engine, sessionmaker, Session, Annotated, Depends

engine = create_engine("postgresql+psycopg2://postgres:dadasdudus12@localhost/studia")

Base = declarative_base()

LocalSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = LocalSession()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()


Db = Annotated[Session, Depends(get_db)]
