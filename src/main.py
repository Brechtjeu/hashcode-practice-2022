from parse import parse_input
from score import get_score
from output import write_output
import os

input_files = os.listdir("../inputs")



if __name__ == '__main__':

    input_filename = input_files[4]

    persons = parse_input(f'../inputs/{input_filename}')
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
    write_output(ingredients, input_filename)

