import psycopg2
import json


class ConnectDB():
    def __init__(self):
        self.info_db = self.get_info_db()
        self.conn = psycopg2.connect(**self.info_db)
        self.cur = self.conn.cursor()

    def config_app(self):
        path = os.getcwd() + "/config.txt"
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def get_info_db(self):
        info_db = self.config_app()['Data_Base']
        return info_db

    def query(self, request):
        self.cur.execute(request)
        self.conn.commit()

    def toyal(self):
        return self.cur.fetchall()

    def status(self):
        return self.cur.statusmessage

    def close(self):
        self.cur.close()
        self.conn.close()
   

class Use: 
    cursor = ConnectDB()

    @classmethod
    def get_users(cls):
        users = {'users': []}

        cls.cursor.query('SELECT * FROM Users')
        records = cls.cursor.toyal()
        for typles in records:
            user_name, user_secret = typles
            _ = dict()
            _['user_name'] = user_name
            _['user_secret'] = user_secret
            users['users'].append(_)
        return users

a = Use()
print(a.get_users())
