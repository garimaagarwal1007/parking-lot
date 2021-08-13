import time

import initialize_data
from initialize_data import spots
from models.tickets import Ticket
import constants

TICKETS = dict()


def all_slots(level, vehicle):
    test = {}
    level = f'level-{int(level)}'
    if level in spots:
        if vehicle.upper() in spots[level]:
            test[level] = spots[level][vehicle.upper()]["free"]
    return test


def process_entry(level, vehicle_type, car_no):
    available_spots = all_slots(level, vehicle_type).get(f"level-{level}")
    if available_spots:
        ticket = Ticket(vehicle_type)
        ticket.vehicle_no = car_no
        ticket.spot = available_spots[0]
        print("Entry processed. \nYour ticket no. is", ticket.ticket_no)
        TICKETS[car_no] = ticket


def process_exit(vehicle_no):
    if vehicle_no in TICKETS:
        ticket_details = TICKETS.get(vehicle_no)
        ticket_details.out_time = time.time()
        ticket_details.status = constants.TicketStatus.ACTIVE
        time_diff = ticket_details.out_time - ticket_details.in_time
        print(time_diff)
    pass


if __name__ == "__main__":
    initialize_data.create_slots_data()
    process_entry(1, 'car', 'MH-04-GL-7207')
    process_exit('MH-04-GL-7207')
