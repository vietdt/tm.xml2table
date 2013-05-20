from mimetypes import guess_type

from zope.interface import implements
from ZPublisher.HTTPRequest import FileUpload

from Products.validation.interfaces.IValidator import IValidator
from Products.validation.config import validation

class MimetypeValidator:
    """
    Validate the mimetype of uploaded file
    """

    implements(IValidator)

    def __init__(self, name, mime=''):
        self.name = name
        self.mime = mime

    def __call__(self, value, *args, **kwargs):
        # calculate mimetype
        if isinstance(value, FileUpload):
            content_type = value.headers.get('content-type')
        elif isinstance(value, file) or hasattr(aq_base(value), 'filename'):
            content_type = guess_type(value.filename)
        else:
            content_type = None

        if content_type and 'xml' not in content_type:
            return "Validation failed: Uploaded file is not a XML file"
        return True


validation.register(MimetypeValidator('isXMLFile', 'xml'))