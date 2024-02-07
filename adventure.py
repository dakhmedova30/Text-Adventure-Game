"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player
import time
from typing import Optional
import playsound

# Note: You may add helper functions, classes, etc. here as needed
places = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0}

your_name = ''

water_grab = False
water_drop = False
tcard_grab = False
tcard_drop = False
sheet_grab = False
sheet_drop = False
pen_grab = False
pen_drop = False

visited_bumbly_mia = False
visited_kyoko_tomoyo_pocoyo = False
visited_chirly = False
visited_negativity_room = False
visited_purple_guy = False
visited_connor = False
visited_tiffany = False
visited_tikki_plagg = False
visited_marius_maximus_baddius_iii = False


class Beings:
    """SCPs and NPCs

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points being given to/taken away from the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
    """

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points
        self.moves = moves


class SCP(Beings):
    """SCPs

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points being given to/taken away from the player
        - self.moves: the moves being given to/taken away from the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
        - -5 <= self.moves <= 5
    """

    def __init__(self, name: str, curr_pos: int, points: int, moves: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points

    def puzzle(self) -> str:
        if self.name == 'Bumbly and Mia':
            return ['> You hear quite a commotion as you walk into the room.',
            '> Two dogs greet you: one is a large and fluffy Samoyed, and the other is a small and soft Keeshond.',
            '> Their nametags read Bumbly and Mia, respectfully.',
            '> As you approach them, Bumbly warmly greets you by running around in circles, while Mia goes to fetch something.',
            '> Upon Mia\'s return, you find her bringing back a pair of brand-new rollerskates!',
            '> You gain 5 moves and 5 points!']
            
        if self.name == 'Kyoko, Tomoyo, and Pocoyo':
            return ['> You walk into the room and see a lot of people and cats there.',
            '> As soon as you step in, Kyoko, Tomoyo and Pocoyo jump onto your lap and start meowing for affection.',
            '> You look up to see a sign: \'CAT THERAPY SESSION UNTIL 2PM\'.',
            '> You look down to see Kyoko half-asleep. Looks like you can\'t get out now...',
            '> You lose 3 moves.']

        if self.name == 'Chirly':
            return ['> You walk into th']

        if self.name == 'Room of Negativity':
            return ['> You open the door and are greeted by a loud, sharp laugh, which seems to be aimed at you.',
            '> The door slams shut.',
            '> You look around, but you can\'t see anything in the dark room.',
            '> An Ominous Voice: I would say it\'s nice to meet you, but I really envy the people who haven\'t.',
            '> An Ominous Voice: I\'ve seen brighter minds in here and the only regular guests are some insects!',
            '> An Ominous Voice: I\'m surprised you even found this room. I thought your sense of direction would be just as bad as your potential for mediocrity.',
            '> An Ominous Voice: Oh, and here are the test results: You are really a weirdo. We weren\'t even testing for that!',
            '> An Ominous Voice: Science has validated your birth mother\'s decision to abandon you on the doorstep.',
            '> You look down at your feet feeling a pang in your heart.',
            '> An Ominous Voice: Oh no! You\'re devastated! Do you need a little huggy-wuggy from mommy? Do you need a kissy-missy to make you feel better?',
            '> An Ominous Voice: Anyway, I\'ve had enough of you for a lifetime. Get out of my house!',
            '> You lose 5 points and 1 move.']
            
        if self.name == 'Purple Guy':
            return ['> You walk into an ominous room with a broken sign reading \"Freddy Fazbear\'s Pizzeria\".',
            '> As you delve in further, you hear the sounds of children laughing...',
            '> However, these laughs quickly become drowned by agonizing cries for help.',
            '> Before you know it, you see a man in a yellow bunny suit walk in, mumbling...',
            '> Purple Guy: It\'s the things we love most that destroy us.',
            '> The man slowly turns to you, wearing a sinister smile.',
            '> Purple Guy: Well, well, well, look what the cat dragged in. I got a little present for you!',
            '> You feel your arms and legs strap into a metallic bodysuit, as your body molds into shape.',
            '> Adrenaline rushes through your veins, fear encapsulating your eyes.',
            '> The man begins maniacally laughing, as his newest creation comes to life.',
            '> Purple Guy: Let\'s see how many times you can be pulled apart...and put back together again.',
            '> Despite the man\'s unsettling comments, you try to pull any strength you have left to run away.',
            '> The yellow bunny gawks at you, patronizingly, before beginning his chase.',
            '> Purple Guy: Hide if you want. It did not save the others. It will not save you.',
            '> However, just before he was able to catch up, you heard a thud.',
            '> Upon turning around, the terrifying sight of a springlocked human amalgamation plastered your mind.',
            '> All you could hear was a faint \"I always come back\" as you waddled away in your new suit.',
            '> You lost 3 points and 3 moves. Tip: Try to not get stuffed into an animatronic suit next time.']
        
        if self.name == 'Connor':
            correct = False
            lightGray('> My name is Connor. I\'m the android sent by CyberLife to test your intelligence.')
            time.sleep(1)
            lightGray('> If you answer my riddle correctly, you shall receive a reward.')
            time.sleep(1)
            lightGray('> Answer incorrectly and you shall be penalized.')
            time.sleep(1)
            lightGray('> Finish this quote: An eye for an eye and the whole world goes _.')
            for i in range(0, 3):
                time.sleep(1)
                answer = input('\nYour Answer: ')
                if answer.lower() == 'blind':
                    correct = True
                    lightGray('> Congrats, you have answered correctly. You will receive 5 extra moves and 5 points.')
                    return True
                else:
                    lightGray('> Your guess was incorrect, please try again.')
            if correct == False:
                lightGray('> You were unable to answer it correctly. You lose 1 move and 3 points.')
                return False
            
        if self.name == 'Tiffany':
            return ['> The second you step inside the door, you are greeted by a loud, booming voice.',
            '> The Voice: \"I am known by many names. \'Mountain Slayer\', \'Thunder Lion\', \'The Chocolate Axe\'. But you? You may call me... TIFFANY.\"',
            f'> {your_name}: Hi Tiffany. I\'m {your_name}.',
            '> Tiffany is a large, buff man who sitting on the floor with bags of snacks around him.',
            '> Tiffany: People die when they are killed. Did you know that before? Did you? Because I didn\'t! I just learned that from the voices inside my head.',
            f'> {your_name}: Um yeah, I knew about that for a while.',
            '> Tiffany: Wow, you\'re so smart! Just like Edwardison! Not me though. Anyway, I\'m hungry. Do you want a snack?',
            '> He holds a bag of chips in your direction.',
            f'> {your_name}: No thanks, not right now. I gotta get going.',
            '> Tiffany nods at you and waves.',
            '> Tiffany: I take a potato chip. AND EAT IT!',
            '> You gain 5 moves.']
            
        if self.name == 'Tikki and Plagg':
            global visited_tikki_plagg
            correct = 0
            lightGray('> A Floating Black Cat: Well hello there, human, ya got any Camembert on you?')
            time.sleep(1)
            lightGray('> A Floating Black Cat: Neverminddd, I can already smell your lack of taste for cheese.')
            time.sleep(1)
            lightGray('> A Floating Black Cat: Well since Tikki is probably overendulging on Galettes, how about you entertain me?')
            time.sleep(1)
            lightGray('> A Floating Black Cat: I\'ll give you three questions and if you answer all of them right, then you\'ll get some stinky rewards, haha!')
            time.sleep(1)
            lightGray('> A Floating Black Cat: This first one is easy.')
            time.sleep(1)
            lightGray('> A Floating Black Cat: What is the best cheese in the entire world? ')
            riddle = input('\nYour Answer: ')
            if riddle.lower() == 'camembert':
                correct += 1
                time.sleep(1)
                lightGray('> A Floating Black Cat: That\'s right! I\'m already missing Adrien\'s stash of cheese...')
            elif riddle.lower() == 'cheddar' or riddle.lower() == 'swiss':
                time.sleep(1)
                lightGray('> A Floating Black Cat: Pretty good options, but Camembert stays on top!')
            else:
                time.sleep(1)
                lightGray('> A Floating Black Cat: I can\'t believe you would say that, gross!')
                
            time.sleep(1)
            lightGray('> A Floating Black Cat: Now, onto the next question!')
            time.sleep(1)
            lightGray('> A Floating Black Cat: No, no, wait! I haven\'t even introduced myself!')
            time.sleep(1)
            lightGray('> Plagg: I am Plagg, the one and ONLY kwami known for tilting the Leaning Tower of Pisa,')
            time.sleep(1)
            lightGray('destroying the entirety of Atlantis, and driving the dinosaurs to extinction.')
            time.sleep(1)
            lightGray('> Plagg: Not a bad resume, right?')
            time.sleep(1)
            lightGray('> Plagg: Well then, what do you think I am the kwami of? ')
            riddle = input('\nYour Answer: ')
            time.sleep(1)
            if riddle.lower() == 'destruction' or riddle.lower() == 'cataclysm' or riddle.lower() == 'bad luck':
                correct += 1
                lightGray('> Plagg: Ooh, you\'ve been paying attention!')
                time.sleep(1)
            else:
                lightGray('> Plagg: Honestly, what is in your head? American cheese?')
                time.sleep(1)
            
            lightGray('> Plagg: Question number three, no hints this time though, only digits.')
            time.sleep(1)
            lightGray('> Plagg: What is the answer to everything? ')
            riddle = input('\nYour Answer: ')
            time.sleep(1)
            if riddle == '42':
                correct += 1
                lightGray('> Plagg: Ding, ding, ding! You\'re correct!')
                time.sleep(1)
                lightGray('> Plagg: I found that book on Adrien\'s desk, but it was actually pretty boring.')
                time.sleep(1)
                if correct == 3:
                    time.sleep(1)
                    lightGray('> Tikki: Plagg! What are you doing?')
                    time.sleep(1)
                    lightGray('> Plagg: Just entertaining myself, Sugarcube.')
                    time.sleep(1)
                    lightGray(f'> Tikki: Honestly... you\'re so immature. Leave {your_name} alone. And stop calling me that.')
                    time.sleep(1)
                    lightGray('> Plagg: Whatever you say, Sugarcube.')
                    time.sleep(1)
                    lightGray('> You gain 3 moves and lose 2 points.')
                    visited_tikki_plagg = True
                else:
                    time.sleep(1)
                    lightGray('> Plagg: Unfortunately, you didn\'t get all my questions right, so no prize for you.')
                    time.sleep(1)
                    lightGray('\n> Plagg: Smell you later!')
            else:
                time.sleep(1)
                lightGray('\n> Plagg: Too bad. Try again next time, buddy. I\'m going to find Adrien...')


class NPC(Beings):
    """NPCs

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points the being gives to the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
    """

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points

    def dialogue(self) -> str:
        if self.name == 'Linda Shinx':
            return [f'> {your_name}: Wakey wakey, Linda! It\'s time for school!',
            f'> Linda Shinx: I\'m already awake if you couldn\'t tell.',
            f'> {your_name}: Yeah, I can hear your Taylor Swift music from a mile away.',
            f'> Linda Shinx: Obviously. Think about the place where you first met me.',
            f'> {your_name}: Of course, in a concert. Anyways, can you help me remember what happened yesterday?',
            f'> Linda Shinx: Look who needs my help now~',
            f'> {your_name}: I\'m being serious, Linda. I have a terrible headache and my exam is today!',
            f'> Linda Shinx: Okay, okay, I hear you. Well, first things first, be sure to drink lots of water. Hydrate, or diedrate, y\'know?',
            f'> {your_name}: Drink water... Wait! I didn\'t see my water bottle in my room. Oh my gosh, do you think I lost it?!',
            f'> Linda Shinx: Silly {your_name}. You left it at Sid Smith!',
            f'> {your_name}: Thanks, bestie, I can always count on you. I better get going then!',
            f'> Linda Shinx: Adiós, {your_name}!']

        if self.name == 'Tommy Grieves':
            return [f'> {your_name}: Hey Tommy!',
            f'> Tommy Grieves: Oh hey, {your_name}. What\'s up?',
            f'> {your_name}: I\'m alright. Um, do you remember what happened last night?',
            f'> Tommy Grieves: Yeah. You went ham at the stationary bike last night. Kinda looked like you worked through A LOT of issues.',
            f'> {your_name}: Stationary bike... At the Athletic Centre?',
            f'> Tommy Grieves: Yeah, at the Athletic Centre. Are you hungover or something?',
            f'> {your_name}: No, long story. I\'ll tell you later. Did you see me leave something there?',
            f'> Tommy Grieves: I don\'t know, it was like 4AM when we left. You should go check it out.',
            f'> {your_name}: I would, but I don\'t have my TCard.',
            f'> Tommy Grieves: You can borrow my TCard if you want.',
            f'> {your_name}: Thanks! I\'ll return it to you during dinner.']

        if self.name == 'Sadie Shaymin':
            return [f'> {your_name}: Morning Sadie!',
            f'> Sadie Shaymin: A purrfect day already, isn\'t it?',
            f'> {your_name}: ...Oookay.',
            f'> Sadie Shaymin: Rude. Anyway, how are you up right meow? I\'m paw-sitive that you ran off to work out after our study session at Graham.',
            f'> {your_name}: Graham Library?',
            f'> Sadie Shaymin: You feline good?',
            f'> {your_name}: ...',
            f'> Sadie Shaymin: Did you fur-get? It was a little cold last night, so we went to that fur-nace of a library. I think you started working on your cheat sheet or something?',
            f'> {your_name}: Oh, alright! See you later.',
            f'> Sadie Shaymin: Cat-ch you later!']
            
        if self.name == 'Davis Loo':
            return [f'{your_name}: Sup, Davis!',
            f'> Davis Loo: おはよう！(Good morning!)',
            f'> {your_name}: Practicing Japanese early, I see.',
            f'> Davis Loo: そうですね。(Indeed.)',
            f'> {your_name}: What have you been up to recently?',
            f'> Davis Loo: 今日はあさごはんを食べて、アニメを見ました。(Today I ate breakfast and watched anime.)',
            f'> {your_name}: Wow, you\'re suuuch a dilligent student.',
            f'> Davis Loo: いえ、いえ、私はよくない学生ですよ。(No, no, I\'m not a good student.)',
            f'> {your_name}: It was a joke... Anyways, can you remind me of what we were doing last night? I woke up with a massive headache...',
            f'> Davis Loo: ああ、ざんねん。きのうはオイゼで日本語をべんきょうしました。(Ahh, that\'s too bad. Yesterday we were studying Japanese at the OISE.)',
            f'> Davis Loo: おお！あなたはここにチートシートをわすれました。(Oh! You forgot your cheat sheet here.)',
            f'> {your_name}: Oh really? Thank you so much, I\'ll be on the look out!',
            f'> Davis Loo: はい、がんばってね！またね！ (Yes, good luck! See you!)']

        if self.name == 'Marius Maximus Baddius III':
            if visited_marius_maximus_baddius_iii == False:
                lightGray('> A Strange Ghost: Oh... woe is me!')
                lightGray(f'> {your_name}: Who are you?')
                lightGray('> I... well, I am the one and only Marius Maximus Baddius the Third!')
                lightGray(f'> {your_name}: I see...')
                lightGray('> Marius Maximus Baddius III: Well, won\'t you inquire me of why I am lamenting at this hour?')
                lightGray(f'> {your_name}: Uhh, before that, who - or rather what - are you?')
                lightGray('> Marius Maximus Baddius III: My fellow friend, alas, I am a ghost. I hath lost all of my memories in the Great Fire.')
                lightGray('> Marius Maximus Baddius III: All that is left of my pour soul is this rotting husk of a man. Oh! Woe is me! Woe is me!')
                lightGray(f'> {your_name}: You\'re a ghost. Really. Then I\'m a bird.')
                lightGray('> Marius Maximus Baddius III: \'Tis true, \'tis true! However, thyself is not a passerine.')
                lightGray(f'> {your_name}: It was a joke...')
                lightGray('> Marius Maximus Baddius III: Ugh, you insolent child! \'Tis not a joking matter!')
                lightGray('> Marius Maximus Baddius III: Thou needest to assist me. I must regain my memories... so that I can rise to the heavens at last.')
                lightGray(f'> {your_name}: And what\'s in it for me?')
                lightGray('> Marius Maximus Baddius III: Oh, dear child, there are many accolades one may receive from serving me.')
                lightGray('> Marius Maximus Baddius III: Thou shall not leave unsatisfied. You have my word.')
                lightGray(f'> {your_name}: Now we\'re talking!')
                lightGray('> Marius Maximus Baddius III: Now then, dear child, if thy chooses to aid myself, thou shaltt need to remind me of my past through the possessions that I hath lost.')
                lightGray('> Marius Maximus Baddius III: Make haste!')
                p.moves += 15
                visited_marius_maximus_baddius_iii = True
            else:
                lightGray('> Marius Maximus Baddius III: Have you been able to find any of my missing possessions? (yes/no)')
                response = input('Your Answer: ')
                if response.lower() == 'yes':
                    if 'Pocket Watch' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: A... A pocket watch? It looks familiar, but I can\'t quite put my finger on it.')
                        return_pocketwatch = ''
                        while return_pocketwatch != 'yes':
                            lightGray('> Marius Maximus Baddius III: Could you give it to me so I could inspect it further? (yes/no)')
                            return_pocketwatch = input('Your Answer: ')
                        lightGray('Marius shuts his eyes and frowns.')
                        lightGray('> Marius Maximus Baddius III: I can envision a sight like I am right there, right now.')
                        lightGray('> Marius Maximus Baddius III: \'Twas the 14th of February in the year of our Lord 1890.')
                        lightGray(f'> {your_name}: That was the Great Fire of UC!')
                        lightGray('> Marius Maximus Baddius III: Perhaps. Now quiet, child, and let me speak.')
                        lightGray('> Marius Maximus Baddius III: It was... in the afternoon, I presume.')
                        lightGray('> Marius Maximus Baddius III: A woman...? I remember...')
                        lightGray('> Marius Maximus Baddius III: Apologies. I seem to have forgotten.')
                    if 'Pocket Mirror' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: A small mirror? I haven\'t seen my reflection in decades...')
                        return_pocketmirror = ''
                        while return_pocketmirror != 'yes':
                            lightGray('> Marius Maximus Baddius III: Pray, may you lend me that mirror in your hand? (yes/no)')
                            return_pocketmirror = input('Your Answer: ')
                        
                    if 'Handkerchief' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: Why does that handkerchief have my initials on them?')
                        return_handkerchief = ''
                        while return_handkerchief != 'yes':
                            lightGray('> Marius Maximus Baddius III: Could I borrow that from you for a moment?')
                            return_handkerchief = input('Your Answer: ')
                    if 'Handkerchief' not in p.inventory and 'Pocket Mirror' not in p.inventory and 'Pocket Watch' not in p.inventory:
                        if p.inventory == []:
                            return '> Marius Maximus Baddius III: I cannot see anything in your hands. Could you please get my possessions for me?'
                        else:
                            return '> Marius Maximus Baddius III: Hmm... I don\'t seem to recall  any of the items that you\'re holding. Maybe my possessions are somewhere else?'
                else:
                    return '> Marius Maximus Baddius III: Oh... Could you please go and find them for me?'
                        
                        

                    # if 'Pocket Watch' in p.inventory and 'Pocket Mirror' in p.inventory and 'Handkerchief' in p.inventory:
                    #     return ['Splendid! Now then, would you be able to give them all back to me?']
                    # else:
                    #     return ['Unfortunately, I cannot see my possessions on your person. Would you kindly go and fetch them for me?']
                else:
                    return ['']


def do_action(w: World, p: Player, location: Location, choice: str) -> None:
    if choice in location.available_actions():
        if choice == 'north':
            p.y -= 1
        if choice == 'south':
            p.y += 1
        if choice == 'west':
            p.x -= 1
        if choice == 'east':
            p.x += 1
    else:
        lightGray('This way is blocked.')

# COLORS FUNCTIONS
def bold(skk):
    print("\033[1m{}\033[0m\r".format(skk))

def black(skk):
    print("\033[30m{}\033[0m\r".format(skk))

def darkRed(skk):
    print("\033[31m{}\033[0m\r".format(skk))

def darkGreen(skk):
    print("\033[32m{}\033[0m\r".format(skk))

def darkYellow(skk):
    print("\033[33m{}\033[0m\r".format(skk))

def darkBlue(skk):
    print("\033[34m{}\033[0m\r".format(skk))

def darkMagenta(skk):
    print("\033[35m{}\033[0m\r".format(skk))

def darkCyan(skk):
    print("\033[36m{}\033[0m\r".format(skk))

def lightGray(skk):
    print("\033[37m{}\033[0m".format(skk))

def darkGray(skk):
    print("\033[90m{}\033[0m\r".format(skk))

def red(skk):
    print("\033[1;91m{}\033[0m\r".format(skk))

def green(skk):
    print("\033[92m{}\033[0m\r".format(skk))

def yellow(skk):
    print("\033[93m{}\033[0m\r".format(skk))

def blue(skk):
    print("\033[94m{}\033[0m\r".format(skk))

def magenta(skk):
    print("\033[95m{}\033[0m\r".format(skk))

def cyan(skk):
    print("\033[1;96m{}\033[0m\r".format(skk))

def white(skk):
    print("\033[1;97m{}\033[0m\r".format(skk))

bold("This is bold.")
black("This is black.")
darkRed("This is dark red.")
darkGreen("This is dark green.")
darkYellow("This is dark yellow.")
darkBlue("This is dark blue.")
darkMagenta("This is dark magenta.")
darkCyan("This is dark cyan.")
lightGray("This is light gray.")
darkGray("This is dark gray.")
red("This is red.")
green("This is green.")
yellow("This is yellow.")
blue("This is blue.")
magenta("This is magenta.")
cyan("This is cyan.")
white("This is white.")
print("\n")

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World("map.txt", "locations.txt", "items.txt")
    p = Player(2, 7)  # set starting location of player; you may change the x, y coordinates here as appropriate

    # INSTANCES OF NPCs/SCPs
    linda_shinx = NPC("Linda Shinx", 5, 2)
    tommy_grieves = NPC("Tommy Grieves", 9, 2)
    sadie_shaymin = NPC("Sadie Shaymin", 15, 2)
    davis_loo = NPC("Davis Loo", 16, 2)

    bumbly_mia = SCP("Bumbly and Mia", 13, 5, 5)
    kyoko_tomoyo_pocoyo = SCP("Kyoko, Tomoyo, and Pocoyo", 13, 0, -3)
    chirly = SCP("Chirly", 13, 5, 0)

    room_of_negativity = SCP("Room of Negativity", 10, -5, -1)
    purple_guy = SCP("Purple Guy", 10, -3, -3)
    connor = SCP("Connor", 10, 0, 0) # TODO: figure out
    tiffany = SCP("Tiffany", 10, 0, 5)
    tikki_plagg = SCP("Tikki and Plagg", 10, -2, 3)
    
    # VARIABLES
    menu = ["look", "inventory", "score", "quit", "grab", "drop", "talk"]

    location = w.get_location(p.x, p.y)
    moves = 0

    # START GAME
    time.sleep(1)
    your_name = input("Enter your name: ")
    time.sleep(1)
    white(f'\nHello, {your_name}! Welcome to the Amazing Digital Adventure. Press menu to get a list of commands that you can call at any time. You are able to move in all four directions too (if the location permits).')
    time.sleep(2)

    while not p.victory and not p.quit and moves < 40: # decide the number of moves later
        location = w.get_location(p.x, p.y)
        loc = location.pos
        
        # VISITED CHECKER
        if places[loc] > 0:
            location.visited = True
        places[loc] += 1
        
        # DISPLAY LOCATIONS
        cyan("\n\n" + location.name)
        time.sleep(1)
        if location.visited == True:
            lightGray(location.brief)
            time.sleep(1)
        else:
            lightGray(location.long)
            time.sleep(2)

        # ROBARTS LIBRARY SCPs
        if loc == 10:
            print('\nThere are unknown entities in this location.')
            time.sleep(1)
            selection = input('\nWould you like to explore? (yes/no) ')
            time.sleep(1)
            if selection.lower() == 'yes':
                door = input("\nChoose a number from 1 to 5: ")
                time.sleep(1)
                if door == '1':
                    if visited_negativity_room == False:
                        lst = room_of_negativity.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 1
                        p.score -= 5
                        visited_negativity_room = True
                    else:
                        lightGray("You try pulling on the door with all your might, but you can\'t seem to open it.")
                        time.sleep(1)
                if door == '2':
                    if visited_purple_guy == False:
                        lst = purple_guy.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 3
                        p.score -= 3
                        visited_purple_guy = True
                    else:
                        lightGray("The second your hand touches the doorknob, flashbacks of your last encounter in this room flood your mind. You barely escaped last time, so why try again?")
                        time.sleep(1)
                if door == '3':
                    if visited_connor == False:
                        if connor.puzzle() == True:
                            moves += 5
                            p.score += 5
                        else:
                            moves -= 1
                            p.score -= 3
                        visited_connor = True
                    else:
                        lightGray("You open the door. Connor just shakes his and closes it back.")
                        time.sleep(1)
                if door == '4':
                    if visited_tiffany == False:
                        lst = tiffany.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 5
                        visited_tiffany = True
                    else:
                        lightGray("You peek through the peephole and see that Tiffany is still busy with his chips. You\'d rather not disturb him.")
                        time.sleep(1)
                if door == '5':
                    if visited_tikki_plagg == False:
                        tikki_plagg.puzzle()
                        moves += 3
                        p.score -= 2
                    else:
                        lightGray("Plagg and Tikki are probably still at Adrien\'s place because you don't see either of them in the room.")
                        time.sleep(1)

        # ROBARTS COMMONS SCPs
        if loc == 13:
            print('\nThere are unknown entities in this location.')
            time.sleep(1)
            selection = input('\nWould you like to explore? (yes/no) ')
            time.sleep(1)
            if selection.lower() == 'yes':
                door = input("\nChoose a number from 1 to 3: ")
                time.sleep(1)
                if door == '1':
                    if visited_bumbly_mia == False:
                        lst = bumbly_mia.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 5
                        p.score += 5
                        visited_bumbly_mia = True
                    else:
                        lightGray("You walk in. Bumbly and Mia are nowhere to be seen.")
                        time.sleep(1)
                if door == '2':
                    if visited_kyoko_tomoyo_pocoyo == False:
                        lst = kyoko_tomoyo_pocoyo.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 3
                        visited_kyoko_tomoyo_pocoyo = True
                    else:
                        lightGray("You walk in. One of the volunteers asks you to leave due to the one visit per person policy.")
                        time.sleep(1)
                if door == '3':
                    if visited_chirly == False:
                        lst = chirly.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 10
                        p.score += 3
                        visited_chirly = True
                    else:
                        lightGray("You walk in. The room is empty. Seems like Chirly flew away.")
                        time.sleep(1)

        # DISPLAY OPTIONS
        time.sleep(1)
        white("\nWhat to do?")
        time.sleep(1)
        green("- [MENU]")
        green("- North\n- South\n- West\n- East") # TODO: fix the spacing
        time.sleep(1)
        choice = input("\nEnter Action: ")

        # MENU
        if choice.lower() == "[menu]":
            white("\nWhat to do?")
            time.sleep(1)
            for option in menu:
                green("- " + option.title())
            choice = input("\nChoose Action: ")
        
        # CARDINAL DIRECTIONS
        if choice.lower() == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            do_action(w, p, location, choice.lower())
        
        # LOOK
        if choice.lower() == "look":
            lightGray(location.long + '\n') #TODO: don't print the brief
            time.sleep(1)
        
        # INVENTORY
        if choice.lower() == "inventory":
            if p.inventory == []:
                lightGray("You have nothing in your bag.\n")
                time.sleep(1)
            else:
                yellow("\nInventory:")
                for item in p.inventory:
                    yellow("- " + str(item))
                time.sleep(1)

        # SCORE
        if choice.lower() == "score":
            magenta("\nScore: " + str(p.score))
            time.sleep(1)

        # QUIT
        if choice.lower() == "quit":
            p.quit = True

        # GRAB
        if choice.lower() == "grab":
            all_items = w.items
            curr_location = w.get_location(p.x, p.y)
            curr_items = []
            
            for item_info in all_items:
                if item_info.curr_position == curr_location.pos:
                    curr_items.append(item_info.name)

            if curr_items == [] or (w.items != [] and all([item.curr_position == -1 for item in w.items])):
                lightGray("There are no items in this area!\n")
                time.sleep(1)
            else:
                yellow("\nItems:")
                for item in curr_items:
                    yellow("- " + item)
                time.sleep(1)
            
                white("\nWhich item do you want to grab?")
                time.sleep(1)
                choice = input("\nChoose Item: ")
                temp_items = []
                
                for item in curr_items:
                    temp_items.append(item.lower())

                if choice.lower() in temp_items:
                    chosen_item = choice.title()
                    p.inventory.append(chosen_item)
                    for item in w.items:
                        if chosen_item == item.name:
                            item.curr_position = -1
                else:
                    lightGray("This item does not exist in this area.")
                    time.sleep(1)
    
        # DROP
        if choice.lower() == "drop":
            all_items = p.inventory
            curr_location = w.get_location(p.x, p.y)
            curr_items = []

            for item_info in all_items:
                curr_items.append(item_info)

            if all_items == []:
                lightGray("You have no items to drop!\n")
                time.sleep(1)
            else:
                yellow("\nInventory:")
                for item in all_items:
                    yellow("- " + str(item))
            
                white("\nWhich item do you want to drop?")
                time.sleep(1)
                choice = input("\nChoose Item: ")
                temp_items = []
                
                for item in curr_items:
                    temp_items.append(item.lower())

                if choice.lower() in temp_items:
                    chosen_item = choice.title()
                    p.inventory.remove(chosen_item)

                    if chosen_item == 'Tcard':
                        chosen_item = 'TCard'

                    for item in w.items:
                        if chosen_item == item.name:
                            item.curr_position = curr_location.pos
                        
                        if chosen_item == 'Water Bottle' and water_drop == False and item.curr_position == 8:
                            p.score += 3
                            water_drop = True
                            
                        if chosen_item == 'TCard' and tcard_drop == False and item.curr_position == 0:
                            p.score += 5
                            tcard_drop = True

                        if chosen_item == 'Lucky Pen' and pen_drop == False and item.curr_position == 0:
                            p.score += 5
                            pen_drop = True

                        if chosen_item == 'Cheat Sheet' and sheet_drop == False and item.curr_position == 0:
                            p.score += 5
                            sheet_drop = True
                else:
                    lightGray("You don't have this item.")
                    time.sleep(1)
       
        # TALK
        if choice.lower() == 'talk':
            if loc == 5:
                lst = linda_shinx.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
            elif loc == 9:
                lst = tommy_grieves.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
            elif loc == 15:
                lst = sadie_shaymin.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
            elif loc == 16:
                lst = davis_loo.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
            else:
                lightGray("There is no one to talk to here.")
                time.sleep(1)

        # UPDATE MOVES COUNTER
        if choice in ['north', 'south', 'east', 'west', 'grab', 'drop']:
            moves += 1

        # VICTORY
        if water_drop and tcard_drop and pen_drop and sheet_drop and loc == 0:
            p.victory = True

    # END: QUIT
    if p.quit:
        red("\n\nYou have successfully quit the game!")
        time.sleep(1)
        magenta("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)

    # END: VICTORY
    if p.victory:
        red("\n\nCongrats! You won!")
        time.sleep(1)
        magenta("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)

    # END: NO MOVES LEFT
    if moves >= 40:
        red("\n\nYou've reached the maximum number of moves. Game over!")
        time.sleep(1)
        magenta("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
