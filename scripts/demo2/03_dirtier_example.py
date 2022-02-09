class MyFriend:
    name = 'unknown'
    age = '20'

    def __init__(self):
        self.dayborn = 'Monday'

    @classmethod
    def getName(cls):
        print(f'My friends class attribute: name={cls.name}')
    @classmethod
    def getAge(cls):
        print(f'My friends class attribute: age={cls.age}')
if __name__ == '__main__':
    special = MyFriend()
    special.getName()
    special.getAge()

    print(special.__getattribute__('dayborn'))