"""Definition of the XMLFile content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.validation import V_REQUIRED
from plone.app.blob.field import BlobField

# -*- Message Factory Imported Here -*-

from Products.CMFPlone import PloneMessageFactory as _

from tm.xml2table.interfaces import IXMLFile
from tm.xml2table.config import PROJECTNAME
from tm.xml2table import validators

XMLFileSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    BlobField('xmlfile',
            required = True,
            primary = True,
            searchable = False,
            accessor = 'getXMLFile',
            mutator = 'setXMLFile',
            index_method = 'getIndexValue',
            languageIndependent = True,
            storage = atapi.AnnotationStorage(migrate=True),
            default_content_type = 'application/octet-stream',
            validators = (('isNonEmptyFile', V_REQUIRED),
                          ('checkFileMaxSize', V_REQUIRED),
                          ('isXMLFile', V_REQUIRED)),
            widget = atapi.FileWidget(label = _(u'label_xmlfile', default=u'XML File'),
                                description=_(u''),
                                show_content_type = False,)),

    BlobField('xslfile',
            required = True,
            searchable = False,
            accessor = 'getXSLFile',
            mutator = 'setXSLFile',
            index_method = 'getIndexValue',
            languageIndependent = True,
            storage = atapi.AnnotationStorage(migrate=True),
            default_content_type = 'application/octet-stream',
            validators = (('isNonEmptyFile', V_REQUIRED),
                          ('checkFileMaxSize', V_REQUIRED)),
            widget = atapi.FileWidget(label = _(u'label_xslfile', default=u'XSL File'),
                                description=_(u''),
                                show_content_type = False,)),

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
