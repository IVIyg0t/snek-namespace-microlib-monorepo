from setuptools import setup

setup(
    name="SnekCore",
    version="0.0.1",
    install_requires=["typer[all]"],
    packages=["cli", "Snek.SnekCore"],
    entry_points={
        "snek_types": ["simple = Snek.SnekCore.SimpleSnek:SimpleSnek"],
        "console_scripts": ["snek = cli.cli:app"],
    },
)
