from abc import abstractmethod


class AbstractSnek:
    @abstractmethod
    def get_snek(self) -> str:
        pass
