#!/usr/bin/env python3
"""Models and database I/O functionality.

Almost all of this is directly copied from the sqlalchemy docs
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
"""

import os
from typing import Optional

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from db.pin import Pin

Base = declarative_base()


class DbManager:
    """"Class to hold the DB I/O handles

    Fields:
        session: handle for commit/rollback/closing
        debug: if True, echoes verbose commands
        db_path: path+filename of database file
            has to start with 'sqlite://'
        _engine: database interface
    """

    def __init__(self, db_path: Optional[str] = None, *, debug: bool = False):
        self._session = None
        self.debug = debug
        self._engine = None

        if db_path:
            self.db_path = db_path
        else:
            self.db_path = 'sqlite:///pin_out.db'

    def _get_handles(self):
        """Connect to the database"""
        if not self.db_path:
            raise ValueError("Require a DB path in order to connect!")

        self._engine = create_engine(
            self.db_path, convert_unicode=True, echo=self.debug)
        self._session = sessionmaker(bind=self._engine)

    def open_session(self) -> sqlalchemy.orm.session.Session:
        """Open and return a session with the database"""
        self._get_handles()
        return self._session()

    def _create_db(self, db_path: Optional[str] = None):
        """Create the database and holds handles to it

        Args:
            db_path: SQLite database path
                needs the full 'sqlite://' part in the name

        """
        self._get_handles()
        Pin.__table__.create(self._engine)


if __name__ == "__main__":
    print("Creating database...")
    if os.path.exists('pin_out.db'):
        raise FileExistsError(
            "'pin_out.db' already exists, please delete and retry")
    manager = DbManager(debug=True)
    manager._create_db()
    print("Database created")
