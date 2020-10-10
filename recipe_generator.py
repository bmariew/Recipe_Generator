import pandas as pd

df = pd.read_csv('recipes.csv', index_col=[0])
#df = pd.DataFrame(columns=['Recipe', 'Ingredients', 'Instructions'])

taco = {'Recipe': 'tacos2', 'Ingredients': ['beef', 'tortilla shells'], 'Instructions': [
    '1. Brown beef', '2. Add taco seasoning']}
df = df.append(taco, ignore_index=True)
pasta = {'Recipe': 'pasta2', 'Ingredients': ['1 jar of pasta sauce', '1 box of noodles'], 'Instructions': [
    '1. boil water', '2. boil nooods for 10 minutes']}
df = df.append(pasta, ignore_index=True)
waffles = {'Recipe': 'waffles2', 'Ingredients': [
    'waffles', 'syrup'], 'Instructions': ['1. Toast waffle', '2. Pour syrup']}
df = df.append(waffles, ignore_index=True)
print(df.head())
df.to_csv('recipes.csv')
