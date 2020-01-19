from termcolor import colored

from adonai_client import AdonaiClient

from ..decorators import client_injection
from .utils import Defaults, get_arguments, get_fields_dict, get_table


class DomainMenu:
    DEFAULT_FIELDS = ["id", "uuid", "name", "description", "is_active"]
    NO_INPUT = False

    @client_injection
    def all(self, client: AdonaiClient = None):
        query = client.query()

        client.fields(query.domains(), **get_fields_dict(self.DEFAULT_FIELDS))

        domains = client.execute(query, interpret=False)["domains"]

        print(get_table(domains, self.DEFAULT_FIELDS))

    @client_injection
    def get(self, id: int, client: AdonaiClient = None):
        query = client.query()

        client.fields(query.get_domain(id=id), **get_fields_dict(self.DEFAULT_FIELDS))

        domain = client.execute(query, interpret=False)["getDomain"]

        if domain is None:
            print(colored("Not found!", "red"))
            return

        print(get_table(domain, self.DEFAULT_FIELDS))

    @client_injection
    def create(
        self,
        name: str,
        description: str = Defaults.NO_INPUT,
        client: AdonaiClient = None,
    ):
        mutation = client.mutation()

        args = get_arguments(name=name, description=description)
        client.fields(
            mutation.create_domain(**args).domain(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        domain = client.execute(mutation, interpret=False)["createDomain"]["domain"]

        print(get_table(domain, self.DEFAULT_FIELDS))

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
            mutation.update_domain(id=id, **args).domain(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        domain = client.execute(mutation, interpret=False)["updateDomain"]["domain"]

        print(get_table(domain, self.DEFAULT_FIELDS))

    @client_injection
    def toggle(self, id: int, is_active: bool, client: AdonaiClient = None):
        mutation = client.mutation()

        args = get_arguments(is_active=is_active)
        client.fields(
            mutation.toggle_domain(id=id, **args).domain(),
            **get_fields_dict(self.DEFAULT_FIELDS)
        )

        domain = client.execute(mutation, interpret=False)["toggleDomain"]["domain"]

        print(get_table(domain, self.DEFAULT_FIELDS))

    @client_injection
    def projects(self, id: int, client: AdonaiClient = None):
        from .project import ProjectMenu

        query = client.query()

        client.fields(
            query.get_domain(id=id).projects(),
            **get_fields_dict(ProjectMenu.DEFAULT_FIELDS)
        )

        domain = client.execute(query, interpret=False)["getDomain"]

        if domain is None:
            print(colored("Not found!", "red"))
            return

        projects = domain["projects"]

        print(get_table(projects, ProjectMenu.DEFAULT_FIELDS))
