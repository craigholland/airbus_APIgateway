"""`main` is the top level module  of airbus Gateway."""

# Import the Pyramid Framework
from pyramid.config import Configurator
from pyramid.response import Response


config = Configurator()


def root_page(request):
    """Main Page."""

    return Response('Fuck Off World API')


_routes = [
    ('root', '/', root_page)
]

routes =  _routes
for route in routes:
    name, uri, handler = route
    config.add_route(name, uri)
    config.add_view(handler, route_name=name)

app = config.make_wsgi_app()
