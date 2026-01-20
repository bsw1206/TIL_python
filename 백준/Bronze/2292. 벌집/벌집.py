T = int(input())
room_number = 1
passed_room = 1
while (T > room_number):
    room_number += 6 * passed_room
    passed_room += 1
print(passed_room)	