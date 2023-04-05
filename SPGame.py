'''
Jared Kerin 
7/25-12/18
A game that takes you traveling from point A to point B
'''
from termcolor import colored

def main():
    health = 100
    energy = 100
    money = 100
    text = colored('THE ADVENTURES OF SLIM PICKENS', 'red', attrs=['reverse', 'blink'])
    print(text)
    print("Your name is Slim Pickens, a retired cowboy living on a ranch with your wife in the South West.\nOn a quiet day, old enemies from a a past life show up at your ranch and kidnap your wife.\nYou must travel from your home in Texas and follow the trail of your enemies and save your wife\nEvery choice you make along the way will have an impact on if you succeed in saving her or not. \nYour choices will determine your\nHEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
    print("You are in a rush to leave and see a few items just outside your house \nWhat will you bring with you?")
    text = colored(' A) a knife\n B) extra water\n C) a cooking pot\n D) extra money', 'yellow', attrs=['blink'])
    print(text)
    gear = input("Please enter what you would like to bring with you:")
    if gear.lower() == "a":
        print("You brought your knife, +25 ENERGY")
        energy = energy + 25
    elif gear.lower() == "b":
        print("You brought extra water, +25 ENERGY")
        energy = energy + 25
    elif gear.lower() == "c":
        print("You brought your pot, +30 ENERGY")
        energy = energy + 30
    elif gear.lower() == "d":
        print("You brought extra money, +100 MONEY")
        money = money + 100
    print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
    print("You have come across your hometown and you feel like you could use some more supplies\nWould you like to buy anything?")
    print("What would you like to buy")
    text = colored(' A) A revolver $150 \n B) Coffee $25 \n C) Medicine $100 \n D) Fire starter $50\n E) Nothing', 'yellow', attrs=['blink'])
    print(text)
    town1ans = input("Enter what you would like to buy?:")
    if town1ans.lower() == "a":
        if money >= 150:
            print("You bought a revolver, -100 MONEY, +50 ENERGY")
            money = money - 150
            energy = energy + 50
        elif money < 150:
            print("You couldn't afford the revolver, lets just move on...")
    elif town1ans.lower() =="b":
        print("You bought coffee, -25 MONEY, +50 ENERGY, + 5 HEALTH")
        money = money - 25
        energy = energy + 50
        health = health + 5
    elif town1ans.lower() == "c":
        print("You bought medicine, -100 MONEY, +30 ENERGY")
        money = money - 100
        energy = energy + 30
    elif town1ans.lower() == "d":
        print("You bought a fire starter, -50 MONEY, + 25 ENERGY")
        money = money - 50
        energy = energy + 25
    elif town1ans.lower() == "e":
        print("You bought nothing.")
    print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
    print("You continue on your journey.\nComing up is a pathway through what looks like an old town engulfed by forest, You could cut through using the path or go around not know how far out the forest goes:")
    text = colored(' A) Go Around \n B) Cut Through', 'yellow', attrs=['blink'])
    print(text)
    directions = input("Where will you travel:")
    if directions.lower() == "a":
        print("You decide to go around, -30 energy")
        energy = energy - 30
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("You have been moving for quite some time now, and are starting to feel fatigued\nYou see some wild plants that look edible, should you try to eat them?")
        text = colored(' A) Try them\n B) Keep going', 'yellow', attrs=['blink'])
        print(text)
        decision1 = input("What will you do?:")
        if decision1.lower() == "a":          
               print("The plants in fact tasted great, you're feeling much better!\n+25 energy")
               energy = energy + 25       
        if decision1.lower() == "b":
           health = health - health
    elif directions.lower() =="b":
        print("You decide to cut through")
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("You have been seen by a wild bear, what will you do?")
        text = colored(' A) Run away\n B) Fight it', 'yellow', attrs=['blink'])
        print(text)
        decision2 = input("What will you do?:")
        if decision2.lower() == "a":
            if energy >= 150:
                print("Good job, you made it. -25 ENERGY")
                energy = energy - 25
            elif energy < 150:
                print("You made it, but you were injured while running. -15 HEALTH, -30 ENERGY")
                health = health - 15
                energy = energy - 30
        if decision2.lower() == "b":
            if energy >= 125:
                print("Good job, you defeated the bear.")
            elif energy >60:
                print("You defeated the bear, but you were hurt. -15 HEALTH, -10 ENERGY")
                health = health - 15
            elif energy <60:
                print("You barely escaped with your life. -25 HEALTH, -25 ENERGY")
                health = health - 25
                energy = health - 25
    if health <= 0:
        print("Its too hot out, I have no energy, it looks like this is the end...\nYOU HAVE DIED GAME OVER")
    else:
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("It is starting to get dark you should set up camp")
        print("Do you want to hunt and possibly get your energy back?:")
        text = colored(' A) Yes\n B) No', 'yellow', attrs=['blink'])
        print(text)
        hunt1 = input("Will you hunt?:")
        if hunt1.lower() == "a":
            print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
            print("Do you want to go:")
            text = colored(' A) Right \n B) Left', 'yellow', attrs=['blink'])
            print(text)
            direction = input("Which way?")
            if direction.lower() == "a":
                print("You were able to shoot down a small bird and have a nice meal, heath +20, energy +15")
                health = health + 20
                energy = energy + 15
            elif direction.lower() == "b":
                print("After a long hike you found no food, -25 ENERGY")
                energy = energy - 25
            elif hunt1.lower() == "b":
                print("You stayed at camp and went to sleep")
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("You are amazed at how far you made it the first day.\nIt must have been the adreneline.")
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("You wake up the next day feeling sick...\nShould you use your resources to maybe feel better?:")
        text = colored(' A) Yes \n B) No', 'yellow', attrs=['blink'])
        print(text)
        morning1 = input("Is it worth it?")
        if morning1.lower() == "a":
                if energy >= 105:
                    print("You feel better now, -10 ENERGY, +10 HEALTH")
                    energy = energy - 10
                    health = health + 10
                elif energy < 105:
                    print("That definetly did not work, -20 ENERGY, -30 HEALTH")
                    health = health - 30
                    energy = energy - 20
        if morning1.lower() == "b":
                print(" you didn't want to try to fix your problem you still don't feel to good, -20 HEALTH")
                health = health -20
        print("Its time to keep moving, you can spot a small town in the distance lets head in that direction...")
        print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
        print("You reach the town and enter a small saloon to maybe get some information...after some time of asking around a small man approaches you and tells you he has what you are looking for...")
        text = colored(' A) Yes \n B) No', 'yellow', attrs=['blink'])
        print(text)
        information1 = input("Should you go with him?")
        if information1.lower() == "a":
            print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
            print("The man brings you into a building and into a small office like room...He claims he can give you all the information you need if you give him all your money.")
            text = colored(' A) Give him the cash\nB) Pull out your gun and then see what he says\nC) Run', 'yellow', attrs=['blink'])
            print(text)
            information2 = input()
            if information2.lower() == "a":
                print("You give the man all you cash...he thanks you for your bussines as you are escorted out by two large men with rifles")
                money = money - money
            elif information2.lower() == "b":
                if energy >= 100:
                    print("You pull your gun on the man he says I thought you might do that...as you hear footsteps running toward the room you run at the man and kick him over as you make a risky leap out the window as his men start to shoot at you...barely escaping with your life you make for your horse and get out of the town, -10 HEALTH")
                    health = health - 10
                elif energy < 100:
                    print("You pull your gun on the man he he says I thought you might do that...as you hear footsteps running toward the room you hesitate and then try to run at the man but it was to late you were caught, -130 HEALTH")
                    health = health - 130
            elif information2.lower() == "c":
                print("You tried to run away but was stoped by two large men with riffles who take your money and most of your gear...They supprisingly let you go and you mount your horse to leave")
                energy = energy - 50
                money = money - money
        if information1.lower() == "b":
            print("You decided to not go with him, you feel as if this is a good choice when you hear gun shots from a building you later see the man walk into")
        if health <= 0:
            print("YOU HAVE DIED. GAME OVER.")
        else:
            print("You come across what looks like an accident between stage coaches, but are skeptical about helping because the victims seem to be holding guns,so you decide not to stop for fear of being robbed, or worse.")
            print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
            print("A man comes up to you and tries to rob you. Do you...")
            text = colored(' A) Fight him\nB) Give him 100 dollars to leave you alone', 'yellow', attrs=['blink'])
            print(text)
            robber = input()
            if robber.lower() == "a":
                if energy >= 120:
                    print("You were quick to defeated the robber and you took his money and gear. +100 MONEY, +10 ENERGY ")
                    money = money + 100
                    energy = energy + 10
                elif energy < 120:
                    print("You injured the robber, and he decided to run away and leave you alone. - 20 ENERGY")
                    energy = energy - 20
            elif robber.lower() == "b":
                if money >= 100:
                    print("You gave the robber 100 dollars to leave you alone.")
                    money = money - 100
                elif money < 100:
                    print("You didn't have enough money to pay the robber, so he beat you up.")
                    health = health - 15
                    energy = energy - 20
            print("HEALTH:", health,",ENERGY:", energy, ",MONEY:", money)
            print("You see a town in the distance, do you want to go check it out?") 
            text = colored(' A) Yes\nB) No', 'yellow', attrs=['blink'])
            print(text)
            abandonedtown = input()
            if abandonedtown.lower() == "a":
                print("You go to the town and discover that it is being raided. Do you want to...") 
                text = colored('  A) Join in on the raiding and try to get supplies\nB) Help some families get out and then leave\nC) Run")', 'yellow', attrs=['blink'])
                print(text)
                choice1 = input()
                if choice1.lower() == "a":
                    print("You have been shot by one of the robbers and are fatally injured.")
                    health = health - 100
                elif choice1.lower() == "b":
                    if energy >= 75:
                        print("You helped the families escape the town and suffered no casualties\n they want say thank you and give you some supplies.")
                        energy = energy + 20
                        health = health + 20
                        money = money + 200
                    elif energy < 75:
                        print("You helped the families escape, but were hurt along the way. The families give you medicine and some supplies as thanks.")
                        health = health + 10
                        energy = energy + 10
                        money = money + 150
                elif choice1.lower() == "c":
                    print("You ran away from the town as fast as you could, and somehow find money on the ground.")
                    energy = energy - 10
                    money = money + 150
            if abandonedtown.lower() == "b":
                print("You decided to not stop, but you find a wad of cash on the ground.")
                money = money + 150
            if health <= 0:
                print("You have died. Game over.")
            else:
                print("Your health is", health, ", Your energy is", energy, ", Your money is", money, ".")
                print("You continue on your journey, and you can tell that you're almost there.")
                print("Its time to set up camp again, and you are so tired from the day that you decide not to hunt.")
                print("You wake up the next morning feeling well rested.")
                print("You continue your journey.")
                print("You make it to the last town where you can stock up on supplies, weapons, and gear. Seeing as it is a developed town, everything you can buy here is extremely better than what you have, but it costs more money.")
                print("You walk into the store, what would you like to buy\n A) Dual highly advanced revolvers with cool hat, boots, and cowboy outfit $250\n B) Advanced rifle with more modern outfit, jacket, hat, and boots $250")
                finalchoice = input()
                if finalchoice.lower() == "a":
                    print("You bought the dual revolvers and cowboy outfit, and you feel like you did back in your glory days of being a cowboy.")
                    money = money - 250
                    health = health + 100
                    energy = energy + 100
                if finalchoice.lower() == "b":
                    print("You bought the rifle and modern outfit, and you feel like you can take on anybody.")
                    money = money - 250
                    health = health + 100
                    energy = energy + 100
                print("On your way out you see a man and ask him if he has seen a gang of cowboys go by, he then tells you that they are heading for a nearby train station.")
                print("You get on your horse and go to the train station as fast as you can.")
                print("You see the train station and notice a small building next to to that appears to have your wife and her kidnappers inside of it. Do you\n A) Charge into the building and take them all on at once\n B) Wait for them to come out of the building so you can take them on one by one\n C) Wait on the train to surprise the enemy who is bringing your wife on the train while the other enemies keep guard outside of the train")
                finalbattle = input("What's the plan")
                if finalbattle.lower() == "a":
                    print("You charge into the building like a madman and get shot by one of the robbers. You manage to take them out before you pass out, and the last thing you see before everything fades to black is your wife, smiling, saying thank you and telling you how much she loves you.")
                elif finalbattle.lower() == "b":
                    print("you waited a long time for the men to come outside,when they do you take them out one by one with little injurys\nyou are able to save your wife but realize there was one more person left, your best friend walks out of the train and tell you this had to be done\n you relize that there is no other choice so you draw your gun as he does, he misses the shot..... you don't")
                elif finalbattle.lower() == "c":
                    print("You hide on the train and wait for one of the kidnappers to bring your wife on board. When you see who the kidnapper is, you are astonished as you realize that it is your old best friend, and the only person who you trusted enough to tell the location of your ranch. As you jump out of the shadows to do what has to be done once and for all, you can see the sadness in his eyes. He appologizes while he draws his weapon, but you make like Han Solo the famous space cowboy and shoot first. You then hug your wife and make your way to wherever the train is taking you to start a new, peaceful life away from all of this.")
                    text1 = colored('Congratulations! You have beaten the game! The End!', 'blue', attrs=['reverse', 'blink'])
                print(text1)
main()       