class EntryPoint:
    def __init__(self, name: str, is_open: bool):
        self._name = name
        self._is_open = is_open

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_open_status(self) -> bool:
        return self._is_open
