#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from sqlalchemy import BigInteger, Boolean, Column, \
                       Date, DateTime, Enum, Float, ForeignKey, Integer, \
                       String, UniqueConstraint, and_, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



CIK = 'cik_str'
TICKER = 'ticker'
TITLE = 'title'


Base = declarative_base()

class PublicCompany(Base):
    __tablename__ = 'public_companies'

    cik = Column(Integer, primary_key=True)
    ticker = Column(String)
    name = Column(String)
    exchange = Column(String)



