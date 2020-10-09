import json
str_json = '{"10": "qwe"}'


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

print(is_json(str_json))
