from dataclasses import dataclass, field
@dataclass
class OrderItemEntity:
    id: int
    pizza_id: int
    topping_ids: list[int] = field(default_factory=list)