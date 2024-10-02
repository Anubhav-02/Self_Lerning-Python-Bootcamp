line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? : ") 

# Convert letter (A, B, C) to column index (0, 1, 2)
col_index = ord(position[0].upper()) - ord('A')

# Convert number (1, 2, 3) to row index (0, 1, 2)
row_index = int(position[1]) - 1

# Place the "X" on the map at the calculated row and column
map[row_index][col_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")