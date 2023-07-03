def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

# auxiliary function
def welcome_message (name, room_num):
    return (f"Hello, {name}! You'll be assigned to room {room_num}!")

def assign_rooms(names):
    room = 1 
    welcome_messages = []
    for name in names :
        welcome_messages.append(welcome_message(name, room))
        room += 1
    return welcome_messages

def printer(names):
    messages = assign_rooms(names)
    for name in names :
        print (badge_maker(name))
    for message in messages :
        print (message)

