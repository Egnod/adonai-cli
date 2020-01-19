from termcolor import colored

from adonai_client import AdonaiClient

from ..decorators import client_injection
from .utils import Defaults, get_arguments, get_fields_dict, get_table


class ProjectMenu:
    DEFAULT_FIELDS = ["id", "uuid", "domain_id", "name", "description", "is_active"]
    NO_INPUT = False

    @client_injection
    def all(self, client: AdonaiClient = None):
        query = client.query()

        client.fields(query.projects(), **get_fields_dict(self.DEFAULT_FIELDS))

        projects = client.execute(query, interpret=False)["projects"]

        if len(projects) == 0:
            print(colored("Empty!", "red"))
            return

        print(get_table(projects, self.DEFAULT_FIELDS))

    @client_injection
    def get(self, id: int, client: AdonaiClient = None):
        query = client.query()

        client.fields(query.get_project(id=id), **get_fields_dict(self.DEFAULT_FIELDS))

        project = client.execute(query, interpret=False)["getProject"]

        if project is None:
            print(colored("Not found!", "red"))
            return

        print(get_table(project, self.DEFAULT_FIELDS))

    @client_injection
    def create(
        self,
        name: str,
        domain_id: int,
        description: str = Defaults.NO_INPUT,
        client: AdonaiClient = None,
    ):
        mutation = client.mutation()

        args = get_arguments(name=name, description=description, domain_id=domain_id)
        client.fields(
            mutation.create_project(**args).project(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        project = client.execute(mutation, interpret=False)["createProject"]["project"]

        print(get_table(project, self.DEFAULT_FIELDS))

    @client_injection
    def update(
        self,
        id: int,
        name: str = Defaults.NO_INPUT,
        description: str = Defaults.NO_INPUT,
        client: AdonaiClient = None,
    ):
        mutation = client.mutation()

        args = get_arguments(name=name, description=description)
        client.fields(
            mutation.update_project(id=id, **args).project(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        project = client.execute(mutation, interpret=False)["updateProject"]["project"]

        print(get_table(project, self.DEFAULT_FIELDS))

    @client_injection
    def toggle(self, id: int, is_active: bool, client: AdonaiClient = None):
        mutation = client.mutation()

        args = get_arguments(is_active=is_active)
        client.fields(
            mutation.toggle_project(id=id, **args).project(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        project = client.execute(mutation, interpret=False)["toggleProject"]["project"]

        print(get_table(project, self.DEFAULT_FIELDS))

    @client_injection
    def domain(self, id: int, client: AdonaiClient = None):
        from .domain import DomainMenu

        query = client.query()

        client.fields(
            query.get_project(id=id).domain(),
            **get_fields_dict(DomainMenu.DEFAULT_FIELDS)
        )

        project = client.execute(query, interpret=False)["getProject"]

        if project is None:
            print(colored("Not found!", "red"))
            return

        domain = project["domain"]

        if domain is None:
            print(colored("Domain not found!", "red"))
            return

        print(get_table(domain, DomainMenu.DEFAULT_FIELDS))

    @client_injection
    def permissions(self, id: int, client: AdonaiClient = None):
        from .permission import PermissionMenu

        query = client.query()

        client.fields(
            query.get_project(id=id).permissions(),
            **get_fields_dict(PermissionMenu.DEFAULT_FIELDS)
        )

        project = client.execute(query, interpret=False)["getProject"]

        if project is None:
            print(colored("Not found!", "red"))
            return

        permissions = project["permissions"]

        print(get_table(permissions, PermissionMenu.DEFAULT_FIELDS))
