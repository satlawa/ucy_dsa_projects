#------------------------------------------------------#
#   problem 7 - Request Routing in a Web Server with a Trie
#------------------------------------------------------#

class RouteTrieNode:
    """ Represents a single node in the Trie. """
    def __init__(self):
        """ Initialize the node with children as before, plus a handler """
        self.handler = None
        self.children = {}

    def insert(self, path_part):
        """ Insert the node as before """
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


class RouteTrie:
    """ RouteTrie stores the routes and their associated handlers """
    def __init__(self, handler):
        """ Initialize the trie with an root node and a handler, this is the root path or home page node """
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path_parts, handler):
        """ Insert new nodes recursively with a handler on the leaf """
        current_node = self.root

        for path_part in path_parts:
            current_node.insert(path_part)
            current_node = current_node.children[path_part]

        current_node.handler = handler

    def find(self, path_parts):
        """ Serarches through the RouteTrie if path exists """
        current_node = self.root

        for path_part in path_parts:
            if path_part not in current_node.children:
                return None
            current_node = current_node.children[path_part]

        return current_node.handler


class Router:
    """ The Router class wraps the Trie and handle """
    def __init__(self, handler_root, handler_404):
        """ Initialize the Router by createing a new RouteTrie for holding our routes
            and add a handler for 404 page not found responses """
        self.router = RouteTrie(handler_root)
        self.handler_404 = handler_404

    def add_handler(self, path, handler):
        """ Adds a handler for a path """
        path_parts = self.split_path(path)
        self.router.insert(path_parts, handler)

    def lookup(self, path):
        """ Lookup path if it exists in Router """
        if path == '/':
            return self.router.handler
        elif path is None or type(path) is not str:
            return self.handler_404

        path_parts = self.split_path(path)

        found = self.router.find(path_parts)

        if found is None:
            return self.handler_404
        else:
            return found

    def split_path(self, path):
        """ splits the path into a list of path parts on '/' """
        path_parts = path.split(sep="/")
        return list(filter(None, path_parts))


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# Standard test cases
print(router.lookup("/"))
# 'root handler'
print(router.lookup("/home"))
# 'not found handler'
print(router.lookup("/home/about"))
# 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
# 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
# 'not found handler'

# Edge test cases
print(router.lookup(""))
# 'not found handler'
print(router.lookup(3))
# 'not found handler'
print(router.lookup(None))
# 'not found handler'
