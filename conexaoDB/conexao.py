import psycopg2 as pg


def conectadb(porta, acao):
    try:
        print(porta)
        connection = pg.connect(user="myuser", password="mypassword", host="localhost", port=porta, database="alarme")
        curs = connection.cursor()

        sql_insert = "INSERT INTO alarme VALUES (default, %s);"
        curs.execute(sql_insert, (acao,))
        connection.commit()

        connection.close()
    except (pg.Error, Exception) as error:
        print(f"Erro ao conectar ou inserir no banco de dados: {error}")