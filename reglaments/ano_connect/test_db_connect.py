import psycopg2

host = '127.0.0.1'
user = 'postgres'
name = 'ano_rsi_db'
pw = 'Cib3jj7yz123'

connection = psycopg2.connect(
    host=host,
    database=name,
    password=pw,
    user=user
)

print(connection.cursor().execute("""SELECT version()"""))