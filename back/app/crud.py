from pymongo import MongoClient
from bson import ObjectId
import os

# Set your connection string
# MONGO_URI = "mongodb+srv://testa:asan1234@test.wr2lcrn.mongodb.net/?retryWrites=true&w=majority&appName=test"
MONGO_URI = "mongodb+srv://testa:asan1234@test.wr2lcrn.mongodb.net/?retryWrites=true&w=majority&appName=test&tls=true&tlsAllowInvalidCertificates=true"


client = MongoClient(MONGO_URI)

db = client["blogdb"]
collection = db["posts"]

def get_all_posts():
    posts = []
    for doc in collection.find():
        posts.append({
            "id": str(doc["_id"]),
            "title": doc["title"],
            "content": doc["content"]
        })
    return posts


def create_post(post: dict):
    result = collection.insert_one(post)
    return {
        "id": str(result.inserted_id),
        "title": post["title"],
        "content": post["content"]
    }


def delete_post(post_id: str):
    result = collection.delete_one({"_id": ObjectId(post_id)})
    return result.deleted_count == 1

def update_post(post_id: str, updated_post: dict):
    result = collection.update_one(
        {"_id": ObjectId(post_id)},
        {"$set": updated_post}
    )
    return result.modified_count == 1
