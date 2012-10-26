__author__ = "Chris Coughlan, Brian Shoemaker, Katharine Hales"

import common,sys,os,mimetypes,argparse
import urllib,urllib2,urlparse
import xml.etree.ElementTree as etree

from jinja2 import Template
from local_settings import COLLECTION_PID,FEDORA_ROOT

RELS_EXT = '''<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" 
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" 
         xmlns:fedora="info:fedora/fedora-system:def/relations-external#" 
         xmlns:islandora="http://islandora.ca/ontology/relsext#" 
         xmlns:dc="http://purl.org/dc/elements/1.1/" 
         xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/" 
         xmlns:fedora-model="info:fedora/fedora-system:def/model#">
 <rdf:Description rdf:about="info:fedora/{{ object_pid }}">
   <fedora:isMemberOfCollection rdf:resource="info:fedora/{{ parent_pid }}"></fedora:isMemberOfCollection>
   <fedora-model:hasModel rdf:resource="info:fedora/{{ content_model }}"></fedora-model:hasModel>}
 </rdf:Description>
</rdf:RDF>'''

def ingest_manuscript(file_path):
    # Queries repository and gets the next available pid in the coccc
    # namespace
    new_pid = common.repository.api.ingest(text=None,
                                           namespace="coccc")
    # Opens up the mods.xml from the directory
    mods = etree.XML(open(os.path.join(file_path,"mods.xml"),'rb').read())
    # Adds MODS datastream to the new object
    common.repository.api.addDatastream(pid=new_pid,
                                        dsID="MODS",
                                        dsLabel="MODS",
                                        mimeType="application/rdf+xml",
                                        content=etree.tostring(mods))
    # create a file directory walker to find image files in the directory
    manuscript_files = next(os.walk(file_path))[2]
    
    for filename in manuscript_files:
        file_root,file_ext = os.path.splitext(filename)
        if file_ext != "xml": 
            content = open(os.path.join(file_path,filename),"rb").read().encode("base64")
            result = common.repository.api.addDatastream(pid=new_pid,
                                                dsID=filename,
                                                dsLabel=file_root,
                                                mimeType="image/jpeg",
                                                content=content)
            print("...tried to add {0}, result={1}".format(filename,result))
    # finally, add RELS-EXT datastream
    rels_ext_template = Template(RELS_EXT)
    rels_ext = rels_ext_template.render(object_pid=new_pid,
                                        content_model="adr:adrBasicObject",
                                        parent_pid=COLLECTION_PID)
    common.repository.api.addDatastream(pid=new_pid,
                                        dsID="RELS-EXT",
                                        dsLabel="RELS-EXT",
                                        mimeType="application/rdf+xml",
                                        content=rels_ext)
    return new_pid
    
                                        
arg_parser = argparse.ArgumentParser(description="Ingest Manuscript collection into Fedora Repository")
arg_parser.add_argument('directory',
                        nargs="+",
                        help="[directory] top-level directory where the object's MODS and image files reside")

if __name__ == "__main__":
    args = arg_parser.parse_args()
    if 'directory' is args:
        target_directory = args.directory
        print("Attempting to ingest manuscript at {0} into {1}".format(target_directory,
                                                                       FEDORA_ROOT))
        new_pid = ingest_manuscript(target_directory)
        print("Ingested Manuscript, new pid={0}".format(new_pid))
    
