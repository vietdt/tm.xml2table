"""Definition of the XMLFile content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from tm.xml2table.interfaces import IXMLFile
from tm.xml2table.config import PROJECTNAME

XMLFileSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

XMLFileSchema['title'].storage = atapi.AnnotationStorage()
XMLFileSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(XMLFileSchema, moveDiscussion=False)


class XMLFile(base.ATCTContent):
    """a content-type that accepts xml file then render a html display"""
    implements(IXMLFile)

    meta_type = "XMLFile"
    schema = XMLFileSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(XMLFile, PROJECTNAME)
