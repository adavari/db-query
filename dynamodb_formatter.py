def dict_to_dynamodb(raw_dict: dict) -> dict:
    out = {}
    for k, v in raw_dict.items():
        if isinstance(v, str):
            out[k] = {'S': v}
        if isinstance(v, int):
            out[k] = {'N': v}
        if isinstance(v, bool):
            out[k] = {'BOOL': v}
    return out
