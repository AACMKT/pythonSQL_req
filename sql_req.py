import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tables(base, name, password):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS  clients(
                       client_id int generated always as identity PRIMARY KEY,
                       first_name text NOT NULL,
                       last_name text NOT NULL,
                       mail varchar(32) UNIQUE CHECK (mail LIKE '%@%.%') NOT NULL);
            """)
            conn.commit()

            cur.execute("""
            CREATE TABLE IF NOT EXISTS  phones(
                       phone_num_id int generated always as identity PRIMARY KEY,
                       client_id int REFERENCES  clients(client_id),
                       phone_num varchar(24) NOT NULL UNIQUE);
            """)
            conn.commit()
    conn.close()


def insert_data(base, name, password, first_name, last_name, mail):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO clients(first_name, last_name, mail) VALUES(%s, %s, %s);""", (first_name, last_name, mail))
            conn.commit()


def insert_phone(base, name, password, first_name, mail, phone_num):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO phones(client_id, phone_num) VALUES
            ((SELECT client_id FROM clients	WHERE first_name = %s AND mail = %s), %s);
            """, (first_name, mail, phone_num))
            conn.commit()


def edit_client_data(base, name, password, client_id, mail, first_name, last_name):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""UPDATE clients SET
             first_name = %s,
             last_name = %s,
             mail = %s
             WHERE client_id = %s;
             """, (first_name, last_name, mail, client_id))
            conn.commit()


def edit_phone_num(base, name, password, phone_num_id, phone_num):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""UPDATE phones SET
             phone_num = %s
             WHERE phone_num_id = %s;
             """, (phone_num, phone_num_id))
            conn.commit()


def get_clients(base, name, password):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM clients;
            """)
            return cur.fetchall()


def get_records(base, name, password):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT client_id, first_name, last_name, mail, phone_num FROM clients
            LEFT JOIN phones USING(client_id)
            ORDER BY first_name;
            """)
            return cur.fetchall()


def get_by_mail(base, name, password, mail, i):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT client_id, first_name, last_name FROM clients WHERE mail = %s
            """, (mail,))
            return cur.fetchone()[i]


def get_by_id(base, name, password, client_id, i):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT client_id, first_name, last_name, mail FROM clients WHERE client_id = %s
            """, (client_id,))
            return cur.fetchone()[i]


def get_by_mail_phone(base, name, password, client_info, i):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT client_id, first_name, last_name, mail, phone_num FROM clients
            LEFT JOIN phones USING(client_id)
            WHERE mail  = %s OR phone_num  = %s
            ORDER BY first_name;
            """, (client_info, client_info))
            return cur.fetchone()[i]


def get_by_id_phone(base, name, password, client_info, i):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT client_id, first_name, last_name, mail FROM clients
            LEFT JOIN phones USING(client_id)
            WHERE client_id  = %s OR phone_num  = %s
            ORDER BY first_name;
            """, (client_info, client_info))
            return cur.fetchone()[i]


def get_phones(base, name, password, client_id):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT phone_num_id, client_id, phone_num FROM clients
            JOIN phones USING(client_id)
            WHERE client_id = %s
            ORDER BY phone_num_id 
            """, (client_id,))
            return cur.fetchmany(5)


def get_requested_phone(base, name, password, phone_num):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT phone_num_id FROM phones
            WHERE phone_num = %s
            """, (phone_num,))
            return cur.fetchone()


def delete_client(base, name, password, client_id):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM phones CASCADE
            WHERE client_id = %s;

            DELETE FROM clients CASCADE
            WHERE client_id = %s;

            """, (client_id, client_id))
            conn.commit()


def delete_phone(base, name, password, phone_num):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            DELETE FROM phones 
            WHERE phone_num = %s
            """, (phone_num,))
            conn.commit()


def add_phone(base, name, password, client_id, phone_num):
    with psycopg2.connect(database=base, user=name, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO phones(client_id, phone_num) VALUES
            (%s, %s);
            """, (client_id, phone_num))
            conn.commit()


if __name__ == '__main__':

    database = 'postgres'
    username = 'postgres'
    pwd = 'password'

    conn = psycopg2.connect(database=database, user=username, password=pwd)
    with conn.cursor() as curs:

        def get_by_mail_hw(cursor, mail):
            cursor.execute("""
            SELECT client_id, first_name, last_name FROM clients WHERE mail = %s
            """, (mail,))
            return cursor.fetchone()
        # print(get_by_mail_hw(curs, 'mail'))

        def get_by_id_hw(cursor, client_id):
            cursor.execute("""
            SELECT client_id, first_name, last_name, mail FROM clients WHERE client_id = %s
            """, (client_id,))
            return cursor.fetchone()
        # print(get_by_id_hw(curs, 'client_id'))

        '''Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону'''
        def get_by_any_data(cursor, client_info):
            cursor.execute("""
            SELECT client_id, first_name, last_name, mail, phone_num FROM clients
            LEFT JOIN phones USING(client_id)
            WHERE first_name  = %s OR last_name  = %s OR mail  = %s or phone_num  = %s
            ORDER BY first_name;
            """, (client_info, client_info, client_info, client_info))
            return cursor.fetchone()
        print(get_by_any_data(curs, 'client_info'))
    conn.close()

    '''Функция, создающая структуру БД(таблицы).'''
    # create_tables(database, username, pwd)

    '''Функция, позволяющая добавить нового клиента.'''
    # insert_data(database, username, pwd, 'first_name', 'last_name', 'mail')

    '''Функция, позволяющая добавить телефон для существующего клиента.'''
    # insert_phone(database, username, pwd, 'first_name', 'mail', 'phone_num')
    # add_phone(database, username, pwd, 'client_id', 'phone_num')

    '''Функция, позволяющая изменить данные о клиенте.'''
    # edit_client_data(database, username, pwd, 'client_id', 'mail', 'first_name', 'last_name')
    # edit_phone_num(database, username, pwd, 'phone_num_id', 'phone_num')

    '''Функция, позволяющая удалить телефон для существующего клиента.'''
    # delete_phone(database, username, pwd, 'phone_num')

    '''Функция, позволяющая удалить существующего клиента.'''
    # delete_client(database, username, pwd, 'client_id')

    # get_clients(database, username, pwd)
    # get_records(database, username, pwd)

    # get_phones(database, username, pwd, 'client_id')
    # get_requested_phone(database, username, pwd, 'phone_num')





