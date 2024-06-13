
from buisness_logic.buisness_logic_crud import Crud

class BuisnessLogicController:
    def __init__(self):
        self.crud = Crud()

    def get_data(self):
        return "abc"