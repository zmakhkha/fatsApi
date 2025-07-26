from sqlmodel import SQLModel, create_engine

from sqlalchemy.orm import sessionmaker



sql_file_name = "blog.db"
sqlite_url = f"sqlite:///{sql_file_name}"

connect_args = {
	"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_models():
	SQLModel.metadata.creatall(engine)

Session = sessionmaker(bind=engine)

def get_session():
	with Session(engine) as session:
		yield session
	