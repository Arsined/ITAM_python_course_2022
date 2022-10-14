def key_difference(dict1: dict, dict2: dict) -> dict:
    out = {}
    for key, value in dict1.items():
        if key in dict2:
            if dict2[key] == value:
                out[key] = "equal"
            else:
                out[key] = "changed"
        else:
            out[key] = "deleted"
    for key, value in dict2.items():
        if key not in dict1:
            out[key] = "added"
    return out


d1 = {"a": "b", "b": "a", "d": "f"}
d2 = {"a": "b", "b": "e", "c": "a"}
print(key_difference(d1, d2))
