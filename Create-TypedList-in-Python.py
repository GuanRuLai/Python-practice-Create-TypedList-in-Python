class TypedList(list):
    def __init__(self, example_ele, initial_list):
        self.type = type(example_ele)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for ele in initial_list:
            self.__check(ele)
        super().__init__(initial_list)
    def __check(self, ele):
        if type(ele) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a TypedList.")
    def __setitem__(self, i, ele):
        self.__check(ele)
        super().__setitem__(i, ele)
    def __getitem__(self, i):
        return super().__getitem__(i)

x = TypedList("hello", ["some", "original", "stuff"])
y = TypedList("", [""] * 5)
y[3] = "15"
y[4] = "hello"
print(x)
print(y)
print(x + y)
#%%
