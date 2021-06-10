import datetime
import random
import constants


class Ticket:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.in_time = datetime.datetime.now()
        self.out_time = None
        self.status = constants.TicketStatus.ACTIVE
        self.spot = None
        self.ticket_no = f'{random.randrange(1, 10**3):05}'
        self.payment = None
