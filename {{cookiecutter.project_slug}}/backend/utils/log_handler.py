from loguru import logger
import sys

def log_formater(log_level: str) -> logger:
    logger.remove()
    logger.info(f"Initalize log formater - Log level: {log_level}")
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:MM:SS}</green> |<y>[{level}]</y> | <e>{file}::{function}::{line}</e> | {message}",
        filter="",
        level=log_level,
    )

    return logger
