class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests = people
            self.is_taken = True
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"



class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result is None:
                    self.guests += people
                return result

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if result is None:
                    self.guests -= room.guests
                return result

    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")

from room import Room
from hotel import Hotel

hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)
hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)
hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)
hotel.print_status()

