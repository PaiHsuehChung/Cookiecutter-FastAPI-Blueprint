# Build-in
from loguru import logger
# Customize
from config.settings import Settings

class BaseService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings