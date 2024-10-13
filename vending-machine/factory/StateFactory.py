from custom_enum.vending_machine_state_enum import VendingMachineStateEnum
from state.abstract_vending_machine_action import State
from state.ready_state import ReadyState
from state.product_display_state import ProductDisplayState
from state.products_details_reading import ProductsDetailsReading

class StateFactory:
    @staticmethod
    def get_state(state_name: VendingMachineStateEnum, vending_machine) -> State:
        if state_name == VendingMachineStateEnum.READY:
            return ReadyState(vending_machine)
        elif state_name == VendingMachineStateEnum.PRODUCT_DISPLAY:
            return ProductDisplayState(vending_machine)
        elif state_name == VendingMachineStateEnum.PRODUCT_DETAILS_READING:
            return ProductsDetailsReading(vending_machine)
        raise ValueError(f"Unsupported state: {state_name}")
