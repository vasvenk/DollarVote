from proj.utils.dbUtils import get_candidate_db


class Candidate:
    """
    Class for a specific political candidate, uniquely defined by an ID.
    Stores the candidate's stance on important issues as well as first and last name.
    Stances are denoted by a simple +1 and -1 to indicate support or opposition on a specific issue.

    PLANS:
    1.Change the way stances are stored to encompass more views. Create a Stances object that encompasses non-binary
        issues. Migrate over to PostgreSQL to encode relation Company -> Candidate -> Stance.
    """

    def __init__(self, name, open_secrets_id):
        # TODO: Add Code to add stances on different issues using VoteSmart API
        self.name = name
        self.stances = self.get_candidate_stances()
        self.openSecretsId = open_secrets_id
        attrs = {'openSecretsId': self.openSecretsId,
                 'name': self.name,
                 'stances': self.stances}
        get_candidate_db().insert_one(attrs)

    @staticmethod
    def get_candidate_from_name(name):
        return get_candidate_db().find_one({'name': name})

    @staticmethod
    def get_candidate_from_id(candidate_id):
        return get_candidate_db().find_one({'openSecretsId': candidate_id})

    def push_to_db(self):
        pass

    def get_candidate_stances(self):
        # TODO: Finish this method by integrating with VoteSmart API
        return {}

    def set_candidate(self, stances):
        get_candidate_db().update_one({'openSecretsId': self.openSecretsId}, {'$set': stances})
