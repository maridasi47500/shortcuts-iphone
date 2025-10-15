from shortcuts import Shortcut, actions

# Create a Shortcut instance
sc = Shortcut()

# Define the actions for the shortcut
sc.actions = [
    actions.AskAction(data={'question': 'What is your name?'}),
    actions.SetVariableAction(data={'name': 'name'}),
    actions.ShowResultAction(data={'text': 'Hello, {{name}}!'})
]

## Serialize the shortcut to a file
#with open("shortcut_output.toml", "w") as file:
#    file.write(sc.dumps())
#    #shortcuts examples/what_is_your_name.toml what_is_your_name.shortcut
#
## Save the shortcut as a .toml file
#sc.dump_toml("examples/what_is_your_name.toml")

# Save the shortcut as a .shortcut file
sc.dump_shortcut("examples/what_is_your_name.shortcut")

