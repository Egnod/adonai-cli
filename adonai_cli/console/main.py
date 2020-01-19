from termcolor import colored

from adonai_client import AdonaiClient

from .. import CONFIG_FILE_PATH
from ..config import config
from .domain import DomainMenu
from .permission import PermissionMenu
from .project import ProjectMenu


class MainMenu:
    def __init__(self):
        self.domain = DomainMenu()
        self.permission = PermissionMenu()
        self.project = ProjectMenu()

    def login(self, root_endpoint: str, username: str, password: str):
        client = AdonaiClient(root_endpoint, username, password)

        config.username = username
        config.password = password
        config.root_endpoint = root_endpoint

        query = client.query()
        current_user_query = query.current_user()

        fields = ["first_name", "last_name", "login"]

        client.fields(current_user_query, **{field: True for field in fields})

        user = client.execute(query).current_user

        print(
            f"{colored('Hi!', 'green')} {user.first_name} {user.last_name} ({user.login}) you are loggined!",
            CONFIG_FILE_PATH,
        )

    def token(self):
        print(colored(config.token, "white", "on_red"))
