from proj.app import db
from proj.constants.politicsConstants import Stances


class Candidate:
    """
    Class for a specific political candidate, uniquely defined by an ID.
    Stores the candidate's stance on important issues as well as first and last name.
    Stances are denoted by a simple +1 and -1 to indicate support or opposition on a specific issue.

    PLANS:
    1.Change the way stances are stored to encompass more views. Create a Stances object that encompasses non-binary
        issues. Migrate over to PostgreSQL to encode relation Company -> Candidate -> Stance.
    """

    def __init__(self, last_name, first_name):
        # TODO: Add Code to add stances on different issues using VoteSmart API
        self.id = db.get_candidate_db().count()
        self.lastName = last_name
        self.firstName = first_name
        self.stances = self.get_candidate_stances()
        attrs = {'lastName': self.lastName,
                 'firstName': self.firstName,
                 'stances': self.stances}
        db.get_candidate_db().insert_one(attrs)

    @staticmethod
    def get_candidate_from_name(last_name, first_name):
        return db.get_candidate_db().find_one({'firstName': first_name, 'lastName': last_name})

    @staticmethod
    def get_candidate_from_id(candidate_id):
        return db.get_candidate_db().find_one({'id': candidate_id})

    def push_to_db(self):
        pass

    def get_candidate_stances(self):
        return self

    def set_candidate(self, stances):
        db.get_candidate_db().update_one({'id': self.id}, {'$set': stances})
