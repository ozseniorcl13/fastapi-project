from zope import interface, component
from app.domain.services.IDatasetsService import IDatasetsService

@interface.implementer(IDatasetsService)
class DatasetsServiceImpl:
    def validate(self, namespace: str):
        return f'Datasets: {namespace}' 

component.provideUtility(DatasetsServiceImpl())