import re
from pydantic import BaseConfig as PydanticBaseConfig


def snake2camel(snake: str, start_lower: bool = True) -> str:
    """
    Converts a snake_case string to camelCase.
    The `start_lower` argument determines whether the first letter in the generated camelcase should
    be lowercase (if `start_lower` is True), or capitalized (if `start_lower` is False).
    """
    camel = snake.title()
    camel = re.sub("([0-9A-Za-z])_(?=[0-9A-Z])", lambda m: m.group(1), camel)
    if start_lower:
        camel = re.sub("(^_*[A-Z])", lambda m: m.group(1).lower(), camel)
    return camel


class BaseConfig(PydanticBaseConfig):
    alias_generator = snake2camel
    allow_population_by_field_name = True
