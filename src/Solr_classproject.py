__author__= "Claire L Mattoon, Johnny Edward, Eric Ziecker"

import common
import xml.etree.ElementTree as etree

FIELDNAMES = [
    'access', # Should have a constant value of "Online"
    'audience',
    'author', #namePart
    'bib_num',
    'callnum',
    'callnumlayerone',
    'collection', #! Incorrect
    'contents', # Should be all of the text of a transcription (if present)
    'corporate_name',
    'ctrl_num',
    'description',
    'era',
    'format', #! Incorrect this should not be a subject
    'full_title', #title
    'full_lc_subject',
    'genre',
    'holdings',
    'id', #system generated, should be the PID
    'imprint',
    'isbn',
    'issn',
    'item_ids',
    'language',
    'language_dubbed', 
    'language_subtitles',
    'lc_firstletter',
    'location', #! Incorrect, this should be a constant of dacc
    'marc_record',
    'oclc_num',
    'notes', #! Incorrect, only include public access notes (not record notes), abstract
    'personal_name', #namePart
    'place',
    'publisher',
    'publisher_location',
    'pubyear',
    'series',
    'summary',
    'title', # title
    'title_sort',
    'topic', #subject
    'upc',
    'url', # Should be the URL in the location 
]

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


