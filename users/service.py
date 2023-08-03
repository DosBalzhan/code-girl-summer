from users.schemas import CreateUserRequest, UpdateUserRequest
from sqlalchemy import insert,select,update,delete
from database import users as users_table
from database import database
from fastapi import HTTPException

# CREATE user REQUEST 
async def create_user(user:CreateUserRequest):
    insert_query = insert(users_table).values (

        user.dict() 
    ).returning(users_table.columns.id)

    return await database.fetch_one(insert_query)

async def get_users():
   # select_query = 'SELECT * FROM users'
    select_query = select(users_table)

    return await database.fetch_all(select_query)
# GET user BY ID 
async def get_user_by_id(user_id:int):
    select_query = select(users_table).where(users_table.columns.id == user_id)

    user = await database.fetch_one(select_query)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user 

# EDIT user
async def edit_user(user_id: int, user:UpdateUserRequest):
    user_db = await get_user_by_id(id)
    if not user_db:
        raise HTTPException(status_code=404, detail="user not found")
    
    #Update users set, content = 'content'
    update_query = update(users_table).values(user.dict(exclude_none=True)).where(users_table.columns.id == user.id).returning(users_table)
    return await database.fetch_one(update_query)

# DELETE user
async def delete_user(user_id:int):

    user_delete = await delete_user(id)
    if not user_delete:
        raise HTTPException(status_code=404, detail="ppst not found")
    
    delete_query = delete(users_table).where(users_table.columns.id == user_id)
    return await database.execute(delete_query)