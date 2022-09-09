import random

# Initial Question for user
question_response = int(input('How many dice would you like to roll? (1-6) '))

if question_response <= 6:
    number_of_dice = question_response
else:
    print('Enter a number between 1-6')
    raise SystemExit(1)

#Semi-random number generation
def roll_dice(number_of_dice):
    roll_results = []
    for _ in range(number_of_dice):
        roll= random.randint(1,6)
        roll_results.append(roll)
    return roll_results 

#Returns the dice results
roll_results = roll_dice(number_of_dice)

#ASCII dice face diagram [borrowed from RealPython.com]
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

#Generates a array of Dice Faces based on the ASCII diagrams 
# and the values of the random rolls
def generate_diagram(dice_value):

    dice_faces = []
    for value in dice_value:
        dice_faces.append(DICE_ART[value])

    dice_diagram = []
    for row in range(DIE_HEIGHT):
        row_comp = []           
        for dice in dice_faces:
            row_comp.append(dice[row]) 
        row_sep = DIE_FACE_SEPARATOR.join(row_comp)
        dice_diagram.append(row_sep)

    width = len(dice_diagram[0])
    diagram_header = " Roll Results ".center(width, "*")

    dice_face_diagram = "\n".join([diagram_header] + dice_diagram)
    return dice_face_diagram
#    
dice_face_final = generate_diagram(roll_results)

print(f"\n{dice_face_final}")


