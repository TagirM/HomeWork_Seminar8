def get_name():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listName = []
        for line in f.readlines()[::10]:
            listName.append(line.rstrip('\n'))
        return listName


def get_number():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listNumber = []
        for line in f.readlines()[1::10]:
            listNumber.append(line.rstrip('\n'))
        return listNumber


def get_adres():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listAdres = []
        for line in f.readlines()[2::10]:
            listAdres.append(line.rstrip('\n'))
        return listAdres


def get_status():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listStatus = []
        for line in f.readlines()[3::10]:
            listStatus.append(line.rstrip('\n'))
        return listStatus


def get_birthday():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listBirthday = []
        for line in f.readlines()[4::10]:
            listBirthday.append(line.rstrip('\n'))
        return listBirthday


def get_facultet():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listFacultet = []
        for line in f.readlines()[5::10]:
            listFacultet.append(line.rstrip('\n'))
        return listFacultet


def get_kurs():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listKurs = []
        for line in f.readlines()[6::10]:
            listKurs.append(line.rstrip('\n'))
        return listKurs


def get_specialization():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listSpecialization = []
        for line in f.readlines()[7::10]:
            listSpecialization.append(line.rstrip('\n'))
        return listSpecialization


def what_to_do():
    with open('file.txt', 'r', encoding="utf-8") as f:
        listWtd = []
        for line in f.readlines()[8::10]:
            listWtd.append(line.rstrip('\n'))
        return listWtd


def general_information():
    listNumber = get_number()
    listAdres = get_adres()
    listStatus = get_status()
    listBirthday = get_birthday()
    listFacultet = get_facultet()
    listKurs = get_kurs()
    listSpecialization = get_specialization()
    listGeneral = listNumber
    for i in range(len(listGeneral)):
        listGeneral[i] = '\n' + listGeneral[i] + '\n' + listAdres[i] + '\n' + listStatus[i] + '\n' + \
            listBirthday[i] + '\n' + listFacultet[i] + '\n' + \
            listKurs[i] + '\n' + listSpecialization[i]
    return listGeneral


def export_book(book: dict):
    with open('newfile.txt', 'w', encoding="utf-8") as newfile:
        for key, value in book.items():
            newfile.write(f'\n{key}:{value}\n')
