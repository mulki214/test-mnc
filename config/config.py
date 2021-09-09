from config.db import connection

APP_SECRET_KEY = "asdgasdgasd%&&$$$asdfasdf"


conn = connection.get_database('Cluster0')
mainDB = conn.test_rest