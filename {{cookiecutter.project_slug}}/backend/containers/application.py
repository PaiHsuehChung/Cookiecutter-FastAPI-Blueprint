# Build-In
from dependency_injector import containers, providers

# Utils
from utils.log_handler import log_formater


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()
    logger = providers.Resource(log_formater, config.log_level)


class Services(containers.DeclarativeContainer):
    config = providers.Configuration()


class Application(containers.DeclarativeContainer):
    config = providers.Configuration()
    core = providers.Container(Core, config=config)
    services = providers.Container(Services, config=config)
