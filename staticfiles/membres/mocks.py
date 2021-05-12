
class Arif():

    ARIFS = ['nom', 'hadara', 'adresse', 'numero', 'photo']

    @classmethod
    def all(cls):
        return cls.ARIFS


    @classmethod
    def find(cls, id):
        return cls.ARIFS[int(id) - 1]
