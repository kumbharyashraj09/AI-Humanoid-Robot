# AI Humanoid Robot Concept Project

print("AI Humanoid Robot Initialized")

def listen_command():
    return "move forward"

def process_command(command):
    if command == "move forward":
        return "Robot Moving Forward"
    return "Unknown Command"

command = listen_command()
result = process_command(command)

print(result)
