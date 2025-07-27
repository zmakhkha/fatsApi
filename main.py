from fastapi import FastAPI, HTTPException
from Shema import Blog
from database import create_db_and_models, engine
from contextlib import asynccontextmanager
from sqlmodel import Session, select

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("📦 STARTUP: Connecting to DB")
    create_db_and_models()
    yield
    print("🧹 SHUTDOWN: Closing DB connection")


app = FastAPI(lifespan=lifespan)

# Simple blog management API
@app.get("/all-blogs/")
def get_blogs():
	with Session(engine) as session:
		return session.exec(select(Blog)).all()

@app.get("/blog/{id}")
def get_blog(id: int):
	with Session(engine) as session:
		blog =  session.exec(select(Blog).where(Blog.id == id)).first()
		if not blog:
			raise HTTPException(status_code=404, detail="Blog not found")
		return blog

@app.post("/blog/", response_model=Blog)
def create_blog(blog: Blog):
	blog = Blog(title = blog.title, content= blog.content)
	with Session(engine) as session:
		session.add(blog)
		session.commit()
		session.refresh(blog)
		return blog

@app.put("/blog/")
def update_blog(blog: Blog):
	with Session(engine) as session:
		blog_db = session.exec(select(Blog).where(Blog.id == blog.id)).first()
		if not blog:
			raise HTTPException(status_code = 404, detail="Blog not found")
		
		blog_db.title = blog.title
		blog_db.content = blog.content

		session.add(blog_db)
		session.commit()
		session.refresh(blog_db)

		return blog_db

@app.delete("/blog/{id}")
def delete_blog(id: int):
	with Session(engine) as session:
		blog = session.exec(select(Blog).where(Blog.id == id)).first()
		if not blog:
			raise HTTPException(status_code=404, detail="Blog not found")
		session.delete(blog)
		session.commit()
		return {"detail": f"Blog with id {id} deleted successfully"}
