import re
from helper_functions.storage import read_file


def extract_routes(text):
    find_route = r"/[a-zA-Z0-9_\-/]{2,}"
    find_decorator = "@.*route.*"
    route_lines = re.findall(find_decorator, text)
    routes = []
    for line in route_lines:
        route = re.findall(find_route, line)
        if route:
            routes.append(route[0])
    return routes


def extract_routes_from_file(filename):
    text = read_file(filename)
    results = extract_routes(text)
    return results
