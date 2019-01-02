import os

from proj.constants.EnvVariables import EnvVariables
from pymongo import MongoClient

db = MongoClient(os.environ.get(EnvVariables.mongoUrl)).DollarVote0


def get_candidate_db():
    return db.Candidates


def get_user_db():
    return db.Users


def get_company_db():
    return db.Companies
