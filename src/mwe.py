class Sliceable:
    def __getitem__(self, index):
        return (0, 1, 2)

sliceable = Sliceable()

def func(x=sliceable[:]):
    print(x)
