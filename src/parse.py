from person import Person


def parse_input(file_name):

    persons = []

    with open(file_name) as file:
        nb_persons = int(file.readline())

        for i in range(nb_persons):
            likes = file.readline().split()[1:]
            dislikes = file.readline().split()[1:]
            persons.append(Person(likes, dislikes))

    return persons

