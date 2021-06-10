from enum import Enum


class TicketStatus(Enum):
    ACTIVE = 1
    EXPIRED = 2


class VehicleType(Enum):
    CAR = 1
    BIKE = 2


class SlotType(Enum):
    FREE = 1
    TAKEN = 2
