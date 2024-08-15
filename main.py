#!/usr/bin/python3


# Data load function
def load_data():
    with open("data.txt") as f:
        # Read the data line by line. Remove the \n, split the line and convert the values to int
        histories = [list(map(int, line.rstrip().split())) for line in f]

    return histories


# A function so it's easier to organize the return values.
def pre_solver(history_layer):
    deeper_layer = history_solver(history_layer)
    return history_layer[-1] + deeper_layer[-1]


# A recursive function to solve the histories.
def history_solver(history_layer):
    # Helper var to stop before the last element in the list
    for_upto = len(history_layer) - 1

    # New layer to hold the temporary values of the history
    new_layer = []

    # C-like for so it's easier to exclude last element in list
    # Substract the history values from each other to get the new layyer
    # Store it in a new list
    for i in range(0, for_upto):
        new_layer.append(history_layer[i + 1] - history_layer[i])

    # Check if the newly created list holds different numbers or not
    # If not it means that the difference between the layer's numbers are 0
    # So the function can return
    if len(list(dict.fromkeys(new_layer))) != 1:

        # Recursive call until the difference is 0 between the numbers
        deeper_layer = history_solver(new_layer)

        # Append the new history layer values to the layer list
        new_layer.append(new_layer[-1] + deeper_layer[-1])

    return new_layer


if __name__ == "__main__":
    # Load the data from file
    histories = load_data()

    # The final sum of all the histories, that's the game's answer
    sum_of_all_histories = 0

    # Loop through the histories, and solve them.
    for history in histories:
        sum_of_all_histories += pre_solver(history)

    # The answer
    print(f"The combined sum of each history: {sum_of_all_histories}")
