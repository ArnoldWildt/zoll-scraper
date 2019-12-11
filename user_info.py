users_filename = "users_file.txt"

class User:
    def __init__(self, name, email, distance):

        self.name = name
        self.email = email
        self.distance = distance

    def print_info(self):
        print(f"""\
            Name: {self.name}
            Email: {self.email}
            Distance: {self.distance}
        """)


def get_users():

    user_list = []
    
    with open(users_filename) as users_file:
        users = users_file.readlines()

    for _ in users:
        user_details = _.split(",")
        user_list.append(User(*user_details))

    return user_list
