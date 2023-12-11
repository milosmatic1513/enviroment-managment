from default import config as default_config
from dev import config as dev_config
from prod import config as prod_config
from env import config as envs
import os

environment = os.environ.get('PYTHON_ENV') or 'dev'
environment_config = None
if environment == 'dev':
    environment_config = dev_config
if environment == 'prod':
    environment_config = prod_config

priorities = {1: environment_config, 2: envs, 3: default_config}

config = {**priorities[3], **priorities[2], **priorities[1]}