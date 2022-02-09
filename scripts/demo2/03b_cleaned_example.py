class MyFriend:

    name = 'unknown'
    age = '20'

    def __init__(self, name):
        self.dayborn = 'Monday'

    @classmethod
    def getname(cls):
        print(f'My friends class attribute: name={cls.name}')

    @classmethod
    def getage(cls):
        print(f'My friends class attribute: age={cls.age}')


if __name__ == '__main__':

    special = MyFriend('Dave')
    special.getname()
    special.getage()
    print(special.__getattribute__('dayborn'))
