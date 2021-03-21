from configparser import ConfigParser
import psycopg2


def config(filename='../database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect(username, password):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print("Checking IF User Exists?")
        cur.execute(f'SELECT * from user_details where user_name = \'{username}\' and user_pass = \'{password}\'')

        # display the PostgreSQL database server version
        user_list = cur.fetchall()
        print(len(user_list))
        print(user_list)
        # close the communication with the PostgreSQL
        cur.close()
        return user_list
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert(username, vid_id, vid_tag, sec_key, sec_msg):
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database to Insert...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        # cur.execute(f'SELECT * from user_details where user_name = \'{username}\' and user_pass = \'{password}\'')
        insert_stmt = f'INSERT INTO video_details (vid_id, vid_tag, sec_key, sec_msg, user_name) VALUES ({vid_id}, \'{vid_tag}\', \'{sec_key}\', \'{sec_msg}\', \'{username}\')'
        print("Inserting TO Database ")
        cur.execute(insert_stmt)

        # To Reflect Insert in Database  we need to commit in connection
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_signup(firstname, lastname, emailadd, set_username, password):
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database to Insert Signup...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        # cur.execute(f'SELECT * from user_details where user_name = \'{username}\' and user_pass = \'{password}\'')
        insert_stmt = f'INSERT INTO user_details (user_name, user_pass, first_name, last_name, email_id ) VALUES ({set_username}, \'{password}\', ' \
                      f'\'{firstname}\', \'{lastname}\', \'{emailadd}\')'
        print("Inserting TO Database ")
        cur.execute(insert_stmt)

        # To Reflect Insert in Database  we need to commit in connection
        conn.commit()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
# if __name__ == '__main__':
#     connect()
