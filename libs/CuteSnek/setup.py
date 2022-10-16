from setuptools import setup

setup(
    name="CuteSnek",
    version="0.0.1",
    install_requires=[],
    packages=["Snek.CuteSnek"],
    entry_points={"snek_types": ["cute = Snek.CuteSnek.CuteSnek:CuteSnek"]},
)
