from posts.schemas import CreatePostRequest, EditPostRequest
from sqlalchemy import insert,select,update,delete
from database import posts as posts_table
from database import database
from fastapi import HTTPException

# CREATE POST REQUEST 
async def create_post(post:CreatePostRequest):
    # insert_query = f'INSERT INTO posts (title, content, author, location) VALUES (\'{post.title}\', \'{post.content}\', \'{post.author}\', \'{post.location}\')'
    insert_query = insert(posts_table).values (

        post.dict() 
        # title=post.title,
        # content=post.content,
        # author=post.author,
        # location=post.location
        #post.dict()
    ).returning(posts_table.columns.id)

    return await database.fetch_one(insert_query)

async def get_posts():
   # select_query = 'SELECT * FROM posts'
    select_query = select(posts_table)

    return await database.fetch_all(select_query)
# GET POST BY ID 
async def get_post_by_id(post_id:int):
    select_query = select(posts_table).where(posts_table.columns.id == post_id)

    post = await database.fetch_one(select_query)
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    return post 

# EDIT POST 
async def edit_post(post_id: int, post:EditPostRequest):
    post_db = await get_post_by_id(id)
    if not post_db:
        raise HTTPException(status_code=404, detail="ppst not found")
    
    #Update posts set, content = 'content'
    update_query = update(posts_table).values(post.dict(exclude_none=True)).where(posts_table.columns.id == post.id).returning(posts_table)
    return await database.fetch_one(update_query)

# DELETE POST 
async def delete_post(post_id:int):

    post_delete = await delete_post(id)
    if not post_delete:
        raise HTTPException(status_code=404, detail="ppst not found")
    
    delete_query = delete(posts_table).where(posts_table.columns.id == post_id)
    return await database.execute(delete_query)