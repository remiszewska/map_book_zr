users: list = [

    {"name": "Julia", "surname": "Gotowiec", "posts": 1500, },
    {"name": "Hubert", "surname": "Sybilski", "posts": 1000000, },
    {"name": "Adrian", "surname": "Dobrzański", "posts": 1, },

]

def read_friends(users: list)->None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')


read_friends(users)