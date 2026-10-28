from os import system as __exec


___PGSQL_DATABASE_FOLD_INIT: str = '~/._labs'


def __init_pgsql_instance() -> None:
    print('creando instancia pgsql')
    __exec('initdb ' + ___PGSQL_DATABASE_FOLD_INIT)


def __init_pg_serve() -> None:
    print('iniciando server pgsql')
    __exec(
        'pg_ctl '
        + '-D {} '.format(___PGSQL_DATABASE_FOLD_INIT)
        + '-l {} '.format(___PGSQL_DATABASE_FOLD_INIT + '/logfile')
        + 'start '
    )


def __create_pg_usr() -> None:
    print('creando user')
    usr: str = input('User<admin>: ') or 'admin'
    __exec(
        'createuser '
            '--superuser '
            '--pwprompt '
            + usr
    )


def __create_on_pg_sample_db() -> None:
    print('creando db')
    db_name: str = input('Database Name<sample>: ') or 'sample'
    __exec('createdb ' + db_name)


def main() -> None:
    try:
        __init_pgsql_instance()
        __init_pg_serve()
        __create_pg_usr()
        __create_on_pg_sample_db()

    except Exception as e:
        print('error creating instance pgsql: ', str(e))


if __name__ == '__main__':
    main()

