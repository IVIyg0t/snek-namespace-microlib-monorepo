from setuptools import setup

setup(
    name="FancySnek",
    version="0.0.1",
    install_requires=[],
    packages=["Snek.FancySnek"],
    entry_points={"snek_types": ["fancy = Snek.FancySnek.FancySnek:FancySnek"]},
)
