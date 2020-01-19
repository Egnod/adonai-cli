import json

from . import CONFIG_FILE_PATH


class Config:
    def __setattr__(self, name, value):
        config = None

        with open(CONFIG_FILE_PATH, "r") as f:
            try:
                config = json.loads(f.read())

            except json.JSONDecodeError:
                config = {}

            config[name] = value

        with open(CONFIG_FILE_PATH, "w") as f:
            f.write(json.dumps(config))

    def __getattribute__(self, name):
        value = None

        with open(CONFIG_FILE_PATH, "rb") as f:
            config = json.loads(f.read())

            value = config.get(name)

            if value is None:
                raise AttributeError(f"config key {name} not found!")

        return value


config = Config()
