from Snek.SnekCore.AbstractSnek import Snek

CUTE_SNEK = r"""[green]
                    /^\/^\
                  _|__|  O|
         \/     /~     \_/ \
          \____|__________/  \
                 \_______      \
                         `\     \                 \
                           |     |                  \
                          /      /                    \
                         /     /                       \
                       /      /                         \ \
                      /     /                            \  \
                    /     /             _----_            \   \
                   /     /           _-~      ~-_         |   |
                  (      (        _-~    _--_    ~-_     _/   |
                   \      ~-____-~    _-~    ~-_    ~-_-~    /
                     ~-_           _-~          ~-_       _-~ 
                        ~--______-~                ~-___-~
[/green]"""


class CuteSnek(Snek):
    def get_snek(self) -> str:
        """
        Return the cute version of the string.

        Args:
            self: write your description
        """
        return CUTE_SNEK
