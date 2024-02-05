def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def room_assigner(name, room):
    return f"Hello, {name}! You'll be assigned to room {room}!"

def assign_rooms(names):
    return [room_assigner(names[i], i + 1) for i in range(len(names))]

def printer(names):
    for mes in batch_badge_creator(names):
        print(mes)
    for mes in assign_rooms(names):
        print(mes)
