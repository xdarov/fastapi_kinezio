import os

DB = {
    'DB_ENGINE': os.environ['DB_ENGINE'],
    'DB_HOST': os.environ['DB_HOST'],
    'DB_DATABASE': os.environ['DB_DATABASE'],
    'DB_PORT': os.environ['DB_PORT'],
    'DB_USER': os.environ['DB_USER'],
    'DB_PASSWORD': os.environ['DB_PASSWORD']
}


def get_db_settings():
    return f'{DB["DB_ENGINE"]}://{DB["DB_USER"]}:{DB["DB_PASSWORD"]}'\
           f'@{DB["DB_HOST"]}:{DB["DB_PORT"]}/{DB["DB_DATABASE"]}'


if __name__ == '__main__':
    print(get_db_settings())
