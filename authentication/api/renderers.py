import json
from rest_framework.renderers import JSONRenderer

from core.api.renderers import AuthJSONRenderer


class UserJSONRenderer(AuthJSONRenderer):
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):

        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return super().render(data)
