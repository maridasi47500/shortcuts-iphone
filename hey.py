from shortcuts import Shortcut, actions

# Create a Shortcut instance
sc = Shortcut()

# Define the actions for the shortcut
sc.actions = [
    actions.AskAction(data={'question': 'What is your name?'}),
    actions.SetVariableAction(data={'name': 'name'}),
    actions.ShowResultAction(data={'text': 'Hello, {{name}}!'})
]

# Serialize the shortcut to a file
with open("shortcut_output.toml", "w") as file:
    file.write(sc.dumps())


import subprocess

#hey="shortcuts sign --mode people-who-know-me --input ./MySC.shortcut --output MySigned.shortcut"
hey="shortcuts examples/what_is_your_name.toml what_is_your_name.shortcut"
subprocess.run(hey.split(" ")) 
# Save the shortcut as a .toml file
#sc.dump_toml("examples/what_is_your_name.toml")

# Save the shortcut as a .shortcut file
#sc.dumps("examples/what_is_your_name.shortcut")

