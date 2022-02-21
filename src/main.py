from parse import parse_input
from score import get_score

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
            
        for dislike in person.dislikes:
            if dislike in scores:
                scores[dislike] -= 1
            else:
                scores[dislike] = -1

    ingredients = [ingredient for ingredient, score in scores.items() if score > 0]
    print(ingredients)
    print(get_score(ingredients, persons))

