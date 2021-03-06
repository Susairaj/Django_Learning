# Problem
# You want to sort objects of the same class, but they don’t natively support comparison
# operations.
# Solution
# The built-in sorted() function takes a key argument that can be passed a callable that
# will return some value in the object that sorted will use to compare the objects. For
# example, if you have a sequence of User instances in your application, and you want to
# sort them by their user_id attribute, you would supply a callable that takes a User
# # instance as input and returns the user_id . For example:

class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        print("User({})".format(self.user_id))
        return "User({})".format(self.user_id)
users = [User(23), User(3), User(99)]
print(users)
print(sorted(users,key=lambda u:u.user_id))
#oR
from operator import attrgetter
print(sorted(users,key=attrgetter('user_id')))