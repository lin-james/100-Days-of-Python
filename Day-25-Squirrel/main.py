from ctypes import alignment
import pandas as pd
import turtle
IMAGE_URL = "./Day-25-Squirrel/blank_states_img.gif"
DATA_URL = "./Day-25-Squirrel/50_states.csv"
TITLE = "Guess the States"
PROMPT = "Input here"
ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")
# Set up U.S. map
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_URL)
turtle.shape(IMAGE_URL)

# Read U.S. States into list
data = pd.read_csv(DATA_URL)
all_states = data["state"].to_list()

# Text turtle
text = turtle.Turtle()
text.penup()
text.hideturtle()

# Gameplay loop
game_is_on = True
correct_states = []
correct_guess = 0
# User's answer input
user_input = screen.textinput(title=TITLE, prompt=PROMPT).title()
while game_is_on:
    # End game if user cancels
    if user_input == None:
        game_is_on = False

    if user_input in correct_states:
        user_input = screen.textinput(
            title=f"{correct_guess}/50 States Correct", prompt=PROMPT).title()
        continue
        # If state is correct
    if user_input in all_states:
        state_data = data[data["state"] == user_input]

        text.goto(int(state_data["x"]), int(state_data["y"]))
        text.write(user_input, align=ALIGNMENT, font=FONT)

        correct_states.append(user_input)
        correct_guess += 1

    user_input = screen.textinput(
        title=f"{correct_guess}/50 States Correct", prompt=PROMPT).title()

    if correct_guess == 50:
        game_is_on = False
        print("You Win")
# if df["state"] == user_input.title():
#     answer = df[df["state"] == user_input.title()]
#     print(answer)
turtle.mainloop()


# data = pd.read_csv("./Day-25-Squirrel/Squirrel_Data.csv")
# # print(data.columns)

# # print(data["Primary Fur Color"].value_counts())

# squirrel_count = data["Primary Fur Color"].value_counts()


# grey_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinn_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_count = len(data[data["Primary Fur Color"] == "Black"])

# print(grey_count)
# print(cinn_count)
# print(black_count)

# data_dict = {
#     "Fur Color": ["Grey", "Cinnamon", "Black"],
#     "Count": [grey_count, cinn_count, black_count]
# }

# df = pd.DataFrame(data_dict)
# df.to_csv("./Day-25-Squirrel/Squirrel_Count.csv")
