from user_management.models.user import User


class Crud:
    def __init__(self, session):

        self.session = session

    def create(self, user: User):

        if self.session.query(User).filter(User.email == user.email).first():
            return {
                "message": "User already exists",
                "status": 409
            }

        self.session.add(user)

        try:
            self.session.commit()
            self.session.refresh(user)

        except Exception:
            self.session.rollback()
            raise
        return user.id

    def read(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def read_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()
