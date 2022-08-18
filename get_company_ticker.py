#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys
import config
import json
import urllib
from urllib.request import urlopen
import sqlite3


CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS public_companies(
                        id integer PRIMARY KEY,
                        cik integer,
                        name text,
                        ticker text,
                        exchange text);"""


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, CREATE_TABLE_SQL, tablename):
    """ create a table from the CREATE_TABLE_SQL statement
    :param conn: Connection object
    :param CREATE_TABLE_SQL: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(CREATE_TABLE_SQL)
    except Error as e:
        print(e)


def insert_into(conn, record, tablename):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """

    sql = f"INSERT INTO public_companies(cik, name, ticker, exchange) VALUES(?,?,?,?)"
    cur = conn.cursor()

    try:
        cur.execute(sql, record)
    except Exception as e:
        print(f"Error: Thrown\n {e} \n\n \
                Above error, was thrown on following record: {record}")

    conn.commit()
    return cur.lastrowid


def main(url, db):

    database = tablename = db

    # request and read data file
    response = urllib.request.urlopen(url)
    raw_data = response.read()

    # process json from file to dict
    company_tickers_dict = json.loads(raw_data)
    ticker_data = company_tickers_dict['data']

    # create a database connection and table if not exist
    conn = create_connection(database)
    create_table(conn, CREATE_TABLE_SQL, tablename)

    with conn:

        # iterate each record in file, and insert into database table
        for entry in ticker_data:
            entry_id = insert_into(conn, entry, tablename)


if __name__ == "__main__":

    start = time.perf_counter()
    database = f"{os.getcwd()}/db/public_companies.db"
    url = config.COMPANY_TICKERS_EXCHANGE_URL
    main(url, database)

    database = f"{os.getcwd()}/db/company_tickers_mf.db"
    url = config.COMPANY_TICKERS_MF_URL
    main(url, database)

    print(f"Serial downloader took {time.perf_counter() - start} sec")
