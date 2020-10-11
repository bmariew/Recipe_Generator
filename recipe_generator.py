import pandas as pd


def initial_input():
    response = input(
        '''
        Enter "New" if you would like to record a new recipe.
        Enter "Random" if you would like a randomly generated recipe.

        ''')
    return response.lower()


def add_recipe():
    name = input(
        '''
        Great! What is the name of the recipe you would like to add?

        ''')
    ingred = input(
        '''
        Please provide a comma separated list of ingredients needed to make {}.

        '''.format(name))
    ingred = ingred.split(',')

    instruct = input(
        '''
        Please provide a comma separated list of instructions need to make {}.

        '''.format(name))
    instruct = instruct.split(',')

    row = {'Recipe': name, 'Ingredients': ingred, 'Instructions': instruct}
    return row


df = pd.read_csv('recipes.csv', index_col=[0])

action = initial_input()
if action == 'new':
    new_row = add_recipe()
    df = df.append(new_row, ignore_index=True)
elif action == 'random':
    print('Great! Randomly generated recipe coming up!')
else:
    print('Sorry, that response is invalid')

df.to_csv('recipes.csv')
