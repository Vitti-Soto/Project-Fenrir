from setuptools import setup, find_packages
import os


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name="Project Fenrir",
    version="0.0.1",
    author=["Victor Sotomayor Monroy, Michel Gonzalez, Barry Congressi, Bryan Kristofferson, Roberto Rafael Edde Verde"],
    author_email="victor@ufl.edu",
    description="A fantasy turn-based role-playing game",
    long_description=read('README.md'),
    lisence="MIT",
    url="https://github.com/Mgonzalez-droid/Project-Fenrir",
    packages=find_packages(),
    install_requires=["pygame"],
    entry_points={
        "console_scripts":
            [
                "play_fenrir=fenrir.app:run"
            ]
    }
)
