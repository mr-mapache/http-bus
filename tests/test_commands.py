from httpbus.commands import Command
from httpbus.commands import Commands

commands = Commands()

@commands.register
class CreateUser(Command):
    id: int
    username: str

def test_commands():
    assert commands.map['CreateUser'] == CreateUser
    cmd = commands.build('CreateUser', {'id':1, 'username':'test'})
    assert cmd.username == 'test'
    assert isinstance(cmd, CreateUser)