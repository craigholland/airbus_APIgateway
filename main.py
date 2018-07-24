"""`main` is the top level module of airbus Shopping Gateway API."""

# Import the Pyramid Framework
from pyramid.config import Configurator
from pyramid.response import Response

import os


config = Configurator()


def root_page(request):
    """Main Page."""
    env = ''
    for k, v in os.environ.iteritems():
        env += '{0}: {1}<br>'.format(k, v)
    return Response(env)


_routes = [
    ('root', '/', root_page)
]

routes =  _routes
for route in routes:
    name, uri, handler = route
    config.add_route(name, uri)
    config.add_view(handler, route_name=name)

app = config.make_wsgi_app()
