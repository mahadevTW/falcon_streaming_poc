import falcon
from .images import Resource
from .images import ImageStore
api = application = falcon.API()
images = Resource(ImageStore())
api.add_route('/chunked-data', images)