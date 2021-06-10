from initialize_data import spots

def all_slots(level, vehicle):
    test = {}
    level = f'level-{int(level)}'
    if level in spots:
        if vehicle.upper() in spots[level]:
            test[level] = spots[level][vehicle.upper()]["free"]
    return test



