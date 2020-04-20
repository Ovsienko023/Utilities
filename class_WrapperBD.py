import psycopg2


class WrapperBD:
    def __init__(self, info_bd):
        self.conn = psycopg2.connect(**info_bd)
        self.cursor = self.conn.cursor()

    def select_all(self):
        reg = 'SELECT user_name, user_secret FROM Users'
        self.cursor.execute(reg)
        records = self.cursor.fetchall()
        return records

    def close(self):
        self.conn.close()
        self.cursor.close()
        
    

info_bd = {"dbname": "postgres", 
                    "user": "", 
                    "password": "", 
                    "host":"localhost"}

a = WrapperBD(info_bd)
print(a.select_all())
a.close()
