__author__= "Claire L Mattoon, Johnny Edward, Eric Ziecker"

import common
import xml.etree.ElementTree as etree
import sunburnt
Solr_server = sunburnt.SolrInterface("http://0.0.0.0:8984/solr/marc_catalog/")

FIELDNAMES = [
    'access', # Should have a constant value of "Online"
    'author', #namePart
    'bib_num', # Pid
    'contents', # Should be all of the text of a transcription (if present)
    'format', #! Incorrect this should not be a subject
    'full_title', #title
    'id', #system generated, should be the PID
    'location', #! Incorrect, this should be a constant of dacc
    'notes', #! Incorrect, only include public access notes (not record notes), abstract
    'personal_name', #namePart
    'summary', # abstract
    'title', # title
    'topic', #subject
    'url', # Should be the URL in the location 
]

def get_title(mods):
    """
    Function takes the objects MODS and extracts and returns the text of the title.
    """
    title = mods.find("{{{0}}}titleInfo/{{{0}}}title".format(common.MODS_NS))
    return title.text

def get_topics(mods):
    """
    Function takes the objects MODS and returns the text of the topics.
    """
    output = []
    topics = mods.findall("{{{0}}}subject/{{{0}}}topic".format(common.MODS_NS))
    for topic in topics:
        output.append(topic.text)
    return output

def get_author(mods):
    """
    Function takes the object's MODS and extracts and returns the text of the
    author.

    :param mods: Etree XML of MODS datastream
    :rtype: string of the author
    """
    name_part = mods.find("{{{0}}}name/{{{0}}}namePart".format(common.MODS_NS))
    return name_part.text
                          

def get_mods(pid):
    """
    Function attempts to extract the MODS datastream from the digital
    repository

    :param pid: PID of the object
    :rtype: Etree of the MODS datastream
    """
    # Save results of attempting to retrieve the MODS datstream from the
    # repository
    mods_result = common.repository.api.getDatastreamDissemination(pid=pid,
                                                                   dsID="MODS")
    # Gets the raw XML from the result
    mods_xml = mods_result[0]
    # Returns the etree MODS xml object from the raw XML
    return etree.XML(mods_xml)

def get_summary(mods):
    """
    Function extracts abstract from MODS and returns text.
    """
    summary = mods.find("{{{0}}}abstract".format(common.MODS_NS))
    return summary.text

def get_url(mods):
    """
    Function extracts URL location from MODS and returns text.
    """
    url = mods.find("{{{0}}}location/{{{0}}}url".format(common.MODS_NS))
    return url.text

def index_manuscript(pid):
    """
    Function takes PID, extracts MODS, creates Solr document and attempts to ingest into Solr.
    """

    mods = get_mods(pid)
    Solr_doc = {'access':'Online',
                'bib_num':pid,
                'format':'Manuscript',
                'location':'dacc',
                'id':pid}
    Solr_doc['author'] = get_author(mods)
    Solr_doc['title'] = get_title(mods)
    Solr_doc['full_title'] = Solr_doc['title']
    Solr_doc['topic'] = get_topics(mods)
    Solr_doc['summary'] = get_summary(mods)
    Solr_doc['notes'] = Solr_doc['summary']
    Solr_doc['personal_name'] = Solr_doc['author']
    Solr_doc['url'] = get_url(mods)
    Solr_server.add(Solr_doc)
