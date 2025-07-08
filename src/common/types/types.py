from typing import Union


JsonPrimitive = Union[str, int, float, bool, None]
JsonType = Union[JsonPrimitive, list["JsonType"], dict[str, "JsonType"]]