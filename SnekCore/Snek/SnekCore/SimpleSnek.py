from Snek.SnekCore.AbstractSnek import Snek

SIMPLE_SNEK = """[green]\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
[/green]"""


class SimpleSnek(Snek):
    def get_snek(self) -> str:
        """
        Returns the simple_snek string.

        Args:
            self: write your description
        """
        return SIMPLE_SNEK
