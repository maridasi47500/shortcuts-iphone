import re
import json


def parse_actions_from_markdown(md):
    actions = []
    blocks = md.split("### ")[1:]
    for block in blocks:
        lines = block.strip().splitlines()
        name = lines[0].strip()
        keyword = re.search(r'\*\*keyword\*\*: `(.+?)`', block).group(1)
        identifier = re.search(r'\*\*shortcuts identifier\*\*: `(.+?)`', block).group(1)
        params = re.findall(r'\* (\w+) \(\*required\*.*?\)', block)
        defaults = {match.group(1): match.group(2) for match in re.finditer(r'\* (\w+) \(\*required\*, default=(.*?)\)', block)}
        actions.append({
            "name": name,
            "keyword": keyword,
            "identifier": identifier,
            "params": params,
            "defaults": defaults
        })
    return actions

def ask_when_run(actions):
    print("Available actions:")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action['name']} ({action['keyword']})")
    choice = int(input("Select an action by number: ")) - 1
    selected = actions[choice]
    print(f"\nYou selected: {selected['name']}")
    param_values = {}
    for param in selected["params"]:
        default = selected["defaults"].get(param)
        prompt = f"Enter value for '{param}'"
        if default:
            prompt += f" (default: {default})"
        value = input(prompt + ": ") or default or "{{ask_when_run}}"
        param_values[param] = value
    return {
        "action": selected["keyword"],
        "identifier": selected["identifier"],
        "params": param_values
    }


# Example usage
if __name__ == "__main__":
    with open("actions.md", "r") as f:
        md_text = f.read()

    actions = parse_actions_from_markdown(md_text)
    selected_action = ask_when_run(actions)
    print("\nFinal JSON:")
    print(json.dumps(selected_action, indent=2))

