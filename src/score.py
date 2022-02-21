def get_score(ingredients, persons):
    score = 0
    for person in persons:
        if person.would_eat_this_pizza(ingredients):
            score += 1
