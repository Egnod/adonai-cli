#  Adonai CLI

Adonai console frontend based on [Fire](https://github.com/google/python-fire) and [Adonai Client](https://github.com/Egnod/adonai-client). PREALPHA

##  Prealpha components

Currently in pre alpha realized: project, permission, domain and they relation commands, user and groups comming soon.

##  Prepare  on prealpha :)

```bash
git clone git@github.com:Egnod/adonai-cli.git
cd adonai-cli
poetry install
```

## Use examples

### Login

```bash
python3 -m adonai_cli login --root_endpoint http://localhost:5000 --username admin --password admin
```
P.S.: http://localhost:5000 as example

###  Get all domains
```bash
python3 -m adonai_cli domain all

┌────┬──────────────────────────────────────┬──────┬─────────────┬───────────┐
│ id │ uuid                                 │ name │ description │ is_active │
╞════╪══════════════════════════════════════╪══════╪═════════════╪═══════════╡
│ 1  │ 00000000-0000-0000-0000-000000000000 │ Base │ None        │ True      │
├────┼──────────────────────────────────────┼──────┼─────────────┼───────────┤
│ 34 │ 2bedc130-1d2b-4fba-bcfd-05750cbae17e │ test │             │ True      │
└────┴──────────────────────────────────────┴──────┴─────────────┴───────────┘
```

###  Create domain
```bash
python3 -m adonai_cli domain create --name test --description test
┌────┬──────────────────────────────────────┬──────┬─────────────┬───────────┐
│ id │ uuid                                 │ name │ description │ is_active │
╞════╪══════════════════════════════════════╪══════╪═════════════╪═══════════╡
│ 36 │ 31920caa-ad63-44e3-b1aa-54f868be9f5c │ test │ test        │ True      │
└────┴──────────────────────────────────────┴──────┴─────────────┴───────────┘
```

###  Help
```bash
python3 -m adonai_cli domain --help
```
You will see man for domain comands group


