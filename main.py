from fastapi import FastAPI
from posts.router  import router as posts_router
from users.router import router as users_router 

app = FastAPI()
app.include_router(posts_router, prefix="/posts")
app.include_router(users_router, prefix = "/users")
