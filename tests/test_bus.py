from typing import Annotated
from httpbus.commands import Command
from httpbus.bus import HTTPBus
from httpbus.bus import Depends
from asyncio import run

bus = HTTPBus()
db = {}

class CreateUser(Command):
    id: int
    username: str

def get_db():
    return db

@bus.register
async def handle_create_user(command: CreateUser, users_db: Annotated[dict, Depends(get_db)]):
    users_db[command.id] = command.username

def test_bus():
    assert bus.command_handlers['CreateUser'] == handle_create_user
    run(bus.execute(CreateUser(id=1, username='test')))