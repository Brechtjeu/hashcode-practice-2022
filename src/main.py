from parse import parse_input

if __name__ == '__main__':

    persons = parse_input('../inputs/a_an_example.in.txt')
    print(persons)

    scores = dict()

    for person in persons:

        for like in person.likes:
            if like in scores:
                scores[like] += 1
            else:
                scores[like] = 1
            
        for like in person.likes:
            if like in scores:
                scores[like] -= 1
            else:
                scores[like] = -1

    ingredients = [ingredient for ingredient, score in scores.items() if score > 0]
    print(ingredients)

