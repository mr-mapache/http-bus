from typing import Callable
from typing import Any
from pydantic import BaseModel
from pydantic import ConfigDict

class Command(BaseModel):
    model_config = ConfigDict(frozen=True)

class Commands:
    def __init__(self, key_generator: Callable[[str], str] = lambda name: name):
        self.key_generator = key_generator
        self.map = dict[str, type[Command]]()

    def register(self, command_type: type[Command]):
        key = self.key_generator(command_type.__name__)
        self.map[key] = command_type
        return command_type
    
    def build(self, action: str, payload: dict[str, Any]) -> Command:
        command_type = self.map[action]
        return command_type.model_validate(payload)