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
        return simple_snek
