# QUERIES
CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""
CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls(id));"""
CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, FOREIGN KEY(option_id) REFERENCES options(id));"""

SELECT_ALL_POLLS = "SELECT * FROM polls;"
SELECT_POLL_WITH_OPTIONS = "SELECT * FROM polls JOIN options ON polls.id = options.poll_id WHERE oplls.id = %s;"
INSERT_OPTION = "INSERT INTO options (option_test, poll_id) VALUES %s;"
INSERT_VOTE = "INSERT INTO votes (username, option_id) VALUES (%s, %s);"


# DATABASE FUNCTIONS
def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


def get_polls(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_latest_poll(connection):
    with connection:
        with connection.cursor() as cursor:
            pass


def get_poll_details(connection, poll_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))
            return cursor.fetchall()


def get_poll_and_vote_results(connection, poll_id):
    with connection:
        with connection.cursor() as cursor:
            pass


def get_random_poll_vote(connection, option_id):
    with connection:
        with connection.cursor() as cursor:
            pass


def create_poll(connection, title, owner, options):
    with connection:
        with connection.cursor() as cursor:
            pass


def add_poll_vote(connection, username, option_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))
