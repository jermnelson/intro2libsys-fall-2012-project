======
README
======
From an October 1st, 2012 e-mail

Here is the follow up from tonight's class regarding the class project and extra credit.

Instead of having two separate projects, we are instead just going to work on one existing
digital collection as two small groups working on one of the two following goals:

   1. Harvest and ingest most of the digital images of primarily handwritten letters currently
      located at 
      `http://www2.coloradocollege.edu/library/index.php/specialcollections/alice-bemis-taylor-collection-ms-0145`_
      into the Digital Archives of Colorado College located at
      `http://dacc.coalliance.org/`_. The small group responsible for this goal is made up
      of Brian, Chris, and Katharine.
     
   2. After the manuscripts are ingested into Fedora, the Fedora Objects will be indexed
      into Colorado College's Solr index for use by the Discovery Layer at
      `http://discovery.coloradocollege.edu/`_. The small group responsible for this goal is
      made of Johnny, Claire, and Eric.     
     
Since this week there is not any readings and to give you some practical experience
in digital cataloging and basic digital curation, I have randomly assigned 15 of these
letters to each of you. Here are the basic steps for preparing the core records 
for ingestion into CC's digital repository. I have attached a git bundle
that has a MODS XML template and a couple examples using two of the letters in the
collection. I selected the first, a letter written by Joseph
Addison, and a letter by Elizabeth Barrett Browning as examples for your reference.

1. Clone the attached bundle to its own repository. You will be repeating
   steps 2 through 8 for each of your 15 letters. Go to the repository and you should
   see three items, a mods-template.xml file, and two directories; AddisonJ and BrowningE.

2. Go to the the home page for the letter. For example, the Addison letter home page is
   `http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/AddisonJ.html`_
   For the Browning letter it is:
   `http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/BrowningE.html`_

3. Note the name of the home-page. You'll use that same name as the directory name for the
   manuscript's images, MODS XML metadata file, and any transcript text files. For the
   Addison letter home-page, it is AddisonJ, for the Browning letter it is BrowningE.  
  
   mkdir AddisonJ
  
4. Copy the mods-template into the new manuscript directory as mods.xml. For example, I
   ran the following command (you can also do this through Windows Explorer or MacOS UI):
  
   cp mods-template.xml AddisonJ/mods.xml
  
5. Open the new mods.xml file in a text editor. You will need to add values about the
   manuscript to the following MODS XML fields:
  
   title - Use the name and dates of the link text from the home-page. For example, the
           link text I used for the Addison letter is Addison, Joseph. (1672-1719)
             
          
   namePart - Use just the name of the letter writer. For the examples, I used
              Addison, Joseph
             
   subject - There are multiple subject elements. For the subject with the name sub-element,
             add the same value you used for the title. In the link text on the home-page,
             many of the entries have two or three character codes like A.L., A.L.S., D.S.,
             and MS. These codes have been reformulated as subjects with topic sub-elements.
             Keep the subjects that are in the link text and delete those subjects that
             are not. The subject/topic values correspond to the following:
            
             A.L. - autograph (handwritten) letter
             A.L.S. - autograph letter, signed
             D.S. - document, signed
             M.S. -  manuscript
            
             For the Addison letter, I removed the document, signed
             and manuscript elements.
            
  recordOrigin - In this field, add your name and any notes you might want to include.
 
  recordCreationDate - The date you created this record.
 
6. Each letter has links to a separate page for each scanned image. Click on the link
   and go to the page. You should see a large image with a small amount of text. Download
   and save each image to the letter's directory. For the Addison letter, I downloaded
   the following jpgs: AddisonJ01a.jpg, AddisonJ02a.jpg, AddisonJ03a.jpg, AddisonJ04a.jpg,
   and AddisonJ05a.jpg.
  
7. Some letters have a transcription. Click on the link and you should an HTML page with
   the text of the letter. Copy the text into a new text file and save in the letter
   directory as transcription.txt. For example, the Browning letter has a transcript which
   I copied into a text file called transcription.txt.
  
8. Add the letter directory to the git repository.

9. Commit your new records to the repository. Any bundle will likely be too big to send via
   email, I'll bring a thumb drive to class next week and I'll copy it then.
  
Letter Assignments:
Brian
        Rossetti, Dante Gabriel. (1828-1892) A.L.S. transcription
        Shenstone, William. (1714-1763) A.L.S.
        Arnold, Edwin. (1832-1904) A.L.S.
        Cooper, Thomas. (1805-1892) A.L.S.
        Ryland, John Collett. (1723-1792) Portrait
        Talfourd, T.M. (1795-1854) A.L.S.
        Kemble, Charles. (1775-1836) D.S.
        Crowquill, Alfred Henry, real name A. Forrester (1804-1872) A.L. (2)
        O.Keefe, John. (1747-1833) A.L.S.
        Moxon, Edward. (1801-1858) A.L.S.
        Southey, Robert. (l774-1843) A.L.S. (2) and MS.
        Watts, Alaric A. (1797-1864) A.L.S.
        Hemans, Felicia. (1793-1835) A.L.S. and MS.
        Bradley, Edward, pseud. Cuthbert Bede. (1827-1889) A.L.S.
        King, David. (1806-1883) MS.
Claire
        Palgrave, Francis Turner. (1824-1897) A.L.S.
        Greenwell, Dora. (1821-1882) A.L.S.
        Hall, Samuel Carter, A.L.S. and MS.
        Brooks, Shirley. A.L.S.
        Montgomery, Rev. Robert (1807-1855) A.L.S. and 2 MSS.
        Ingelow, Jean. (1820-1897) A.L.S. and MS.
        Sedley, Charles. (1639-1701) D.S.
        Howard, Robert. (1626-1698) DS.
        De Vere, Aubrey. (1814-1902) A.L.S. (2)
        Knight, Henry Gally. (1786-1846) A.L.S.
        Hope, Alex Beresford. (1820-1887) A.L.S.
        Kenyon, John. (1784-1856) A.L.S.
        Digby, Kenelm Henry. (1800-1880) MS.
        Arnold, Matthew. (1822-1888) A.L.S.
        Irving, Washington. (1783-1859) A.L.S.
Eric
        Capern, Edward.(1819-1894) A.L.S. and MS.
        Hannay, James. (1827-1873) A.L.S.
        Fitzgerald, William Thomas. (1759-1829) A.L. and MS.
        Knight, J. A.L.S.
        Bently, Elizabeth. A.L.S.
        Dallas, Robert Charles. (1754-1824) A.L.S.
        Crabbe, Rev. George. (1754-1832) MS.
        Noel, Roden, (1834-1894) A.L.S.
        Northcote, James. (1746-1831) MS.
        Coleridge, Samuel Taylor. (1772-1834) MS.
        Colman, George. (1762-1836) A.L.S. (2)
        Marvell, Andrew. (1621-1678) A.L.S.
        Chambers, Robert. (1802-1871) A.L.S.
        Whitehead, William. (1715-1785) A.L.S.
        Baillie, Joanna. (1762-1851) A.L.S.
Chris
        Scott, William Bell, (1811-1890) A.L.S.
        Forbes, Edward. (1815-1854) A.L.S.
        Eliot, George. (1819-1880) A.L.
        Moore, Thomas, (1779-1852) A.L.S.
        Lytton, Lord. (1801-1873) A.L.S. (2)
        Buchanan, Robert Williams. (1841-1901) A.L.S.
        Muller, Friedrich Max. (1823-1900) A.L.S.
        Taylor, John. (1711-1788) A.L.S.
        Benger, Elizabeth Ogilvy. (1778-1827) A.L.S.
        Allen, Grant. (1848-1899) A.L.S. and MS. transcription
        Landor, Walter. Portrait.
        Coleridge, Derwent. (1800-1883) A.L.S.
        Hallam, Henry. (1777-1859) A.L.S. and MS.
        Hobhouse, John C. (1786-1869) A.L.S.
        Carpenter, John Alden.(1876-1951) A.L.S.
Katharine
        Montgomery, Robert. (1807-1855) A.L.S. (2)
        Coleridge, Hartley. (1846?-1920) MS.
        Clare, John. (1793-1864) A.L.S.
        Mayne, John. (1759-1936) A.L.S.
        Rossetti, William Michael. (1829-1919) A.L.S.
        Thomson, James. (1700-1748) A.L.S.
        Jameson, Anna. (1794-1860) A.L.S.
        Darley, George. (1795-1846) A.L.S.
        Tennyson, Lord Alfred. (1809-1892) A.L.S.
        Plymptre, James. (1770-1832) A.L.S.
        Bailey, Philip James. (1816-1902) A.L.S.
        Boothby, Sir Brooke. (1743-1824) A.L.S.
        Porter, Anna. M. (1790-1832) A.L.
        Hume, David. (1711-1776) A.L.S.
        Spencer, William. (1769-1834) A.L.S. and A.L.
Johnny
        Mackay, Charles. (1814-1889) A.L.S. (2)
        Hofland, Barbara. (1770-1844) A.L.S.
        Turner, S. William. A.L.S.
        Waugh, Edwin. (1817-1890) A.L.S.
        Howitt, Richard. A.L.S.
        Morris, Lewis. A.L.S.
        Killigrew, Thomas. (1612-1693) MS.
        Polyhole, R. (1760-1838) A.L.S.
        Churchill, Charles. (1731-1764) D.S.
        Townsend, George. (1788-1857) A.L.S.
        Holmes, Oliver Wendell. (1809-1894) A.L.S.
        Sillery, Charles Doyne. (1807-1837) A.L.S.
        Temple, Sir William. (1628-1699) A.L.S.
        Dixie, Florence. A.L.S.
        Kemble, John Philip. Portrait

.. _http://www2.coloradocollege.edu/library/index.php/specialcollections/alice-bemis-taylor-collection-ms-0145: http://www2.coloradocollege.edu/library/index.php/specialcollections/alice-bemis-taylor-collection-ms-0145
.. _http://dacc.coalliance.org/: http://dacc.coalliance.org/
.. _http://discovery.coloradocollege.edu/: http://discovery.coloradocollege.edu/
.. _http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/AddisonJ.html: http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/AddisonJ.html
.. _http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/BrowningE.html: http://www2.coloradocollege.edu/library/SpecialCollections/Manuscript/Taylor/BrowningE.html
