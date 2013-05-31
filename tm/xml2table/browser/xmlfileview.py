import os
from cStringIO import StringIO
from lxml import etree

from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from tm.xml2table import xml2tableMessageFactory as _


class IXMLFileView(Interface):
    """
    XMLFile view interface
    """


class XMLFileView(BrowserView):
    """
    XMLFile browser view
    """
    implements(IXMLFileView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self):
        """
        render the html table from xml file using a xsl template
        """
        # get default xsl file
        current_path = os.path.abspath(os.path.dirname(__file__))
        xsl_file = self.context.getXSLFile()
        try:
            xslt = etree.XSLT(etree.parse(StringIO(xsl_file.data)))
        except etree.XMLSyntaxError:
            return 'XSL data is invalid.'
        # get xml data
        xmlfile = self.context.getXMLFile()
        try:
            xml = etree.fromstring(xmlfile.data)
        except etree.XMLSyntaxError:
            return 'XML data is invalid.'
        # transform to html
        html = xslt(xml)
        return etree.tostring(html)
