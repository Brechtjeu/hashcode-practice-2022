def get_score(ingredients, persons):
    return sum(1 for person in persons if person.would_eat_this_pizza(ingredients))
