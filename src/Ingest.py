__author__ = "Chris Coughlan, Brian Shoemaker, Katharine Hales"

import common
from eulfedora.models import DigitalObject,FileDatastream,XmlDatastream,FileDatastreamObject

class ManuscriptDigitalObject(DigitalObject):
    CONENT_MODELS = [ "info:fedora/" ]

def ingest_manuscript(file_path):
    manuscript_fedora = common.repository.get_object()
    
