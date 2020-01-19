from termcolor import colored

from adonai_client import AdonaiClient

from ..decorators import client_injection
from .utils import Defaults, get_arguments, get_fields_dict, get_table


class PermissionMenu:
    DEFAULT_FIELDS = ["id", "project_id", "name", "description", "type", "is_active"]
    NO_INPUT = False

    @client_injection
    def all(self, client: AdonaiClient = None):
        query = client.query()

        client.fields(query.permissions(), **get_fields_dict(self.DEFAULT_FIELDS))

        permissions = client.execute(query, interpret=False)["permissions"]

        print(get_table(permissions, self.DEFAULT_FIELDS))

    @client_injection
    def get(self, id: int, client: AdonaiClient = None):
        query = client.query()

        client.fields(
            query.get_permission(id=id), **get_fields_dict(self.DEFAULT_FIELDS)
        )

        permission = client.execute(query, interpret=False)["getPermission"]

        if permission is None:
            print(colored("Not found!", "red"))
            return

        print(get_table(permission, self.DEFAULT_FIELDS))

    @client_injection
    def create(
        self,
        name: str,
        type: str,
        project_id: int = Defaults.NO_INPUT,
        description: str = Defaults.NO_INPUT,
        client: AdonaiClient = None,
    ):
        mutation = client.mutation()

        args = get_arguments(
            name=name, description=description, type=type, project_id=project_id
        )
        client.fields(
            mutation.create_permission(**args).permission(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        permission = client.execute(mutation, interpret=False)["createPermission"][
            "permission"
        ]

        print(get_table(permission, self.DEFAULT_FIELDS))

    @client_injection
    def update(
        self, id: int, description: str = Defaults.NO_INPUT, client: AdonaiClient = None
    ):
        mutation = client.mutation()

        args = get_arguments(description=description)
        client.fields(
            mutation.update_permission(id=id, **args).permission(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        permission = client.execute(mutation, interpret=False)["updatePermission"][
            "permission"
        ]

        print(get_table(permission, self.DEFAULT_FIELDS))

    @client_injection
    def toggle(self, id: int, is_active: bool, client: AdonaiClient = None):
        mutation = client.mutation()

        args = get_arguments(is_active=is_active)
        client.fields(
            mutation.toggle_permission(id=id, **args).permission(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        permission = client.execute(mutation, interpret=False)["togglePermission"][
            "permission"
        ]

        print(get_table(permission, self.DEFAULT_FIELDS))

    @client_injection
    def project(self, id: int, client: AdonaiClient = None):
        from .project import ProjectMenu

        query = client.query()

        client.fields(
            query.get_permission(id=id).project(),
            **get_fields_dict(ProjectMenu.DEFAULT_FIELDS)
        )

        permission = client.execute(query, interpret=False)["getPermission"]

        if permission is None:
            print(colored("Not found!", "red"))
            return

        project = permission["project"]

        if project is None:
            print(colored("Project is None!", "red"))
            return

        print(get_table(project, ProjectMenu.DEFAULT_FIELDS))
