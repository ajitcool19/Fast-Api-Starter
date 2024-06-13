from fastapi import APIRouter

from buisness_logic.buisness_logic_controller import BuisnessLogicController

router = APIRouter(prefix="/buisness-logic")
controller = BuisnessLogicController()

@router.get("/")
def read_root():
    return controller.get_data()



