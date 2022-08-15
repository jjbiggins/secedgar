#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


from flask import Flask
from flask_restful import Api, Resource



app = Flask(__name__)
api = Api(app)



class CompanyTickersAPI(Resource):
    def get(self, id):
        pass

api.add_resource(CompanyTickersAPI, 'https://www.sec.gov/files/company_tickers_mf.json', enpoin

