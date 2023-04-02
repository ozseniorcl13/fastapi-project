from zope.interface import Interface

class IDatasetsService(Interface):
    def validate(self, namespace: str):
        pass