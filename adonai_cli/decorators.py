import functools

from termcolor import colored

from adonai_client import AdonaiClient

from .config import config


def client_injection(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            client = AdonaiClient(
                config.root_endpoint, config.username, config.password
            )

        except AttributeError:
            print(
                f"You are not loggined. Please execute {colored('login', 'blue')} command!"
            )

        return func(*args, **kwargs, client=client)

    return wrapped
