"""
 :mod:`common` Helper functions for the Intro2libsys Fall 2012 Utilities
"""
import os,sys,urllib,urllib2
import xml.etree.ElementTree as etree

MODS_NS = 'http://www.loc.gov/mods/v3'



def add_subject(mods,**kwargs):
    new_subject = etree.SubElement(mods,"{0}subject".format(MODS_NS))
    if kwargs.has_key("topic"):
        new_topic = etree.SubElement(new_subject,"{0}topic".format(MODS_NS))
        

def update_abstract(mods,new_text):
    """
    :param mods: MODS eTree
    :param new_text: New text for MODS abstract
    """
    abstract = mods.find("{0}abstract".format(MODS_NS))
    abstract.text = new_text
                
    pass
    

def validate_mods(**kwargs):
    """
    Function opens and attempts to parse a MODS file

    :param url:  URL for MODS XML file
    :param txt: Raw text of MODS XML
    """

    mods_url = kwargs.get("url")
    if mods_url is not None:
        return etree.XML(urllib2.urlopen(mods_url).read())
    filename = kwargs.get("filename")
    if filename is not None:
        mods_file = open(filename,'rb').read()
        return etree.XML(mods_file)
    text = kwargs.get("txt")
    if text is not None:
        return etree.XML(text)
    return False 




def validate_collection(root):
    print("Validating collection {0}".format(root))
    walker = os.walk(root)
    collection_dirs = next(walker)[1]
    all_mods = []
    for directory in collection_dirs:
        if [".git","src"].count(directory)  > 0:
            continue
        mods_filename = os.path.join(root,directory,"mods.xml")
        print("..{0}".format(mods_filename))
        all_mods.append(validate_mods(filename=mods_filename))
    return all_mods
    
