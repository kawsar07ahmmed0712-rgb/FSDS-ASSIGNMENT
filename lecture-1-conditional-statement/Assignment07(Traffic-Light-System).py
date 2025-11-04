"""
Problem:
Ask the user to input a color (red, yellow, or green).
Print:
● "Stop" for red
● "Ready to go" for yellow
● "Go" for green
● "Invalid color" otherwise
"""

traffic_light = str(input("What is the color of the traffic light now:(red/green/yellow): "))

if traffic_light == "red":
    print("stop")
elif traffic_light == "yellow":
    print("Ready to go")
elif traffic_light == "green":
    print("You can safely go now ")
else:
    print("invalid color")