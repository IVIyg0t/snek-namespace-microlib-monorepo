import typer
import pkg_resources
from rich import print

app = typer.Typer()


def get_installed_sneks() -> dict:
    available_sneks = dict()
    for entry_point in pkg_resources.iter_entry_points("snek_types"):
        available_sneks[entry_point.name] = entry_point

    return available_sneks


@app.command()
def get(type: str, color: str = "green"):

    available_sneks = dict()
    for entry_point in pkg_resources.iter_entry_points("snek_types"):
        available_sneks[entry_point.name] = entry_point

    snek_cls = available_sneks[type].load()
    snek = snek_cls()
    print(snek.get_snek())


@app.command()
def types():
    sneks = get_installed_sneks()
    print(list(sneks.keys()))
    return list(sneks.keys())


if __name__ == "__main__":
    app()
