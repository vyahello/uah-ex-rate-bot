from abc import ABC, abstractmethod
from typing import Dict, Any


class Message(ABC):
    """Abstraction for a message."""

    @abstractmethod
    def send(self) -> Dict[Any, Any]:
        pass


class Answer(ABC):
    """Abstraction for a answer."""

    @abstractmethod
    def chat_id(self) -> int:
        pass

    @abstractmethod
    def message(self) -> str:
        pass
