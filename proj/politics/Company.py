from proj.politics.Candidate import Candidate
from proj.utils.dbUtils import get_company_db


class Company:

    def __init__(self, name):
        self.companyId = get_company_db().size()
        self.name = name
        self.parent = None
        self.candidates = []
        self.total = 0

    def add_candidate(self, candidate_id, contribution):
        candidate = {'id': candidate_id, 'contribution': contribution}
        self.candidates.append(candidate)
        self.total += contribution

    def push_to_db(self):
        attrs = {'id': self.companyId,
                 'name': self.name,
                 'parent': self.parent,
                 'candidates': self.candidates,
                 'total': self.total}
        get_company_db().update_one({'id': self.companyId}, {'$set': attrs})

    def issue_stance(self, issue_name):
        total = 0
        for candidate in self.candidates:
            curr_candidate = Candidate.get_candidate_from_id(candidate['id'])
            total += (candidate['contribution'] / self.total) * curr_candidate['stances'].get(issue_name, 0)
        return total
