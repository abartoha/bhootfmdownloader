import os

list_dir = os.listdir()
print(list_dir)

if list_dir.__contains__('test_name.txt'):
    print(list_dir[list_dir.index('test_name.txt')])
    os.rename('test_name.txt','new_test_name.txt')