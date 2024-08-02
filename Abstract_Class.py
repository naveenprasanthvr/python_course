class fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def rich_in(self):
        return "Vitamin A"
    def colour(self):
        return "Yellow"
class orange(fruit):
    def taste(self):
        return "sour"
    def rich_in(self):
        return "Vitamin C"
    def colour(self):
        return "Orange"
        
A = mango()
print(A.taste(),A.rich_in(),A.colour())
O = orange()
print(O.taste(),O.rich_in(),O.colour())