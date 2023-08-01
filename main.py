from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

posts = {
    0: {
        'title': 'My trip to Spain',
        'content': 'Today I was in Madrid',
        'author': 'Dos Balzhan',
        'location': 'Barcelona'
    },
    1: {
        'title': 'My trip to Korea',
        'content': 'Today I was in Seoul',
        'author': 'Honeeey',
        'location': 'Seoul'
    },
    2: {
        'title': 'My trip to France',
        'content': 'Today I was in Paris',
        'author': 'Emily',
        'location': 'Paris'
}
 }
users = {
    0: {
        'username': 'Kkana',
        'name': 'Kanat',
        'surname': 'Kadirov',
        'age': 20,
        'gender': 'male'
    },
    1: {
        'username': 'honeey',
        'name': 'Elena',
        'surname': 'Pavlova',
        'age': 19,
        'gender': 'female'
    }

}
last_added_post_id = 0

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str
    location: str

class EditPostRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    location: Optional[str] = None

class CreateUserRequest(BaseModel):
    username: str
    name: str
    surname: str
    age: int
    gender: str
class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None

#USERS

@app.get('/')
def read_root():
    html_content = "<h2>Travel Blog Backend App!</h2>"
    return HTMLResponse(content=html_content)

@app.get('/users')
def get_user():
    return users


@app.post('/register')
def create_user(user: CreateUserRequest):
    global last_added_user_id
    new_id = last_added_user_id + 1
    users[new_id] = user
    last_added_user_id = new_id
    return new_id


@app.get('/user/{id}')
def get_users(id:int):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')
    return users[id]

@app.put('/user/{id')
def update_user(id: int, user_update: UpdateUserRequest):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')
    for key, value in user_update.dict().items():
        if value is not None:
            posts[id][key] = value

    return users

@app.delete('/user/{id}')
def delete_user(id: int):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

    del users[id]
    return id



#POSTS

@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def create_post(post: CreatePostRequest):
    global last_added_post_id
    new_id = last_added_post_id + 1
    posts[new_id] = post
    last_added_post_id = new_id
    return new_id


@app.get('/post/{id}')
def get_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    return posts[id]


@app.put('/post/{id}')
def edit_post(id: int, post: EditPostRequest):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    for key, value in post.dict().items():
        if value is not None:
            posts[id][key] = value

    return id

@app.delete('/post/{id}')
def edit_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    del posts[id]

    return id
