import base64


def convert_string_base64(value: str) -> str:
    """Convert string to base64"""

    value64Encode = value.encode("ascii")
    base64Bytes = base64.b64encode(value64Encode)
    base64Decode = base64Bytes.decode("ascii")
    return base64Decode
