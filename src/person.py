
class Person():

    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes


    def __repr__(self) -> str:
        return f"Person who\r\n    likes: {self.likes}\r\n   dislikes: {self.dislikes}\r\n"