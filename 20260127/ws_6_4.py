# 아래 함수를 수정하시오.
def get_keys_from_dict(dict1):
    return list(dict1.keys())

def get_all_keys_from_dict(dictionary):
    
    dict_list = []
    for key in dictionary:
        dict_list.append(key)
        if type(dictionary[key]) == dict:
            sub_keys = get_all_keys_from_dict(dictionary[key])
            dict_list.extend(sub_keys)
    return dict_list    

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']


