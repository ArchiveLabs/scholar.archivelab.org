#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    api/scholar.py
    ~~~~~~~~~~~~~~
    Scholar API

    :copyright: (c) 2015 by mek.
    :license: see LICENSE for more details.
"""

from random import randint
from datetime import datetime
from sqlalchemy import Column, Unicode, BigInteger, Integer, \
        DateTime, ForeignKey, Table, exists, func
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm import relationship
from metapub import FindIt
from api import db, engine, core


class Journal(core.Base):

    __tablename__ = "artists"
    __table_args__ = {'sqlite_autoincrement': True}
    TBL = __tablename__

    id = Column(BigInteger, primary_key=True)
