import os

__version__ = "0.0.1"

CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "config.json"
)


def main():
    from fire import Fire

    from .console.main import MainMenu

    Fire(MainMenu)
