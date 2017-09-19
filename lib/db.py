from flaskext.mysql import MySQL


class MysqlDB():

    def get_connection(self, app, config):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = config['username']
        app.config['MYSQL_DATABASE_PASSWORD'] = config['pass']
        app.config['MYSQL_DATABASE_DB'] = config['db']
        app.config['MYSQL_DATABASE_HOST'] = config['host']
        self.mysql.init_app(app)

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def update_query(self, query):
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            conn.close()
            return 1
        except Exception, e:
            print e
            return 0

    def query(self, query):
        try:
            conn = self.mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            conn.commit()
            conn.close()
            return data
        except Exception, e:
            print e
            return 0
