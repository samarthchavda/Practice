class User:
    def create(self):
        print('user created')


class Student(User):
    def create(self):
        super().create()
        print('student created')