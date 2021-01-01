#------------------------------------------------------#
#   problem 4 - Active Directory
#------------------------------------------------------#

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # check if Args have the right type
    if not isinstance(user, str) or not isinstance(group, Group):
        return False

    # variable to keep track if user was found
    found = False
    users = group.get_users()

    if user in users:
        return True
    else:
        groups = group.get_groups()
        index = 0
        # while there are still groups and user was not found
        while index < len(groups) and found == False:
            # call function recursively
            found = is_user_in_group(user, groups[index])
            index += 1

    return found


# creating structure (groups and users)
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

subchildren = ""

# standard test cases
print(is_user_in_group("sub_child_user", sub_child))
# True
print(is_user_in_group("Adam", sub_child))
# False

# edge test cases
print(is_user_in_group("", sub_child))
# False
print(is_user_in_group("sub_child_user", "subchild"))
# False
print(is_user_in_group("sub_child_user", subchildren))
# False
