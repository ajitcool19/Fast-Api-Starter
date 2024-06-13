from buisness_logic.models.student import Student
from common.database.database_config import context_aware_session


class Crud:
    def __init__(self):
        pass

    def create(self, student: Student):
        saved_data = context_aware_session().add(student)

        try:
            context_aware_session().commit()
        except Exception:
            context_aware_session().rollback()
            raise
        return saved_data


    def read(self, student_id: int):
        return context_aware_session().query(Student).filter(Student.id == student_id).first()

    def update(self):
        pass

    def delete(self):
        pass