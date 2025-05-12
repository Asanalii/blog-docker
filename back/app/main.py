from fastapi import FastAPI, HTTPException
from app import crud

app = FastAPI()

@app.get("/api/posts")
# @app.get("/posts")
def get_posts():
    return crud.get_all_posts()

@app.post("/api/posts")
# @app.post("/posts")
def create_post(post: dict):
    return crud.create_post(post)

@app.delete("/api/posts/{post_id}")
# @app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    success = crud.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"deleted": True}

@app.put("/api/posts/{post_id}")
# @app.put("/posts/{post_id}")
def update_post(post_id: str, post: dict):
    success = crud.update_post(post_id, post)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"updated": True}
