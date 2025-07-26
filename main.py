from fastapi import FastAPI
from Shema import Blog
from database import create_db_and_models


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_models()

# Simple blog management API
@app.get("/all-blogs/")
def get_blogs():
	return {"data": "Those are all the blogs"}

@app.get("/blog/{id}")
def get_blog(id: int):
	return {"data": f"This is blog with id {id}"}

@app.post("/blog/")
def create_blog(blog: Blog):
	return {"title": blog.title, "Content": blog.content}

@app.put("blog/{id}")
def update_blog(id: int, blog: Blog):
	return {"id": id, "title": blog.title, "content": blog.content}

@app.delete("/blog/{id}")
def delete_blog(id: int):
	return {"message": f"Blog with id {id} has been deleted"}

@app.patch("/blog/{id}")
def patch_blog(id: int, blog: Blog):
	return {"id": id, "title": blog.title, "content": blog.content}


# Comments related to blogs API
@app.get("/blog/{id}/comments")
def get_blog_comments(id: int):
	return {"data": f"These are comments for blog with id {id}"}