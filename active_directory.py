from queue import Queue 

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
    if group is None:
        return False
    
    q = Queue()
    q.put(group)
    
    while not q.empty():
        current_group = q.get()
        
        for subgrup in current_group.groups:
            q.put(subgrup)
        
        if user in current_group.users:
            return True
        
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_user("parent1")

#Test case 1
print(is_user_in_group("sub_child_user", sub_child)) # expected True

#Test case 2
print(is_user_in_group("sub_child_user", parent)) # expected True

#Test case 3
print(is_user_in_group("parent1", sub_child)) # expected False

#Test case 4
parent = None
print(is_user_in_group("parent1", parent)) # expected False
    
