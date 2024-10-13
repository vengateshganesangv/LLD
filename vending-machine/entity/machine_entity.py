from custom_enum.vending_machine_state_enum import VendingMachineStateEnum

class Machine:
    _next_id = 1
    def __init__(self, state: VendingMachineStateEnum):
        self._id = Machine._next_id
        Machine._next_id += 1
        self._state = state

    @property
    def id(self) -> int:
        return self._id

    @property
    def state(self) -> VendingMachineStateEnum:
        return self._state

    @state.setter
    def state(self, value) -> None:
        self._state = value
    
    def __repr__(self) -> str:
        return str(self.__dict__)
