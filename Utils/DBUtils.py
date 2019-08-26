import psycopg2

def getPostgresConnection():
    return psycopg2.connect("dbname=postgres user=postgres password=docker")
