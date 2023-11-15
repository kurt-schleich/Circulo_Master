from abc import ABC, abstractmethod


class ContatoBase(ABC):

    def __init__(self, id:str, email:str):
        self.id = id
        self.email = email
        self.favor = False

    @abstractmethod
    def getId(self):
        return self.id

    @abstractmethod
    def setId(self, id:str):
        pass

    @abstractmethod
    def getEmail(self):
        pass

    @abstractmethod
    def setEmail(self, email: str):
        pass

    @abstractmethod
    def getFavor(self):
        pass
