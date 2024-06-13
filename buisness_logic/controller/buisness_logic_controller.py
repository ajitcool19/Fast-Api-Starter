from buisness_logic.Schema.create_student import CreateStudent
from buisness_logic.crud.buisness_logic_crud import Crud
from buisness_logic.models.student import Student


class BuisnessLogicController:
    def __init__(self):
        self.crud = Crud()

    def get_data(self, student_id):
        return self.crud.read(student_id)

    def create_data(self, create_student: CreateStudent):
        student = Student()
        student.name = create_student.name
        student.age = create_student.age
        return self.crud.create(student)
