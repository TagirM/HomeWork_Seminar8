from argparse import Action


name = []
information = []
action = []
inf_book = {}


def init(person_name, info):
    global name
    global information
    global action
    name = person_name
    information = info


def create_new_note(person_name: list, note: dict, info: list):
    note[person_name] = info
    return note


def create_new_list(person_name: list, book: dict):
    book[person_name[0]] = ''
    return book


def update_note(person_name: list, note: dict, info: list):
    note[person_name] = info
    return note


def delete_note(person_name: list, note: dict):
    del note[person_name]
    return note
