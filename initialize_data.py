

LEVEL_COUNT = 3
SPOT_COUNT = 10
VEHICLES = ['CAR', 'BIKE']
spots = {}


# initialize free spots for vehicle types
def create_slots_data():
    for i in range(1, LEVEL_COUNT + 1):
        level = f'level-{i}'
        for veh in VEHICLES:
            for sp in range(1, SPOT_COUNT + 1):
                if level not in spots:
                    spots[level] = {veh: {"free": [f'a-{sp}'], "taken": []}}
                elif level in spots and veh not in spots[level]:
                    spots[level][veh] = {"free": [sp], "taken": []}
                else:
                    spots[level][veh]["free"].append(f'a-{sp}')


def initialize_data():
    create_slots_data()
