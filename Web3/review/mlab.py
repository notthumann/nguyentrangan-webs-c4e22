import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds035786.mlab.com:35786/c4e22-users

host = "ds035786.mlab.com"
port = 35786
db_name = "c4e22-users"
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