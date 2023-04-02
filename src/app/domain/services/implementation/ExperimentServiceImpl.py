from zope import interface, component
from app.domain.services.IExperimentService import IExperimentService

@interface.implementer(IExperimentService)
class ExperimentServiceImpl:
    def findAllByNamespace(self, namespace: str):
        return f'Experiments: {namespace}' 

component.provideUtility(ExperimentServiceImpl())