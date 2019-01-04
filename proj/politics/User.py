from proj.utils.dbUtils import get_user_db
from proj.constants.politicsConstants import Stances, Weights


class User:

    def __init__(self, last_name, first_name, stances, weights):
        self.id = get_user_db().count()
        self.lastName = last_name
        self.firstName = first_name
        self.abortionStance = stances[Stances.abortion]
        self.climateChange = stances[Stances.climateChange]
        self.gunStance = stances[Stances.guns]
        self.obamaCareSupport = stances[Stances.obamaCare]
        self.mexicoWallSupport = stances[Stances.mexicoWall]
        self.proImmigration = stances[Stances.immigration]
        self.abortionWeight = weights[Weights.abortion]
        self.climateWeight = weights[Weights.climateChange]
        self.gunWeight = weights[Weights.guns]
        self.obamaCareWeight = weights[Weights.obamaCare]
        self.mexicoWallWeight = weights[Weights.mexicoWall]
        self.proImmigrationWeight = weights[Weights.immigration]
