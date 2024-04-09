class Tree:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def get_name(self):
        return self._name
class Palm(Tree): # Palm(Tree) means, Palm inherits Tree.
    def __init__(self, name, age, color):
        # First you have to initialize the parent class. What should we write 
        # Solution
        super().__init__(name, age)
        
        self._color = color
    def get_color(self):
        return self._color
def main():
    palm1 = Palm("Lucky", 30, "Green")
    print(palm1.get_name())  # What does this print (1)?
    print(palm1.get_color())  # What does this print (2)?
    tree1 = Tree("Funny", 20)
    print(tree1.get_name())  # What does this print (3)?
    print(tree1.get_color())  # What does this print (4)?
if __name__ == '__main__':
    main()