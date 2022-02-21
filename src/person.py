
class Person():

    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes

    def would_eat_this_pizza(self,ingredients):
        return self.__has_all_likes(ingredients) and self.__has_no_dislikes(ingredients)

    def __has_all_likes(self, ingredients):
        if len(self.likes) > len(ingredients):
            return False
        else:
            return all(ingredient in ingredients for ingredient in self.likes)
    
    def __has_no_dislikes(self, ingredients):
        if len(self.dislikes) > len(ingredients):
            return not any(elem in self.dislikes  for elem in ingredients)
        else:
            return not any(elem in ingredients for elem in self.dislikes)


    def __repr__(self) -> str:
        return f"Person ({len(self.likes)},{len(self.dislikes)})"