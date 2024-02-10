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

from os import environ
import time
import random
from typing import Any
import pygame
from game_data import World, Location, Player

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

pygame.mixer.init()

PLACES = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0,
          17: 0, 18: 0}

YOUR_NAME = ''
X = 0

WATER_DROP = False
TCARD_DROP = False
SHEET_DROP = False
PEN_DROP = False

VISITED_LINDA = False
VISITED_TOMMY = False
VISITED_DAVIS = False
VISITED_SADIE = False
VISITED_BUMBLY_MIA = False
VISITED_KYOKO_TOMOYO_POCOYO = False
VISITED_CHIRLY = False
VISITED_NEGATIVITY_ROOM = False
VISITED_PURPLE_GUY = False
VISITED_CONNOR = False
VISITED_TIFFANY = False
VISITED_TIKKI_PLAGG = False
VISITED_MARIUS = False
VISITED_PHONE_GUY = False
FOUND_ITEMS = False
FOUND_POCKET_MIRROR = False
FOUND_POCKET_WATCH = False
FOUND_HANDKERCHIEF = False
MARIUS_MOVES_GAINED = False
MARIUS_END_GAINED = False

SPELLING = pygame.mixer.Sound('spelling.mp3')


class Beings:
    """Parent class for various enhancement SCPs (everything you meet at the Robarts Library, Commons, and Phone Guy)
    and NPCs (the four characters that help you figure where your items went and Marius, the ghost).

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points being given to/taken away from the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
    """
    name: str
    curr_pos: int
    points: int

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points


class SCP(Beings):
    """Child class of Being defining the creatures and animals you meet at Robarts Library and Commons.

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points being given to/taken away from the player
        - self.moves: the moves being given to/taken away from the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
        - -5 <= self.moves_scp <= 5
    """
    name: str
    curr_pos: int
    points: int
    moves_scp: int

    def __init__(self, name: str, curr_pos: int, points: int, moves_scp: int) -> None:
        """Initialize a new SCP.
        """
        super().__init__(name, curr_pos, points)
        self.moves_scp = moves_scp

    def puzzle(self) -> Any:
        """Dialogue that pops up when you visit a room for the first time along with the
        amount of moves and/or points you win/lose and the questions some of them ask.
        """
        if self.name == 'Bumbly and Mia':
            return ['> You hear quite a commotion as you walk into the room.',
                    '> Two dogs greet you: one is a large and fluffy Samoyed, and the other is a small and soft Keeshond.',
                    '> Their nametags read Bumbly and Mia, respectively.',
                    '> As you approach them, Bumbly warmly greets you by running around in circles, while Mia goes to fetch something.',
                    '> Upon Mia\'s return, you find her bringing back a pair of brand-new rollerskates!',
                    '> You won 5 moves and 5 points!']

        if self.name == 'Kyoko, Tomoyo, and Pocoyo':
            return ['> You walk into the room and see a lot of people and cats there.',
                    '> As soon as you step in, Kyoko, Tomoyo and Pocoyo jump onto your lap and start meowing for affection.',
                    '> You look up to see a sign: \"CAT THERAPY SESSION UNTIL 2PM.\"',
                    '> You look down to see Kyoko half-asleep. Looks like you can\'t get out now...',
                    '> You lost 3 moves.']

        if self.name == 'Chirly':
            return ['> You enter the room and see a sole birdcage.',
                    '> Inside, there is a yellow-green parrotlet named Chirly yapping away.',
                    '> Chirly: Squawk! He\'s dead! He\'s dead!',
                    f'> {YOUR_NAME}: Who\'s... dead?',
                    '> Chirly: Marius! Marius! Squawk! He\'s dead! Squawk!',
                    f'> {YOUR_NAME}: Marius? How did he die?',
                    '> Chirly: He was stabbed! Squawk! 28 times!',
                    f'> {YOUR_NAME}: That\'s crazy... Who did it? Where? When?',
                    '> Chirly: He\'s dead! Detective, he\'s dead! Squawk!',
                    f'> {YOUR_NAME}: Can you at least tell me why?',
                    '> Chirly: Squawk! He\'s dead! Case closed! Squawk!',
                    '> It seems like Chirly has nothing else to say.',
                    '> You won 5 moves and 3 points!']

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
                    '> You lost 1 move and 5 points.']

        if self.name == 'Purple Guy':
            return ['> You walk into an ominous room with a broken sign reading \"Freddy Fazbear\'s Pizzeria.\"',
                    '> As you delve in further, you hear the sounds of children laughing...',
                    '> However, these laughs quickly become drowned by agonizing cries for help.',
                    '> Before you know it, you see a man in a yellow bunny suit walk in, mumbling...',
                    '> Purple Guy: It\'s the things we love most that destroy us.',
                    '> The man slowly turns to you, wearing a sinister smile.',
                    '> Purple Guy: Well, well, well, look what the cat dragged in. I got a little present for you!',
                    '> You feel your arms and legs strap into a metallic bodysuit, as your body molds into shape.',
                    '> Adrenaline rushes through your veins, fear encapsulating your eyes.',
                    '> The man begins maniacally laughing, as his newest creation comes to life.',
                    '> Purple Guy: Let\'s see how many times you can be pulled apart... and put back together again.',
                    '> Despite the man\'s unsettling comments, you try to pull any strength you have left to run away.',
                    '> The yellow bunny gawks at you, patronizingly, before beginning his chase.',
                    '> Purple Guy: Hide if you want. It did not save the others. It will not save you.',
                    '> However, just before he was able to catch up, you heard a thud.',
                    '> Upon turning around, the terrifying sight of a springlocked human amalgamation plastered your mind.',
                    '> All you could hear was a faint \"I always come back\" as you waddled away in your new suit.',
                    '> You lost 3 moves and 3 points. Tip: Try to not get stuffed into an animatronic suit next time.']

        if self.name == 'Connor':
            global X
            correct = False
            lightgray('> Connor: My name is Connor. I\'m the android sent by CyberLife to test your intelligence.')
            time.sleep(2)
            lightgray('> Connor: If you answer my riddle correctly, you shall receive a reward.')
            time.sleep(2)
            lightgray('> Connor: Answer incorrectly and you shall be penalized.')
            time.sleep(2)
            lightgray('> Connor: Finish this quote: An eye for an eye and the whole world goes _.')
            time.sleep(2)
            for num in range(0, 3):
                X = num
                player_answer = input('\033[1;97m\nYour Answer: \033[0m')
                time.sleep(2)
                if player_answer.lower() == 'blind':
                    correct = True
                    lightgray('> Connor: Congrats, you have answered correctly.')
                    time.sleep(2)
                    lightgray('> You won 5 moves and 5 points!')
                    return True
                else:
                    lightgray('> Connor: Your guess was incorrect, please try again.')
                    time.sleep(2)
            if not correct:
                lightgray('> Connor: You were unable to answer it correctly.')
                time.sleep(2)
                lightgray('> You lost 1 move and 3 points.')
                return False

        if self.name == 'Tiffany':
            return ['> The second you step inside the door, you are greeted by a loud, booming voice.',
                    '> The Voice: \"I am known by many names. \'Mountain Slayer\', \'Thunder Lion\', \'The Chocolate Axe.\' But you? You may call me... TIFFANY.\"',
                    f'> {YOUR_NAME}: Hi Tiffany. I\'m {YOUR_NAME}.',
                    '> Tiffany is a large, buff man who is sitting on the floor with bags of snacks around him.',
                    '> Tiffany: People die when they are killed. Did you know that before? Did you? Because I didn\'t! I just learned that from the voices inside my head.',
                    f'> {YOUR_NAME}: Um yeah, I knew about that for a while.',
                    '> Tiffany: Wow, you\'re so smart! Just like Edwardison! Not me though. Anyway, I\'m hungry. Do you want a snack?',
                    '> He holds a bag of chips in your direction.',
                    f'> {YOUR_NAME}: No thanks, not right now. I gotta get going.',
                    '> Tiffany nods at you and waves.',
                    '> Tiffany: I take a potato chip. AND EAT IT!',
                    '> You won 5 moves!']

        if self.name == 'Tikki and Plagg':
            global VISITED_TIKKI_PLAGG
            correct = 0
            lightgray('> A Floating Black Cat: Well hello there, human, ya got any Camembert on you?')
            time.sleep(2)
            lightgray('> A Floating Black Cat: Neverminddd, I can already smell your lack of taste for cheese.')
            time.sleep(2)
            lightgray(
                '> A Floating Black Cat: Well since Tikki is probably overindulging on Galettes, how about you entertain me?')
            time.sleep(2)
            lightgray(
                '> A Floating Black Cat: I\'ll give you three questions and if you answer all of them right, then you\'ll get some stinky rewards, haha!')
            time.sleep(2)
            lightgray('> A Floating Black Cat: This first one is easy.')
            time.sleep(2)
            lightgray('> A Floating Black Cat: What is the best cheese in the entire world? ')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            if riddle.lower() == 'camembert':
                correct += 1
                time.sleep(2)
                lightgray('> A Floating Black Cat: That\'s right! I\'m already missing Adrien\'s stash of cheese...')
            elif riddle.lower() == 'cheddar' or riddle.lower() == 'swiss':
                time.sleep(2)
                lightgray('> A Floating Black Cat: Pretty good options, but Camembert stays on top!')
            else:
                time.sleep(2)
                lightgray('> A Floating Black Cat: I can\'t believe you would say that, gross!')

            time.sleep(2)
            lightgray('> A Floating Black Cat: Now, onto the next question!')
            time.sleep(2)
            lightgray('> A Floating Black Cat: No, no, wait! I haven\'t even introduced myself!')
            time.sleep(2)
            lightgray('> Plagg: I am Plagg, the one and ONLY kwami known for tilting the Leaning Tower of Pisa,')
            time.sleep(2)
            lightgray('> Plagg: Destroying the entirety of Atlantis, and driving the dinosaurs to extinction.')
            time.sleep(2)
            lightgray('> Plagg: Not a bad resume, right?')
            time.sleep(2)
            lightgray('> Plagg: Well then, what do you think I am the kwami of?')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            time.sleep(2)
            if riddle.lower() == 'destruction' or riddle.lower() == 'cataclysm' or riddle.lower() == 'bad luck':
                correct += 1
                lightgray('> Plagg: Ooh, you\'ve been paying attention!')
                time.sleep(2)
            else:
                lightgray('> Plagg: Honestly, what is in your head? American cheese?')
                time.sleep(2)

            lightgray('> Plagg: Question number three, no hints this time though, only digits.')
            time.sleep(2)
            lightgray('> Plagg: What is the answer to everything?')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            time.sleep(2)
            if riddle == '42':
                correct += 1
                lightgray('> Plagg: Ding, ding, ding! You\'re correct!')
                time.sleep(2)
                lightgray('> Plagg: I found that book on Adrien\'s desk, but it was actually pretty boring.')
                time.sleep(2)
                if correct == 3:
                    time.sleep(2)
                    lightgray('> Tikki: Plagg! What are you doing?')
                    time.sleep(2)
                    lightgray('> Plagg: Just entertaining myself, Sugarcube.')
                    time.sleep(2)
                    lightgray(
                        f'> Tikki: Honestly... you\'re so immature. Leave {YOUR_NAME} alone. And stop calling me that.')
                    time.sleep(2)
                    lightgray('> Plagg: Whatever you say, Sugarcube.')
                    time.sleep(2)
                    lightgray('> You won 3 moves and lost 2 points.')
                    VISITED_TIKKI_PLAGG = True
                    return True
                else:
                    time.sleep(2)
                    lightgray('> Plagg: Unfortunately, you didn\'t get all my questions right, so no prize for you.')
                    time.sleep(2)
                    lightgray('> Plagg: Smell you later!')
                    lightgray('> You lost 1 move and 2 points.')
                    VISITED_TIKKI_PLAGG = True
                    return False
            else:
                time.sleep(2)
                lightgray('\n> Plagg: Too bad. Try again next time, buddy. I\'m going to find Adrien...')
                lightgray('> You lost 1 move and 2 points.')
                VISITED_TIKKI_PLAGG = True
                return False

        if self.name == 'Phone Guy':
            lightgray('> You notice a mysterious blue telephone on the ground.')
            time.sleep(1)
            lightgray('> It begins ringing...')
            time.sleep(9)
            lightgray('> Phone Guy: Hello? Hello, hello?')
            time.sleep(3)
            lightgray(
                '> Phone Guy: Uh, I wanted to record a message for you to help you get settled into this text adventure game.')
            time.sleep(6)
            lightgray(
                '> Phone Guy: Um, I actually was the player before you. I\'m finishing up my last playthrough now, as a matter of fact.')
            time.sleep(7)
            lightgray(
                '> Phone Guy: So, I know it can be a bit overwhelming, but I\'m here to tell you there\'s nothing to worry about. Uh, you\'ll do fine.')
            time.sleep(8)
            lightgray('> Phone Guy: So, let\'s just focus on getting you through the game, okay?')
            time.sleep(5)
            lightgray(
                '> Phone Guy: Uh, let\'s see, first there\'s an introductory greeting from the game developers that I\'m supposed to read.')
            time.sleep(6)
            lightgray('> Phone Guy: Uh, it\'s kind of a legal thing, you know.')
            time.sleep(3)
            lightgray(
                f'> Phone Guy: Um, \"Welcome to The Amazing Digital Adventure, {YOUR_NAME}. A magical place for kids and grown-ups alike, where fantasy and fun come to life.\"')
            time.sleep(9)
            lightgray('> Phone Guy: \"Comp Sci Entertainment is not responsible for damage to property or person.\"')
            time.sleep(4)
            lightgray(
                '> Phone Guy: \"Upon discovering that despair or expiration has occurred, a missing person report will be filed within 90 days, or as soon property and premises have been thoroughly cleaned and checked, and the carpets have been replaced.\"')
            time.sleep(11)
            lightgray(
                '> Phone Guy: Blah, blah, blah. Now that might sound bad, I know, but there\'s surely nothing to worry about.')
            time.sleep(6)
            lightgray(
                '> Phone Guy: Uh, the SCP and NPC characters here do get a bit quirky at night, but do I blame them? No.')
            time.sleep(6)
            lightgray(
                '> Phone Guy: If I were forced to say those same stupid lines for twenty years and I never got a bath? I\'d probably be a bit irritable at night too.')
            time.sleep(9)
            lightgray(
                '> Phone Guy: So, remember, these characters hold a special place in the hearts of children and we need to show them a little respect, right? Okay.')
            time.sleep(8)
            lightgray(
                '> Phone Guy: So, just be aware, the characters do tend to wander a bit. Uh, they\'re left in some kind of free roaming mode at night.')
            time.sleep(8)
            lightgray('> Phone Guy: Uh... something about their code bugging up if they get turned off for too long.')
            time.sleep(5)
            lightgray(
                '> Phone Guy: Uh, they used to be allowed to walk around during the day too. But then there was The Bite of \'87. Yeah.')
            time.sleep(7)
            lightgray('> Phone Guy: I-It\'s amazing that the human body can live without the frontal lobe, you know?')
            time.sleep(5)
            lightgray(
                '> Phone Guy: Uh, now concerning your safety, the only real risk to you as a player here, if any, is the fact that these characters, uh, if they happen to see you after hours, probably won\'t recognize you as a person.')
            time.sleep(14)
            lightgray(
                '> Phone Guy: They\'ll pr- they\'ll most likely see you as an amalgamation of HTML without its CSS on.')
            time.sleep(5)
            lightgray(
                '> Phone Guy: Now since that\'s against the rules here at The Amazing Digital Adventure, they\'ll probably try to... forcefully stuff you inside a Being class.')
            time.sleep(10)
            lightgray(
                '> Phone Guy: Um, now, that wouldn\'t be so bad if the classes themselves weren\'t filled with instance attributes, representation invariants, and functions, especially around the top area.')
            time.sleep(11)
            lightgray(
                '> Phone Guy: So, you could imagine how having your head forcefully pressed inside one of those could cause a bit of discomfort... and expiration.')
            time.sleep(8)
            lightgray(
                '> Phone Guy: Uh, the only parts of you that would likely see the light of day again would be your eyeballs and teeth when they merge with the pre-existing code, heh.')
            time.sleep(7)
            lightgray(
                '> Phone Guy: Y-yeah, they don\'t tell you these things when you sign up. But hey, your first playthrough should be a breeze.')
            time.sleep(5)
            lightgray(
                '> Phone Guy: I\'ll chat with you tomorrow. Uh, check those rooms, and remember to quit the game only if absolutely necessary.')
            time.sleep(6)
            lightgray('> Phone Guy: Gotta conserve your moves. Alright, goodbye.')
            time.sleep(4)
            lightgray('> The phone call ends.')


class NPC(Beings):
    """Child class of Beings defining the people (and the one ghost) you meet around campus
    who help you find your missing items or ask for your help to decode their death.

    Instance Attributes:
        - self.name: the beings' name
        - self.curr_pos: the beings' current position
        - self.points: the points the being gives to the player

    Representation Invariants:
        - self.name != ''
        - 0 <= self.curr_pos <= 18
        - -5 <= self.points <= 5
    """
    name: str
    curr_pos: int
    points: int

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new NPC.
        """
        super().__init__(name, curr_pos, points)

    def dialogue(self) -> Any:
        """The conversation with the NPCs that pops up every time you choose to TALK in the location they are in.
        """
        if self.name == 'Linda Shinx':
            global VISITED_LINDA
            VISITED_LINDA = True
            return [f'> {YOUR_NAME}: Wakey wakey, Linda! It\'s time for school!',
                    '> Linda Shinx: I\'m already awake if you couldn\'t tell.',
                    f'> {YOUR_NAME}: Yeah, I can hear your Taylor Swift music from a mile away.',
                    '> Linda Shinx: Obviously. Think about the place where you first met me.',
                    f'> {YOUR_NAME}: Of course, in a concert. Anyways, can you help me remember what happened yesterday?',
                    '> Linda Shinx: Look who needs my help now~. All you need to do is \"shake it off.\" ;)',
                    f'> {YOUR_NAME}: I\'m being serious, Linda. I have a terrible headache and my exam is today!',
                    '> Linda Shinx: Okay, okay, I hear you. Well, first things first, be sure to drink lots of water. Hydrate, or diedrate, y\'know?',
                    f'> {YOUR_NAME}: Drink water... Wait! I didn\'t see my water bottle in my room. Oh my gosh, do you think I lost it?!',
                    f'> Linda Shinx: Silly {YOUR_NAME}. You left it at Sid Smith!',
                    f'> {YOUR_NAME}: Thanks, bestie, I can always count on you. I better get going then!',
                    f'> Linda Shinx: Adiós, {YOUR_NAME}!',
                    '> You won 2 points!']

        if self.name == 'Tommy Grieves':
            global VISITED_TOMMY
            VISITED_TOMMY = True
            return [f'> {YOUR_NAME}: Hey Tommy!',
                    f'> Tommy Grieves: Oh hey, {YOUR_NAME}. What\'s up?',
                    f'> {YOUR_NAME}: I\'m alright. Um, do you remember what happened last night?',
                    '> Tommy Grieves: Yeah. You went ham at the stationary bike last night. Kinda looked like you worked through A LOT of issues.',
                    f'> {YOUR_NAME}: Stationary bike... At the Athletic Centre?',
                    '> Tommy Grieves: Yeah, at the Athletic Centre. Are you hungover or something?',
                    f'> {YOUR_NAME}: No, long story. I\'ll tell you later. Did you see me leave something there?',
                    '> Tommy Grieves: I don\'t know, it was like 4AM when we left. You should go check it out.',
                    f'> {YOUR_NAME}: I would, but I don\'t have my TCard.',
                    '> Tommy Grieves: You can borrow my TCard if you want.',
                    f'> {YOUR_NAME}: Thanks! I\'ll return it to you during dinner.',
                    '> You won 2 points!']

        if self.name == 'Sadie Shaymin':
            global VISITED_SADIE
            VISITED_SADIE = True
            return [f'> {YOUR_NAME}: Morning Sadie!',
                    '> Sadie Shaymin: A purrfect day already, isn\'t it?',
                    f'> {YOUR_NAME}: ...Oookay.',
                    '> Sadie Shaymin: Rude. Anyway, how are you up right meow? I\'m paw-sitive that you ran off to work out after our study session at Graham.',
                    f'> {YOUR_NAME}: Graham Library?',
                    '> Sadie Shaymin: You feline good?',
                    f'> {YOUR_NAME}: ...',
                    '> Sadie Shaymin: Did you fur-get? It was a little cold last night, so we went to that fur-nace of a library. I think you started working on your cheat sheet or something?',
                    f'> {YOUR_NAME}: Oh, alright! See you later.',
                    '> Sadie Shaymin: Cat-ch you later!',
                    '> You won 2 points!']

        if self.name == 'Davis Loo':
            global VISITED_DAVIS
            VISITED_DAVIS = True
            return [f'{YOUR_NAME}: Sup, Davis!',
                    '> Davis Loo: おはよう！(Good morning!)',
                    f'> {YOUR_NAME}: Practicing Japanese early, I see.',
                    '> Davis Loo: そうですね。(Indeed.)',
                    f'> {YOUR_NAME}: What have you been up to recently?',
                    '> Davis Loo: 今日はあさごはんを食べて、アニメを見ました。(Today I ate breakfast and watched anime.)',
                    f'> {YOUR_NAME}: Wow, you\'re suuuch a dilligent student.',
                    '> Davis Loo: いえ、いえ、私はよくない学生ですよ。(No, no, I\'m not a good student.)',
                    f'> {YOUR_NAME}: It was a joke... Anyways, can you remind me of what we were doing last night? I woke up with a massive headache...',
                    '> Davis Loo: ああ、ざんねん。きのうはオイゼで日本語をべんきょうしました。(Ahh, that\'s too bad. Yesterday we were studying Japanese at the OISE.)',
                    '> Davis Loo: おお！あなたはここにチートシートをわすれました。(Oh! You forgot your cheat sheet here.)',
                    f'> {YOUR_NAME}: Oh really? Thank you so much, I\'ll be on the look out!',
                    '> Davis Loo: はい、がんばってね！またね！ (Yes, good luck! See you!)',
                    '> You won 2 points!']

        if self.name == 'Marius Maximus Baddius III':
            global VISITED_MARIUS
            global FOUND_HANDKERCHIEF
            global FOUND_POCKET_MIRROR
            global FOUND_POCKET_WATCH
            global MARIUS_MOVES_GAINED
            global MARIUS_END_GAINED
            global FOUND_ITEMS
            if not VISITED_MARIUS:
                lightgray('> A Strange Ghost: Oh... woe is me!')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: Who are you?')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: I... well, I am the one and only Marius Maximus Baddius the Third!')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: I see...')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: Well, won\'t you inquire me of why I am lamenting at this hour?')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: Uhh, before that, who - or rather what - are you?')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: My fellow friend, alas, I am a ghost. I hath lost all of my memories in the Great Fire.')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: All that is left of my pour soul is this rotting husk of a man. Oh! Woe is me! Woe is me!')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: You\'re a ghost. Really. Then I\'m a bird.')
                time.sleep(2)
                lightgray('> Marius Maximus Baddius III: \'Tis true, \'tis true! However, thyself is not a passerine.')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: It was a joke...')
                time.sleep(2)
                lightgray('> Marius Maximus Baddius III: Ugh, you insolent child! \'Tis not a joking matter!')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: Thou needest to assist me. I must regain my memories... so that I can rise to the heavens at last.')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: And what\'s in it for me?')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: Oh, dear child, there are many accolades one may receive from serving me.')
                time.sleep(2)
                lightgray('> Marius Maximus Baddius III: Thou shall not leave unsatisfied. You have my word.')
                time.sleep(2)
                lightgray(f'> {YOUR_NAME}: Now we\'re talking!')
                time.sleep(2)
                lightgray(
                    '> Marius Maximus Baddius III: Now then, dear child, if thy chooses to aid myself, thou shalt need to remind me of my past through the possessions that I hath lost.')
                time.sleep(2)
                lightgray('> Marius Maximus Baddius III: Make haste!')
                time.sleep(2)
                lightgray('> You won 15 moves!')
                MARIUS_MOVES_GAINED = True
                VISITED_MARIUS = True

            elif not FOUND_ITEMS:
                lightgray(
                    '> Marius Maximus Baddius III: Have you been able to find any of my missing possessions? (yes/no)')
                time.sleep(2)
                reply = input('\033[1;97m\nYour Answer: \033[0m')
                time.sleep(2)
                if reply.lower() == 'yes':
                    if 'Pocket Watch' in p.inventory:
                        lightgray(
                            '> Marius Maximus Baddius III: A... A pocket watch? It looks familiar, but I can\'t quite put my finger on it.')
                        time.sleep(2)
                        return_pocketwatch = ''
                        while return_pocketwatch != 'yes':
                            lightgray(
                                '> Marius Maximus Baddius III: Could you give it to me so I could inspect it further? (yes/no)')
                            time.sleep(2)
                            return_pocketwatch = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightgray('> Marius shuts his eyes and frowns.')
                        time.sleep(2)
                        lightgray(
                            '> Marius Maximus Baddius III: I can envision a sight like I am right there, right now.')
                        time.sleep(2)
                        lightgray(
                            '> Marius Maximus Baddius III: \'Twas the 14th of February in the year of our Lord 1890.')
                        time.sleep(2)
                        lightgray(f'> {YOUR_NAME}: That was the Great Fire of UC!')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: Perhaps. Now quiet, child, and let me speak.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: It was... in the afternoon, I presume.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: A woman...? I remember...')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: Apologies. I seem to have forgotten.')
                        FOUND_POCKET_WATCH = True

                    if 'Pocket Mirror' in p.inventory:
                        lightgray(
                            '> Marius Maximus Baddius III: A small mirror? I haven\'t seen my reflection in decades...')
                        time.sleep(2)
                        return_pocketmirror = ''
                        while return_pocketmirror != 'yes':
                            lightgray(
                                '> Marius Maximus Baddius III: Pray, may you lend me that mirror in your hand? (yes/no)')
                            time.sleep(2)
                            return_pocketmirror = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightgray(
                            '> Marius looks at the mirror and admires his reflection. Suddenly, the image begins to shift.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: That face... The woman looks familiar...')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: ...Both women look familiar.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: My Francesca? Why did she leave?')
                        time.sleep(2)
                        lightgray(
                            '> Marius Maximus Baddius III: And is that... Bernice Sougher? What is she doing here?!')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: ...Oh.')
                        time.sleep(2)
                        lightgray('> The image disappears.')
                        FOUND_POCKET_MIRROR = True

                    if 'Handkerchief' in p.inventory:
                        lightgray('> Marius Maximus Baddius III: Why does that handkerchief have my initials on them?')
                        time.sleep(2)
                        return_handkerchief = ''
                        while return_handkerchief != 'yes':
                            lightgray(
                                '> Marius Maximus Baddius III: Could I borrow that from you for a moment? (yes/no) ')
                            time.sleep(2)
                            return_handkerchief = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightgray(
                            '> Marius carefully examines the handkerchief, brushing a ghostly finger against a small splotch of red on the handkerchief.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: Blood? I thought I died in the fire.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: Ow! Why does my stomach hurt?')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: I remember... I got stabbed.')
                        if FOUND_POCKET_MIRROR:
                            time.sleep(2)
                            lightgray(f'{YOUR_NAME}: Bernice sounds sus...')
                        elif FOUND_POCKET_WATCH:
                            time.sleep(2)
                            lightgray(f'{YOUR_NAME}: The woman sounds sus...')
                        time.sleep(2)
                        lightgray(
                            '> Marius Maximus Baddius III: I felt a sharp pain. And then agony as I bled out and was consumed... by a fire.')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: That\'s all I can recollect.')
                        FOUND_HANDKERCHIEF = True

                    if FOUND_POCKET_WATCH and FOUND_POCKET_MIRROR and FOUND_HANDKERCHIEF:
                        lightgray('> You won 10 moves and 50 points!')
                        time.sleep(2)
                        lightgray('> Marius Maximus Baddius III: Thank you child, for helping me figure out my past.')
                        MARIUS_END_GAINED = True
                        FOUND_ITEMS = True

                    if 'Handkerchief' not in p.inventory and 'Pocket Mirror' not in p.inventory and 'Pocket Watch' not in p.inventory:
                        if p.inventory == []:
                            lightgray(
                                '> Marius Maximus Baddius III: I cannot see anything in your hands. Could you please get my possessions for me?')
                        else:
                            lightgray(
                                '> Marius Maximus Baddius III: Hmm... I don\'t seem to recall any of the items that you\'re holding. Maybe my possessions are somewhere else?')

                elif reply.lower() == 'no':
                    lightgray('> Marius Maximus Baddius III: Oh... Could you please go and find them for me?')

                else:
                    pygame.mixer.Sound.play(SPELLING)

            else:
                lightgray(
                    '> Marius Maximus Baddius III: I can now ascend to a further plane on the next anniversary of my demise.')


def do_action(player_game: Player, location_game: Location, choice_game: str) -> None:
    """Allows for the player to move in four cardinal directions.
    """
    if choice_game in location_game.available_actions():
        if choice_game == 'north':
            player_game.y -= 1
        if choice_game == 'south':
            player_game.y += 1
        if choice_game == 'west':
            player_game.x -= 1
        if choice_game == 'east':
            player_game.x += 1
    else:
        lightgray('This way is blocked.')


# COLORS FUNCTIONS
def bold(skk: str) -> None:
    """Defining bolded text."""
    print("\033[1m{}\033[0m\r".format(skk))


def darkyellow(skk: str) -> None:
    """Defining a dark yellow color for text."""
    print("\033[33m{}\033[0m\r".format(skk))


def darkcyan(skk: str) -> None:
    """Defining a dark cyan color for text."""
    print("\033[36m{}\033[0m\r".format(skk))


def lightgray(skk: str) -> None:
    """Defining a light gray color for text."""
    print("\033[37m{}\033[0m".format(skk))


def red(skk: str) -> None:
    """Defining a red color for text."""
    print("\033[1;91m{}\033[0m\r".format(skk))


def yellow(skk: str) -> None:
    """Defining a yellow color for text."""
    print("\033[93m{}\033[0m\r".format(skk))


def cyan(skk: str) -> None:
    """Defining a cyan color for text."""
    print("\033[1;96m{}\033[0m\r".format(skk))


def white(skk: str) -> None:
    """Defining a white color for text."""
    print("\033[1;97m{}\033[0m\r".format(skk))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 300,
        'extra-imports': ['hashlib']
    })

    SPELLING.set_volume(0.2)
    w = World("map.txt", "locations.txt", "items.txt")
    p = Player(2, 7)  # set starting location of player; you may change the x, y coordinates here as appropriate

    # INSTANCES OF NPCs/SCPs
    linda_shinx = NPC("Linda Shinx", 5, 2)
    tommy_grieves = NPC("Tommy Grieves", 9, 2)
    sadie_shaymin = NPC("Sadie Shaymin", 15, 2)
    davis_loo = NPC("Davis Loo", 16, 2)
    marius_maximus_baddius_iii = NPC("Marius Maximus Baddius III", 50, 10)

    bumbly_mia = SCP("Bumbly and Mia", 13, 5, 5)
    kyoko_tomoyo_pocoyo = SCP("Kyoko, Tomoyo, and Pocoyo", 13, 0, -3)
    chirly = SCP("Chirly", 13, 5, 0)

    room_of_negativity = SCP("Room of Negativity", 10, -5, -1)
    purple_guy = SCP("Purple Guy", 10, -3, -3)
    connor = SCP("Connor", 10, 0, 0)
    tiffany = SCP("Tiffany", 10, 0, 5)
    tikki_plagg = SCP("Tikki and Plagg", 10, -2, 3)

    phone_guy = SCP("Phone Guy", 11, 3, -3)

    # VARIABLES
    menu = ["look", "inventory", "score", "quit", "grab", "drop", "talk"]

    # INITIAL LOCATION AND MOVES INITIALIZATION
    location = w.get_location(p.x, p.y)
    moves = 40

    # START GAME
    pygame.mixer.music.load("kahoot.mp3")
    pygame.mixer.music.set_volume(0.07)
    pygame.mixer.music.play(loops=-1, start=0.7)

    time.sleep(1)
    YOUR_NAME = input("\033[1;97m\nEnter your name: \033[0m")
    time.sleep(1)
    white(
        f'\nHello, {YOUR_NAME}! Welcome to The Amazing Digital Adventure. Type [MENU] to get a list of commands that you can call at any time. You are able to move in all four cardinal directions too, if the location permits.')
    time.sleep(1)

    while not p.victory and not p.quit and moves > 0:
        location = w.get_location(p.x, p.y)
        loc = location.pos

        # VISITED CHECKER
        if PLACES[loc] > 0:
            location.visited = True
        PLACES[loc] += 1

        # DISPLAY LOCATIONS
        cyan("\n\n" + location.name)
        time.sleep(1)
        if location.visited:
            lightgray(location.brief)
            time.sleep(1)
        else:
            lightgray(location.long)
            time.sleep(1)

        # ROBARTS LIBRARY SCPs
        if loc == 10:
            white('\nThere are unknown entities in this location.')
            time.sleep(1)
            selection = input('\033[1;97m\nWould you like to explore? (yes/no) \033[0m')
            time.sleep(1)
            if selection.lower() == 'yes':
                door = input("\033[1;97m\nChoose a number from 1 to 5: \033[0m")
                time.sleep(1)
                if door == '1':
                    if not VISITED_NEGATIVITY_ROOM:
                        pygame.mixer.music.load("tadc.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=16)
                        lst = room_of_negativity.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves -= 1
                        p.score -= 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_NEGATIVITY_ROOM = True
                    else:
                        lightgray("> You try pulling on the door with all your might, but you can\'t seem to open it.")
                        time.sleep(1)
                elif door == '2':
                    if not VISITED_PURPLE_GUY:
                        pygame.mixer.music.load("fnaf.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=42.8)
                        lst = purple_guy.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves -= 3
                        p.score -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_PURPLE_GUY = True
                    else:
                        lightgray(
                            "> The second your hand touches the doorknob, flashbacks of your last encounter in this room flood your mind. You barely escaped last time, so why try again?")
                        time.sleep(1)
                elif door == '3':
                    if not VISITED_CONNOR:
                        pygame.mixer.music.load("connor.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=64)
                        if connor.puzzle():
                            moves += 5
                            p.score += 5
                        else:
                            moves -= 1
                            p.score -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_CONNOR = True
                    else:
                        lightgray("> You open the door. Connor just shakes his and closes it back.")
                        time.sleep(1)
                elif door == '4':
                    if not VISITED_TIFFANY:
                        pygame.mixer.music.load("sao.mp3")
                        pygame.mixer.music.set_volume(0.05)
                        pygame.mixer.music.play(loops=-1)
                        lst = tiffany.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves += 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_TIFFANY = True
                    else:
                        lightgray(
                            "> You peek through the peephole and see that Tiffany is still busy with his chips. You\'d rather not disturb him.")
                        time.sleep(1)
                elif door == '5':
                    if not VISITED_TIKKI_PLAGG:
                        pygame.mixer.music.load("mlb.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, fade_ms=2000)
                        if tikki_plagg.puzzle():
                            moves += 3
                            p.score -= 2
                        else:
                            moves -= 1
                            p.score -= 2
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                    else:
                        lightgray(
                            "> Plagg and Tikki are probably still at Adrien\'s place because you don't see either of them in the room.")
                        time.sleep(1)
                else:
                    pygame.mixer.Sound.play(SPELLING)
            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(SPELLING)

        # ROBARTS COMMONS SCPs
        if loc == 13:
            white('\nThere are unknown entities in this location.')
            time.sleep(1)
            selection = input('\033[1;97m\nWould you like to explore? (yes/no) \033[0m')
            time.sleep(1)
            if selection.lower() == 'yes':
                door = input('\033[1;97m\nChoose a number from 1 to 3: \033[0m')
                time.sleep(1)
                if door == '1':
                    if not VISITED_BUMBLY_MIA:
                        pygame.mixer.music.load("dog.mp3")
                        pygame.mixer.music.set_volume(0.08)
                        pygame.mixer.music.play(loops=-1)
                        lst = bumbly_mia.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves += 5
                        p.score += 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_BUMBLY_MIA = True
                    else:
                        lightgray("> You walk in. Bumbly and Mia are nowhere to be seen.")
                        time.sleep(1)
                elif door == '2':
                    if not VISITED_KYOKO_TOMOYO_POCOYO:
                        pygame.mixer.music.load("cat.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=0.5)
                        lst = kyoko_tomoyo_pocoyo.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_KYOKO_TOMOYO_POCOYO = True
                    else:
                        lightgray(
                            "> You walk in. One of the volunteers asks you to leave due to the one visit per person policy.")
                        time.sleep(1)
                elif door == '3':
                    if not VISITED_CHIRLY:
                        pygame.mixer.music.load("birdcage.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1)
                        lst = chirly.puzzle()
                        for text in lst:
                            lightgray(text)
                            time.sleep(2)
                        moves += 10
                        p.score += 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        VISITED_CHIRLY = True
                    else:
                        lightgray("> You walk in. The room is empty. Seems like Chirly flew away.")
                        time.sleep(1)
                else:
                    pygame.mixer.Sound.play(SPELLING)
            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(SPELLING)

        # PHONE GUY SCP
        if loc == 11:
            white('\nThere is an unknown entity in this location.')
            time.sleep(1)
            selection = input('\033[1;97m\nWould you like to explore? (yes/no) \033[0m')
            time.sleep(1)
            if selection.lower() == 'yes':
                if not VISITED_PHONE_GUY:
                    pygame.mixer.music.load("phoneguy.mp3")
                    pygame.mixer.music.set_volume(0.08)
                    pygame.mixer.music.play(start=5)
                    phone_guy.puzzle()

                    pygame.mixer.music.load("fnaf.mp3")
                    pygame.mixer.music.set_volume(0.04)
                    pygame.mixer.music.play(loops=-1, start=0)

                    moves -= 3
                    p.score += 3

                    time.sleep(2)
                    lightgray('\n> The phone suddenly rings again.')
                    time.sleep(2)
                    lightgray('> Phone Guy: Hello? Hello, hello?')
                    time.sleep(2)
                    lightgray(f'> Phone Guy: Oh, it\'s you again, {YOUR_NAME}.')
                    time.sleep(2)
                    lightgray(
                        '> Phone Guy: Now that you gained a basic sense of this game\'s mechanics, would you like to play a game? (yes/no)')
                    time.sleep(2)
                    response = input('\033[1;97m\nYour Answer: \033[0m')

                    if response.lower() == 'yes':
                        pity = 0

                        time.sleep(2)
                        lightgray('> Phone Guy: Uh, welcome to The Amazing Digital Gacha Gambling Game.')

                        time.sleep(2)
                        lightgray('> Phone Guy: You can exit anytime by typing \"leave.\"')

                        time.sleep(2)
                        lightgray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                        while moves > 0 and answer != 'leave':
                            # END: NO MOVES LEFT
                            if moves <= 0:
                                red("\n\nYou've reached the maximum number of moves. Game over!")
                                time.sleep(1)
                                darkyellow("\nYour final score is: " + str(p.score) + "\n")
                                time.sleep(1)

                            if pity >= 90:
                                chance = random.randint(1, 2)
                                if chance == 1:
                                    moves += 100
                                    p.score += 100
                                    time.sleep(2)
                                    lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                    time.sleep(2)
                                    lightgray('> You won 100 moves and 100 points!')
                                    pity = 0
                                else:
                                    moves += 35
                                    p.score += 35
                                    time.sleep(2)
                                    lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                    time.sleep(2)
                                    lightgray('> You won 35 moves and 35 points!')
                                    pity = 0

                            elif 76 <= pity <= 80:
                                if answer.lower() == '1':
                                    pity += 1
                                    rand = random.randint(1, 500)

                                    if 1 <= rand <= 25:
                                        chance = random.randint(1, 2)
                                        if chance == 1:
                                            moves += 100
                                            p.score += 100
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightgray('> You won 100 moves and 100 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightgray('> You won 35 moves and 35 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0

                                    elif 26 <= rand <= 50:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightgray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightgray('> You won 5 moves and 5 points!')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightgray('> You lost 1 move and won 1 point.')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                elif answer.lower() == '10':
                                    pity += 10
                                    for i in range(0, 10):
                                        rand = random.randint(1, 500)

                                        if 1 <= rand <= 3:
                                            chance = random.randint(1, 2)
                                            if chance == 1:
                                                moves += 100
                                                p.score += 100
                                                time.sleep(2)
                                                lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightgray('> You won 100 moves and 100 points!')
                                                pity = 0
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightgray(
                                                    '> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightgray('> You won 35 moves and 35 points!')
                                                pity = 0

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightgray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightgray('> You lost 1 move and won 1 point.')
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                                else:
                                    pygame.mixer.Sound.play(SPELLING)
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                            else:
                                if answer.lower() == '1':
                                    pity += 1
                                    rand = random.randint(1, 500)

                                    if 1 <= rand <= 3:
                                        chance = random.randint(1, 2)
                                        if chance == 1:
                                            moves += 100
                                            p.score += 100
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightgray('> You won 100 moves and 100 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightgray('> You won 35 moves and 35 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0

                                    elif 4 <= rand <= 28:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightgray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightgray('> You won 5 moves and 5 points!')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightgray('> You lost 1 move and won 1 point.')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                elif answer.lower() == '10':
                                    pity += 10
                                    for i in range(0, 10):
                                        rand = random.randint(1, 500)

                                        if 1 <= rand <= 3:
                                            chance = random.randint(1, 2)
                                            if chance == 1:
                                                moves += 100
                                                p.score += 100
                                                time.sleep(2)
                                                lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightgray('> You won 100 moves and 100 points!')
                                                pity = 0
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightgray(
                                                    '> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightgray('> You won 35 moves and 35 points!')
                                                pity = 0

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightgray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightgray('> You lost 1 move and won 1 point.')
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                                else:
                                    pygame.mixer.Sound.play(SPELLING)
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                        time.sleep(2)
                        lightgray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    elif response.lower() == 'no':
                        time.sleep(2)
                        lightgray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    else:
                        pygame.mixer.Sound.play(SPELLING)

                    pygame.mixer.music.load("kahoot.mp3")
                    pygame.mixer.music.set_volume(0.07)
                    pygame.mixer.music.play(loops=-1, start=0.7)
                    VISITED_PHONE_GUY = True

                else:
                    pygame.mixer.music.load("fnaf.mp3")
                    pygame.mixer.music.set_volume(0.04)
                    pygame.mixer.music.play(loops=-1, start=0)

                    lightgray('> You notice a mysterious blue telephone on the ground.')
                    time.sleep(2)
                    lightgray('> The phone suddenly starts ringing.')
                    time.sleep(2)
                    lightgray('> Phone Guy: Hello? Hello, hello?')
                    time.sleep(2)
                    lightgray(f'> Phone Guy: Oh, it\'s you again, {YOUR_NAME}.')
                    time.sleep(2)
                    lightgray(
                        '> Phone Guy: Now that you gained a basic sense of this game\'s mechanics, would you like to play a game? (yes/no)')
                    time.sleep(2)
                    response = input('\033[1;97m\nYour Answer: \033[0m')

                    if response.lower() == 'yes':
                        pity = 0

                        time.sleep(2)
                        lightgray('> Phone Guy: Uh, welcome to The Amazing Digital Gacha Gambling Game.')

                        time.sleep(2)
                        lightgray('> Phone Guy: You can exit anytime by typing \"leave.\"')

                        time.sleep(2)
                        lightgray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                        while moves > 0 and answer != 'leave':
                            # END: NO MOVES LEFT
                            if moves <= 0:
                                red("\n\nYou've reached the maximum number of moves. Game over!")
                                time.sleep(1)
                                darkyellow("\nYour final score is: " + str(p.score) + "\n")
                                time.sleep(1)

                            if pity >= 90:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    moves += 100
                                    p.score += 100
                                    time.sleep(2)
                                    lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                    time.sleep(2)
                                    lightgray('> You won 100 moves and 100 points!')
                                    pity = 0
                                else:
                                    moves += 35
                                    p.score += 35
                                    time.sleep(2)
                                    lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                    time.sleep(2)
                                    lightgray('> You won 35 moves and 35 points!')
                                    pity = 0

                            elif 76 <= pity <= 80:
                                if answer.lower() == '1':
                                    pity += 1
                                    rand = random.randint(1, 500)

                                    if 1 <= rand <= 25:
                                        chance = random.randint(1, 2)
                                        if chance == 1:
                                            moves += 100
                                            p.score += 100
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightgray('> You won 100 moves and 100 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightgray('> You won 35 moves and 35 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0

                                    elif 26 <= rand <= 50:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightgray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightgray('> You won 5 moves and 5 points!')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightgray('> You lost 1 move and won 1 point.')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                elif answer.lower() == '10':
                                    pity += 10
                                    for i in range(0, 10):
                                        rand = random.randint(1, 500)

                                        if 1 <= rand <= 3:
                                            chance = random.randint(1, 2)
                                            if chance == 1:
                                                moves += 100
                                                p.score += 100
                                                time.sleep(2)
                                                lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightgray('> You won 100 moves and 100 points!')
                                                pity = 0
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightgray(
                                                    '> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightgray('> You won 35 moves and 35 points!')
                                                pity = 0

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightgray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightgray('> You lost 1 move and won 1 point.')
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                                else:
                                    pygame.mixer.Sound.play(SPELLING)
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                            else:
                                if answer.lower() == '1':
                                    pity += 1
                                    rand = random.randint(1, 500)

                                    if 1 <= rand <= 3:
                                        chance = random.randint(1, 2)
                                        if chance == 1:
                                            moves += 100
                                            p.score += 100
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightgray('> You won 100 moves and 100 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightgray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightgray('> You won 35 moves and 35 points!')
                                            lightgray(
                                                '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            pity = 0

                                    elif 4 <= rand <= 28:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightgray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightgray('> You won 5 moves and 5 points!')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightgray('> You lost 1 move and won 1 point.')
                                        lightgray(
                                            '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                elif answer.lower() == '10':
                                    pity += 10
                                    for i in range(0, 10):
                                        rand = random.randint(1, 500)

                                        if 1 <= rand <= 3:
                                            chance = random.randint(1, 2)
                                            if chance == 1:
                                                moves += 100
                                                p.score += 100
                                                time.sleep(2)
                                                lightgray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightgray('> You won 100 moves and 100 points!')
                                                pity = 0
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightgray(
                                                    '> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightgray('> You won 35 moves and 35 points!')
                                                pity = 0

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightgray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightgray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightgray('> You lost 1 move and won 1 point.')
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                                else:
                                    pygame.mixer.Sound.play(SPELLING)
                                    lightgray(
                                        '\n> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                    answer = input('\033[1;97m\nYour Answer: \033[0m')

                        time.sleep(2)
                        lightgray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    elif response.lower() == 'no':
                        time.sleep(2)
                        lightgray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    else:
                        pygame.mixer.Sound.play(SPELLING)

                    pygame.mixer.music.load("kahoot.mp3")
                    pygame.mixer.music.set_volume(0.07)
                    pygame.mixer.music.play(loops=-1, start=0.7)

            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(SPELLING)

        # DISPLAY OPTIONS
        time.sleep(1)
        white("\nWhat to do?")
        time.sleep(1)
        darkcyan("- [MENU]")
        darkcyan("- North\n- South\n- West\n- East")
        time.sleep(1)
        white('\nMoves: ' + str(moves))
        time.sleep(1)
        choice = input("\033[1;97m\nEnter Action: \033[0m")

        # MENU
        if choice.lower() == "[menu]":
            white("\nWhat to do?")
            time.sleep(1)
            for option in menu:
                darkcyan("- " + option.title())
            choice = input("\033[1;97m\nChoose Action: \033[0m")

        # CARDINAL DIRECTIONS
        if choice.lower() == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            do_action(p, location, choice.lower())

        # LOOK
        if choice.lower() == "look":
            lightgray(location.long + '\n')
            time.sleep(1)

        # INVENTORY
        if choice.lower() == "inventory":
            if p.inventory == []:
                lightgray("You have nothing in your bag.\n")
                time.sleep(1)
            else:
                yellow("\nInventory:")
                for item in p.inventory:
                    yellow("- " + str(item))
                time.sleep(1)

        # SCORE
        if choice.lower() == "score":
            darkyellow("\nScore: " + str(p.score))
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

            if (w.items != [] and all([item_comp.curr_position == -1 for item_comp in w.items])) or curr_items == []:
                lightgray("There are no items in this area!\n")
                time.sleep(1)
            else:
                yellow("\nItems:")
                for item in curr_items:
                    yellow("- " + item)
                time.sleep(1)

                white("\nWhich item do you want to grab?")
                time.sleep(1)
                choice = input("\033[1;97m\nChoose Item: \033[0m")
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
                    pygame.mixer.Sound.play(SPELLING)
                    lightgray("This item does not exist in this area.")
                    time.sleep(1)

        # DROP
        if choice.lower() == "drop":
            all_items = p.inventory
            curr_location = w.get_location(p.x, p.y)
            curr_items = []

            for item_info in all_items:
                curr_items.append(item_info)

            if all_items == []:
                lightgray("You have no items to drop!\n")
                time.sleep(1)
            else:
                yellow("\nInventory:")
                for item in all_items:
                    yellow("- " + str(item))

                white("\nWhich item do you want to drop?")
                time.sleep(1)
                choice = input("\033[1;97m\nChoose Item: \033[0m")
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

                        if chosen_item == 'Water Bottle' and not WATER_DROP and item.curr_position == 8:
                            p.score += 3
                            WATER_DROP = True

                        if chosen_item == 'TCard' and not TCARD_DROP and item.curr_position == 0:
                            p.score += 5
                            TCARD_DROP = True

                        if chosen_item == 'Lucky Pen' and not PEN_DROP and item.curr_position == 0:
                            p.score += 5
                            PEN_DROP = True

                        if chosen_item == 'Cheat Sheet' and not SHEET_DROP and item.curr_position == 0:
                            p.score += 5
                            SHEET_DROP = True
                else:
                    pygame.mixer.Sound.play(SPELLING)
                    lightgray("You don't have this item.")
                    time.sleep(1)

        # TALK
        if choice.lower() == 'talk':
            if loc == 5:
                pygame.mixer.music.load("getaway.mp3")
                pygame.mixer.music.set_volume(0.06)
                pygame.mixer.music.play(loops=-1)
                if not VISITED_LINDA:
                    p.score += 2
                lst = linda_shinx.dialogue()
                for text in lst:
                    lightgray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 6:
                pygame.mixer.music.load("jojo.mp3")
                pygame.mixer.music.set_volume(0.06)
                pygame.mixer.music.play(loops=-1, fade_ms=2000)
                marius_maximus_baddius_iii.dialogue()
                if not MARIUS_MOVES_GAINED:
                    moves += 15
                    MARIUS_MOVES_GAINED = False
                if 'Pocket Watch' in p.inventory and FOUND_POCKET_WATCH:
                    p.inventory.remove('Pocket Watch')
                if 'Pocket Mirror' in p.inventory and FOUND_POCKET_MIRROR:
                    p.inventory.remove('Pocket Mirror')
                if 'Handkerchief' in p.inventory and FOUND_HANDKERCHIEF:
                    p.inventory.remove('Handkerchief')
                if FOUND_ITEMS and VISITED_MARIUS and MARIUS_END_GAINED:
                    moves += 10
                    p.score += 50
                    MARIUS_END_GAINED = False

                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 9:
                pygame.mixer.music.load("whistle.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.5)
                if not VISITED_TOMMY:
                    p.score += 2
                lst = tommy_grieves.dialogue()
                for text in lst:
                    lightgray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 15:
                pygame.mixer.music.load("tangled.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1)
                if not VISITED_SADIE:
                    p.score += 2
                lst = sadie_shaymin.dialogue()
                for text in lst:
                    lightgray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 16:
                pygame.mixer.music.load("renai.mp3")
                pygame.mixer.music.set_volume(0.04)
                pygame.mixer.music.play(loops=-1, start=0.7)
                if not VISITED_DAVIS:
                    p.score += 2
                lst = davis_loo.dialogue()
                for text in lst:
                    lightgray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            else:
                lightgray("There is no one to talk to here.")
                time.sleep(1)

        # MISSPELLING
        if choice.lower() not in ['north', 'south', 'east', 'west', '[menu]', 'look', 'inventory', 'score', 'quit',
                                  'grab', 'drop', 'talk', 'quit', 'cheat sheet', 'lucky pen', 'tcard', 'water bottle',
                                  'pocket watch', 'handkerchief', 'pocket mirror']:
            pygame.mixer.Sound.play(SPELLING)

        # UPDATE MOVES COUNTER
        if choice.lower() in ['north', 'south', 'east', 'west', 'grab', 'drop']:
            moves -= 1

        # VICTORY
        if WATER_DROP and TCARD_DROP and PEN_DROP and SHEET_DROP and loc == 0:
            p.victory = True

    # END: QUIT
    if p.quit:
        red("\n\nYou have successfully quit the game!")
        time.sleep(1)
        darkyellow("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)

    # END: VICTORY
    if p.victory:
        red("\n\nCongrats! You won!")
        time.sleep(1)
        darkyellow("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)

    # END: NO MOVES LEFT
    if moves <= 0:
        red("\n\nYou've reached the maximum number of moves. Game over!")
        time.sleep(1)
        darkyellow("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)
