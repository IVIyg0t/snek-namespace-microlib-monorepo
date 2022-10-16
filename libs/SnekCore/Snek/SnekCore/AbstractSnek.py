from abc import abstractmethod


class AbstractSnek:
    @abstractmethod
    def get_snek(self) -> str:
        """
        Returns the SKEW version.

        Args:
            self: write your description
        """
        pass
