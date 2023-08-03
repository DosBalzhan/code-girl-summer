from users.schemas import CreateUserRequest, UpdateUserRequest
from fastapi import HTTPException, APIRouter
from users import service 
import time 

router = APIRouter()


@router.get('')
async def get_users():
   return await service.get_users()

@router.post('')
async def create_user(user: CreateUserRequest):
    return await service.create_user(user)



@router.get('/{id}')
async def get_users(id: int):
     return await service.get_user_by_id(id)


@router.put('/{id}')
async def edit_user(id: int, user_data: UpdateUserRequest):
    return await service.edit_user(id,user_data)



@router.delete('/{id}')
async def delete_user(id: int):
    await service.delete_user(id)
    
    return {"message":"ok,deleted"}