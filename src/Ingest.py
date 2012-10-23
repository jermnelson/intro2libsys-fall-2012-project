__author__ = "Chris Coughlan, Brian Shoemaker, Katharine Hales"

import common,sys,os,mimetypes

def ingest_manuscript(file_path):
    # Queries repository and gets the next available pid in the coccc
    # namespace
    new_pid = common.repository.get_next_pid(namespace="coccc")
    # Opens up the mods.xml from the directory
    mods = etree.XML(open(os.path.join(file_path,"mods.xml"),'rb'))
    # Adds MODS datastream to the new object
    common.repository.api.addDatastream(pid=new_pid,
                                        dsID="MODS",
                                        dsLabel="MODS",
                                        mimeType="application/rdf+xml",
                                        content=etree.tostring(mods))
    # create a file directory walker to find image files in the directory
    manuscript_files = next(os.walk(file_path))[1]
    for filename in manuscript_files:
        file_root,file_ext = os.path.splitext(filename)[1]
        if [".png",".jpg",".gif"].count(file_Ext) > 0:
            common.repository.api.addDatastream(pid=new_pid,
                                                dsID=file_root,
                                                dsLabel=file_root,
                                                mimeType=,
                                                content=)
    # finally, add RELS-EXT datastream
    
    
