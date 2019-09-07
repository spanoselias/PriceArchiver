import psycopg2


def getPostgresConnection():
    return psycopg2.connect("dbname=postgres user=postgres password=docker")

def executeSelectQuery(conn, query, constructorObj):
    # create a cursor
    cur = conn.cursor()

    cur.execute(query)
    resutSet = cur.fetchall()

    return collectResults(resutSet, constructorObj)

def collectResults(resutSet, constructorObj):
    streamList = []
    for rs in resutSet:
        obj = constructorObj(rs)
        streamList.append(obj)

    return streamList
