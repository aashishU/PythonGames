def choice_3(c3):
    valid = False
    while not valid:
        if c3 == "SHORTER":
            print("You found people camping. They immediately called in and You got rescued")
            print("Congratulations....You survived the Jungle Safari..!!")
            break

        elif c3 == "LONGER":
            print("You ran into a group of wild pigs and they killed you.")
            print("Really an embarrassing way to die.")
            print("!__GAME OVER__!")
            break

        else:
            print("Type a valid choice.")
            valid = True


def choice_2(c2):
    valid = False
    while not valid:
        if c2 == "SWIM THROUGH":
            print("You got bit by a water snake but don't worry they are not poisonous.")
            print("On the top of a hill, you spot lights and movement.")
            print("There are two paths leading there, one is through the hill but short,")
            print("another is the road, longer path.")
            c3 = input("Longer/Shorter : ")
            c3 = c3.upper()
            return choice_3(c3)

        elif c2 == "GO AROUND":
            print("There was a lion waiting for you in the bushes and you died.")
            print("!__GAME OVER__!")
            break

        else:
            print("Type a valid choice")
            valid = True


def choice_1(c1):
    valid = False
    while not valid:
        if c1 == "LEFT":
            print("After walking about an hour and a half, you reached at a lake.")
            c2 = input("Go around/Swim through :")
            c2 = c2.upper()
            return choice_2(c2)

        elif c1 == "RIGHT":
            print("You walked ten hours straight but reached nowhere and died out of thirst")
            print("!__GAME OVER__!")
            break

        else:
            print("Type a valid choice")
            valid = True


def story():
    print("You went for jungle safari and got separated from the group.\nThere are two paths in front of you.")
    c1 = input("Left/Right :")
    c1 = c1.upper()
    return choice_1(c1)


def age_control(name, age):
    if age > 12:
        print("You are allowed to play the game " + name)
        story()
    else:
        print("You are too young to play this game " + name + ". Its life threatening.")


def play_game():
    print("Welcome to the world of choices.")
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    return age_control(name, age)


play_game()
