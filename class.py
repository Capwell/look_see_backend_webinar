class Course:
    def __init__(self, course):
        self.course = course

    def show(self):
        print(self.course)


backend = Course('Бэкенд разработка')
frontend = Course('Фронтенд разработка')

backend.show()
frontend.show()
