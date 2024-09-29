from dataclasses import dataclass
from typing import Protocol


@dataclass
class Id[T]:
    value: T


class Repository(Protocol):
    def show_tables(self) -> list[str]: ...
    # CRUD operations
    # def create(self, item: object) -> None: ...
    def read(self, id: Id) -> object: ...

    # def update(self, id: Id, item: object) -> None: ...
    # def delete(self, id: Id) -> None: ...
