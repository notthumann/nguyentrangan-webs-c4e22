import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds249123.mlab.com:49123/c4e22-pol

host = "ds249123.mlab.com"
port = 49123
db_name = "c4e22-pol"
user_name = "xero0696"
password = "minhngoc123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())