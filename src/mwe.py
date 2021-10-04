class Sliceable:
    def __getitem__(self, _):
        return (0, 1, 2)

sliceable = Sliceable()


def func(x=sliceable[:]):
    """We want the parameter x to be documented as :code:`sliceable[:]`, not :code:`(0,1,2)`. """
    print(x)
