# welcome_stranger.py

my_list = ["John", "Q", "Doe"]
my_dict =  {"title": "Master", "occupation": "Plumber"}

def welc_strang(list_1, dict_1):
    print(f'Hello, {list_1[0]} {list_1[1]} {list_1[2]}! Nice to have a {dict_1["title"]} {dict_1["occupation"]}.')
    
greeting = welc_strang(my_list, my_dict)
print(greeting)