from zope.interface import Interface

class IExperimentService(Interface):
    def findAllByNamespace(self, namespace: str):
        pass