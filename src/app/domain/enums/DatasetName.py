from enum import Enum

class DatasetName(str, Enum):
    CUSTOM = 'custom'
    IRIS = 'iris'
    SARS_COV = 'sars_cov'