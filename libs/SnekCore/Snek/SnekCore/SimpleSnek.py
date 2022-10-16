from Snek.SnekCore.AbstractSnek import AbstractSnek

simple_snek = """[green]\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
[/green]"""


class SimpleSnek(AbstractSnek):
    def get_snek(self) -> str:
        """
        Returns the simple_snek string.

        Args:
            self: write your description
        """
        return simple_snek
