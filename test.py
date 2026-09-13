from injector import inject, Injector


class A:
    name: str = "hello world"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(self.a.name)


injector = Injector()
print(injector.get(B).print())
