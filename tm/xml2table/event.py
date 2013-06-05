import os
import time
from mimetypes import guess_type
from lxml import etree

from Products.CMFCore.utils import getToolByName

from config import TABLE_FOLDER, XML_FOLDER, XSL_FOLDER

def createTable(obj, e):
    """
    An event handler triggered when a ATFile is initialized.
    This will check whether the uploaded file is xml. If yes, it will create
    a table based on the xml and the associated xsl.
    """
    print 'ENTERING createTable event handler ...'
    parent = obj.aq_parent
    portal_url = getToolByName(obj, 'portal_url')
    portal = portal_url.getPortalObject()
    xml_folder_path = os.path.join('/', portal.id, XML_FOLDER)
    parent_path = '/'.join(parent.getPhysicalPath())
    # xml file should be added in correct folder
    if parent_path == xml_folder_path:
        print 'FOUND new file in correct folder: %s' % parent_path
        xml_file = obj.getFile()
        if isXMLFile(xml_file.content_type, xml_file.filename):
            print 'FOUND XML file: %s' % xml_file.filename
            try:
                xml = etree.fromstring(xml_file.data)
            except etree.XMLSyntaxError:
                print 'ERROR XMLSyntaxError: XML data is invalid'
                return None
            # FIXME: find exact xml element 'xslFilename'
            el = xml.find('xslFilename')
            if el is None:
                print 'ERROR NotFound: xslFilename element'
                return None
            xsl_filename = el.text
            print 'FOUND xslFilename element: %s' % xsl_filename
            xsl_file_path = os.path.join('/', portal.id, XSL_FOLDER, xsl_filename)
            try:
                xsl_obj = obj.unrestrictedTraverse(xsl_file_path)
            except AttributeError:
                print 'ERROR NotFound: xsl object at %s' % xsl_file_path
                return None
            print 'FOUND xsl object at: %s' % xsl_file_path
            id = 'table-%s-%s' % (obj.id, time.strftime('%y%m%d%H%M%S'))
            title = 'Table of %s' % obj.id
            portal.invokeFactory('XMLFile', id,
                                 title=title,
                                 xmlfile=xml_file,
                                 xslfile=xsl_obj.getFile())
            print 'CREATE new table: %s' % id

def isXMLFile(content_type, filename):
    """
    Validate the mimetype of uploaded file
    """
    if content_type and 'xml' in content_type:
        return True
    if filename.endswith('.xml'):
        return True
    return False