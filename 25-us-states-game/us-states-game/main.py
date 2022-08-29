import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)
# Background image
image = "/home/pauline/projets/python/python_bootcamp/25-us-states-game/us-states-game/blank_states_img.gif"
# need .bgpic() AND .addshape() for the background to work !
screen.bgpic(image)
screen.addshape(image)
# add the background modified by the player
turtle.shape(image)

""" Reaching datas """
data = pandas.read_csv("25-us-states-game/us-states-game/50_states.csv")
print(data)
data_list = data["state"].tolist()
states_to_learn_list = data_list

""" Iniate variables """
correct_guesses = []
score = 0


def player_input():
    answer_state = screen.textinput(
        title=f"{score}/50 States correct", prompt="What's another state's name ?")
    return answer_state.capitalize()


def write_state_on_map(x, y, state):
    turtle.penup()
    turtle.hideturtle()
    turtle.color("black")
    turtle.goto(x, y)
    turtle.write(f"{state}")


def already_guessed(guess):
    is_guessed = False
    if guess in correct_guesses:
        is_guessed = True
    return is_guessed


def create_dataframe_states_to_learn():
    data_dict = {"state": states_to_learn_list}
    data = pandas.DataFrame(data_dict)
    data.to_csv("25-us-states-game/us-states-game/states_to_learn.csv")


while len(correct_guesses) < 50:
    player_guess = player_input()
    if player_guess in data_list and not already_guessed(player_guess):
        # find coordonates of the state guessed
        data_row = data[data.state == player_guess]
        data_row_list = data_row.values[0]
        new_x = data_row_list[1]
        new_y = data_row_list[2]
        new_state = data_row_list[0]
        write_state_on_map(new_x, new_y, new_state)
        correct_guesses.append(new_state)
        score += 1
        states_to_learn_list.remove(player_guess)
    # to exit game
    if player_guess == "Exit":
        create_dataframe_states_to_learn()
        break



# !!! IMPORTANT How to keep window open on click !!!
# to have .mainloop() or exitonclick() or a screen.textinput() for the window to work and open 
#turtle.mainloop()
#screen.exitonclick()
