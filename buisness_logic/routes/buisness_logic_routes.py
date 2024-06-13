from fastapi import APIRouter

from buisness_logic.Schema.create_student import CreateStudent
from buisness_logic.controller.buisness_logic_controller import BuisnessLogicController

router = APIRouter(prefix="/buisness-logic")
controller = BuisnessLogicController()

@router.get("/{id}")
def read_root(id : int):
    return controller.get_data(id)

@router.post("/")
def create_data(create_student: CreateStudent):
    return controller.create_data(create_student)



