from model.entity import Entity

class EntityDb:
    def __init__(self):
        self.entityMap = {}
        self.nextID = 1

    def insertEntity(self, Entity):
        self.entityMap[self.nextID] = Entity

    def getEntity(self, ID: int):
        ## return ID if it exists, nothing if it doesn't
        if(ID in self.entityMap.keys()):
            return self.entityMap[ID]
        else:
            return None