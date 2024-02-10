# how_big_room.py

length = input('Enter the length of the room in meters: ')

width = input('Enter the width of the room meters: ')

square_met = float(length) * float(width)

square_ft = square_met * 10.7639

print(f'The room you described has an area of {square_met} square meters and {square_ft} square feet.')
