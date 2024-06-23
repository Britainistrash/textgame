print("You look into the bombing optic, seeing flak bursts and shells below you. As Hiroshima gets closer and closer to the center of the bombing optic, the outcome of the war is in your hand, and you must decide now.")
input()
print("Do you drop the bomb, this will likely end the war, but thousands of people will die.")
input()
print("Or maybe you are too kind that you just can't forgive yourself for killing so many people.")
input()
Choice = input("There is not much time for you to think, you must make the choice now.")
input()
if Choice == "Yes".lower():
    print("You dropped the bomb.")
if Choice == "No".lower():
    print("You stopped for a second and ask yourself: We are all human, just why whould I do that to my own kind...")
elif Choice == "":
    print("You just can't decide if can get yourself to kill those people, and you suddenly realizes that you've already flown past Hiroshima. And you see a Mitsubishi KI-83 diving onto you.")
    Action = input("With the 30mm, the b29 instantly got shreded to pieces. You fall off the plane and start falling.")