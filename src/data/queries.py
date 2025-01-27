import json
import psycopg2
from config import config

def query_person():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = 'SELECT * FROM person;'
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_create_person(name:str, age: int, student:bool):
    command=(
        """
        INSERT INTO person (name, age, student) VALUES (%s, %s, %s);
        """)
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (name,age,student))
                conn.commit()
                result = {"success": "created person name: %s " % name}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
            print(error) 

def db_delete_person(id:int):
    command=(
        """
        DELETE FROM person WHERE id = %s;
        """)
    try:
        with psycopg2.connect(**config()) as conn:
            with conn.cursor() as cur:
                cur.execute(command, (int(id),)) 
                conn.commit()
                result = {"success": "deleted person id: %s " % id}
                return json.dumps(result)
    except (psycopg2.DatabaseError, Exception) as error:
            print(error) 

if __name__ == '__main__':
    query_person()
    #print(db_create_person('John Doe', 32, True))
    #print(db_delete_person(7))