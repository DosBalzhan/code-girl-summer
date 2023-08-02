from fastapi import HTTPException, APIRouter
from users.schemas import CreateUserRequest,UpdateUserRequest

router = APIRouter()

users = {}

last_added_users_id = -1


@router.get('')
def get_user():
    return users


@router.post('/register')
def create_user(user: CreateUserRequest):
    global last_added_user_id
    new_user = last_added_user_id + 1
    users[new_user] = user
    last_added_user_id = new_user
    return new_user


@router.get('/{id}')
def get_users(id:int):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')
    return users[id]

@router.put('/{id')
def update_user(id: int, user_update: UpdateUserRequest):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')
    for key, value in user_update.dict().items():
        if value is not None:
            users[id][key] = value

    return users

@router.delete('/{id}')
def delete_user(id: int):
    if id not in users:
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

    del users[id]
    return id

