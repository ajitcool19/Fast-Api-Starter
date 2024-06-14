def to_camel_case(string: str) -> str:
    components = string.split('_')
    return components[0] + ''.join(_.capitalize() for _ in components[1:])
