#!/usr/bin/python3

'''
Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
'''
import request
from sys import argv


def main(id):
    '''
    Entry function to check details of the user via id passed in argv
    '''
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]


if __name__ == '__main__':
    '''Entry point of the program'''
    if argv:
        main(argv[1])
