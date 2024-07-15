coding:utf-8

from Art import logo


def play_game():
    print(logo)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    print("To start the adventure, you have to cross the forest of Hen.")

    direction_forest = input("You run through the forest of Hen and after 30 minutes you arrive at the seaside. Choose your path !\n 'left' or 'right' ?").lower()

    if direction_forest == 'left':
        direction_sea = input("You ran through the forest and arrived at the seaside. What is your decision ?\n 'pray' or 'swim' ?").lower()
        if direction_sea == 'pray':
            direction_castle = input("A spirit of the forest gives you the power to cross the sea. You arrive to the other side of the sea. You can see a big castle and you go towards it. You arrive in front of the  Windsor Castle ! The doors are open !\n 'enter' or 'knock'?").lower()
            if direction_castle == 'enter':
                choose_door = input("You enter the doors. You observe the entrance hall. There is nothing interesting. But you can see three doors in this room ! You can choose only one door !\n 'red', 'blue' , 'yellow' or 'another' ?").lower()
                if choose_door == 'yellow':
                    fight_moster = input("Unlucky !\n Behind this door, there was a big monster ! Next to him, there was a chest. You fought the monster and, after a very long fight, you decide to use a special move. To defeat the monster, you can choose one special move.\n 'SunnyYellow', 'JungleGreen' or 'UltraViolet' ?").lower()
                    if fight_moster == 'SunnyYellow':
                        open = input("A mini sun burns the monster. Congratulations, you have destroyed the monster ! You have access to the chest ! Do you want open the chest ?\n 'Y' or 'N'").lower()
                        if open == 'Y':
                            print("Congratulations, this is the end of your adventure !!! You open the chest and take the treasure.\n You win !")
                        else:
                         print("The bomb exploded !\n You are dead !\n Game Over ! ")
                         return False
                    elif fight_moster == 'JungleGreen':
                        print("A part of the Hen's strength unfolds in your body. You use this power and destroy the monster and the castle. Because of this power, everything is destroyed and the treasure too !\n You lose !\n Game Over ! ")
                        return False
                    elif fight_moster == 'UltraViolet':
                        print("This special move transforms you into a purple Power Ranger ! With the power of this costume, you kill the monster but the latter has a malediction which melts everything within a radius of 2km !\n You are dead !\n Game Over !")
                        return False
                    else:
                        print("Your strength leaves you because of the monster's curse which lasts 35 minutes. You end up shredded and dismembed by the monster !\n You are dead !\n Game Over ! ")
                        return False

                elif choose_door == 'red':
                    print("You open the door\n The fire of Hell devours your soul and your body !\n You are dead !\n Game Over !")
                    return False
                elif choose_door == 'blue':
                    print("You open the door\n The wolves smell your scent and attack you !\n You are dead !\n Game Over ! ")
                    return False
                else:
                    print("You wait. After 2 hours of waiting, you fall asleep to recover your strength. During the night, while you are asleep, the wandering souls of the castle possess your body and kill your soul !\n You are dead !\n Game Over !")
                    return False
            else:
                print("A pack of carnivore monkeys heard you knocking and attack you !\n You are dead ! Game Over !")
                return False
        else:
            print("After 10 minnutes of swimming, sharks attack you !\n You are dead !\n Game Over ! ")
            return False
    else:
        print("You chose the wrong path and the wandering souls of the forest eat your soul !\n You are dead !\n Game Over !")
        return False

while True:
    if not play_game():
        replay = input("Do you want to play again? Type 'yes' to play again or 'no' to quit: ").lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye!")
            break