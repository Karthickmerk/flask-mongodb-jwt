import uuid

def make_id(api=None):
    if api:
        api = api[:-1]
        return api+'_'+uuid.uuid4().hex
