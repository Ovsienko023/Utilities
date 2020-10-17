import uuid


def gen_tokens():
    access_token = uuid.uuid4()
    refresh_token = uuid.uuid4()
    return (access_token, refresh_token)
