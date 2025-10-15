from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserEntity:
    name: str
    age: int
    gender: str
    id: Optional[int] = None
