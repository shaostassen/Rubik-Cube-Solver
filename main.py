import kociemba

def solve_rubiks_cube(cube_state):
    # Ensure the cube_state string is correctly formatted
    assert len(cube_state) == 54, "Cube state must be a string of 54 characters."
    
    # Solve the Rubik's Cube using Kociemba's algorithm
    solution = kociemba.solve(cube_state)
    
    return solution

# Example: solved cube (white on top, red on front)
# cube_state = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
# solution = solve_rubiks_cube(cube_state)
# print("Solution:", solution)

def array_to_cube_string(cube_array):
    # Define your color mapping based on your array's color format
    color_mapping = {
        'white': 'U',
        'red': 'R',
        'green': 'F',
        'yellow': 'D',
        'orange': 'L',
        'blue': 'B'
    }
    
    # Convert the array to a string
    cube_string = ''.join([color_mapping[color] for color in cube_array])
    
    return cube_string

# Example usage with a sample array
cube_array = [
    'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
    'red', 'red', 'red', 'red', 'red', 'red', 'red', 'orange', 'red',
    'green', 'green', 'green', 'green', 'green', 'green', 'green', 'blue', 'green',
    'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow',
    'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'red', 'orange',
    'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'green', 'blue'
]

cube_state = array_to_cube_string(cube_array)
print("Cube state:", cube_state)
solution = solve_rubiks_cube(cube_state)
print("Solution:", solution)