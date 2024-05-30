## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

#*args = unlimited positional argument, **kwargs unlimited keyword arguments
#args[0] 1st positional argument
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User('Aaron')
new_user.is_logged_in = True
create_blog_post(new_user)

print(new_user.__str__())