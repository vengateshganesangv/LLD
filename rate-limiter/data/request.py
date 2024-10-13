from dataclasses import dataclass
@dataclass
class Request:
    user_id: str
    resource: str