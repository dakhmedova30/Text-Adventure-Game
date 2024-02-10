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
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from game_data import World, Item, Location, Player
import time
import random
from typing import Optional, Any
import pygame
pygame.init()
pygame.mixer.init()


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

visited_linda = False
visited_tommy = False
visited_davis = False
visited_sadie = False
visited_bumbly_mia = False
visited_kyoko_tomoyo_pocoyo = False
visited_chirly = False
visited_negativity_room = False
visited_purple_guy = False
visited_connor = False
visited_tiffany = False
visited_tikki_plagg = False
visited_marius_maximus_baddius_iii = False
visited_phone_guy = False
found_items = False
found_pocket_mirror = False
found_pocket_watch = False
found_handkerchief = False
marius_moves_gained = False
marius_end_gained = False


class Beings:
    """Parent class for various enhancement SCPs (everything you meet at the Robarts Library and Commons, as well as Phone Guy) 
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

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points
        self.moves = moves


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
        - -5 <= self.moves <= 5
    """

    def __init__(self, name: str, curr_pos: int, points: int, moves: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points

    def puzzle(self) -> Any:
        """Dialogue that pops up when you visit a room for the first time along with the 
        amount of moves and/or points you gain/lose and the questions some of them ask.
        """
        if self.name == 'Bumbly and Mia':
            return ['> You hear quite a commotion as you walk into the room.',
            '> Two dogs greet you: one is a large and fluffy Samoyed, and the other is a small and soft Keeshond.',
            '> Their nametags read Bumbly and Mia, respectively.',
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
            return ['> You enter the room and see a sole birdcage.',
            '> Inside, there is a yellow-green parrotlet named Chirly yapping away.',
            '> Chirly: Squawk! He\'s dead! He\'s dead!',
            f'> {your_name}: Who\'s... dead?',
            '> Chirly: Marius! Marius! Squawk! He\'s dead! Squawk!',
            f'> {your_name}: Marius? How did he die?',
            '> Chirly: He was stabbed! Squawk! 28 times!',
            f'> {your_name}: That\'s crazy... Who did it? Where? When?',
            '> Chirly: He\'s dead! Detective, he\'s dead! Squawk!',
            f'> {your_name}: Can you at least tell me why?',
            '> Chirly: Squawk! He\'s dead! Case closed! Squawk!',
            '> It seems like Chirly has nothing else to say.',
            '> You gain 5 moves and 3 points!']

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
            '> You lose 1 move and 5 points.']
            
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
            '> Purple Guy: Let\'s see how many times you can be pulled apart...and put back together again.',
            '> Despite the man\'s unsettling comments, you try to pull any strength you have left to run away.',
            '> The yellow bunny gawks at you, patronizingly, before beginning his chase.',
            '> Purple Guy: Hide if you want. It did not save the others. It will not save you.',
            '> However, just before he was able to catch up, you heard a thud.',
            '> Upon turning around, the terrifying sight of a springlocked human amalgamation plastered your mind.',
            '> All you could hear was a faint \"I always come back\" as you waddled away in your new suit.',
            '> You lose 3 moves and 3 points. Tip: Try to not get stuffed into an animatronic suit next time.']
        
        if self.name == 'Connor':
            correct = False
            lightGray('> Connor: My name is Connor. I\'m the android sent by CyberLife to test your intelligence.')
            time.sleep(2)
            lightGray('> Connor: If you answer my riddle correctly, you shall receive a reward.')
            time.sleep(2)
            lightGray('> Connor: Answer incorrectly and you shall be penalized.')
            time.sleep(2)
            lightGray('> Connor: Finish this quote: An eye for an eye and the whole world goes _.')
            time.sleep(2)
            for i in range(0, 3):
                answer = input('\033[1;97m\nYour Answer: \033[0m')
                time.sleep(2)
                if answer.lower() == 'blind':
                    correct = True
                    lightGray('> Connor: Congrats, you have answered correctly.')
                    time.sleep(2)
                    lightGray('> You gain 5 moves and 5 points!')
                    return True
                else:
                    lightGray('> Connor: Your guess was incorrect, please try again.')
                    time.sleep(2)
            if correct == False:
                lightGray('> Connor: You were unable to answer it correctly.')
                time.sleep(2)
                lightGray('> You lose 1 move and 3 points.')
                return False
            
        if self.name == 'Tiffany':
            return ['> The second you step inside the door, you are greeted by a loud, booming voice.',
            '> The Voice: \"I am known by many names. \'Mountain Slayer\', \'Thunder Lion\', \'The Chocolate Axe\'. But you? You may call me... TIFFANY.\"',
            f'> {your_name}: Hi Tiffany. I\'m {your_name}.',
            '> Tiffany is a large, buff man who is sitting on the floor with bags of snacks around him.',
            '> Tiffany: People die when they are killed. Did you know that before? Did you? Because I didn\'t! I just learned that from the voices inside my head.',
            f'> {your_name}: Um yeah, I knew about that for a while.',
            '> Tiffany: Wow, you\'re so smart! Just like Edwardison! Not me though. Anyway, I\'m hungry. Do you want a snack?',
            '> He holds a bag of chips in your direction.',
            f'> {your_name}: No thanks, not right now. I gotta get going.',
            '> Tiffany nods at you and waves.',
            '> Tiffany: I take a potato chip. AND EAT IT!',
            '> You gain 5 moves!']
            
        if self.name == 'Tikki and Plagg':
            global visited_tikki_plagg
            correct = 0
            lightGray('> A Floating Black Cat: Well hello there, human, ya got any Camembert on you?')
            time.sleep(2)
            lightGray('> A Floating Black Cat: Neverminddd, I can already smell your lack of taste for cheese.')
            time.sleep(2)
            lightGray('> A Floating Black Cat: Well since Tikki is probably overindulging on Galettes, how about you entertain me?')
            time.sleep(2)
            lightGray('> A Floating Black Cat: I\'ll give you three questions and if you answer all of them right, then you\'ll get some stinky rewards, haha!')
            time.sleep(2)
            lightGray('> A Floating Black Cat: This first one is easy.')
            time.sleep(2)
            lightGray('> A Floating Black Cat: What is the best cheese in the entire world? ')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            if riddle.lower() == 'camembert':
                correct += 1
                time.sleep(2)
                lightGray('> A Floating Black Cat: That\'s right! I\'m already missing Adrien\'s stash of cheese...')
            elif riddle.lower() == 'cheddar' or riddle.lower() == 'swiss':
                time.sleep(2)
                lightGray('> A Floating Black Cat: Pretty good options, but Camembert stays on top!')
            else:
                time.sleep(2)
                lightGray('> A Floating Black Cat: I can\'t believe you would say that, gross!')
                
            time.sleep(2)
            lightGray('> A Floating Black Cat: Now, onto the next question!')
            time.sleep(2)
            lightGray('> A Floating Black Cat: No, no, wait! I haven\'t even introduced myself!')
            time.sleep(2)
            lightGray('> Plagg: I am Plagg, the one and ONLY kwami known for tilting the Leaning Tower of Pisa,')
            time.sleep(2)
            lightGray('> Plagg: Destroying the entirety of Atlantis, and driving the dinosaurs to extinction.')
            time.sleep(2)
            lightGray('> Plagg: Not a bad resume, right?')
            time.sleep(2)
            lightGray('> Plagg: Well then, what do you think I am the kwami of?')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            time.sleep(2)
            if riddle.lower() == 'destruction' or riddle.lower() == 'cataclysm' or riddle.lower() == 'bad luck':
                correct += 1
                lightGray('> Plagg: Ooh, you\'ve been paying attention!')
                time.sleep(2)
            else:
                lightGray('> Plagg: Honestly, what is in your head? American cheese?')
                time.sleep(2)
            
            lightGray('> Plagg: Question number three, no hints this time though, only digits.')
            time.sleep(2)
            lightGray('> Plagg: What is the answer to everything?')
            time.sleep(2)
            riddle = input('\033[1;97m\nYour Answer: \033[0m')
            time.sleep(2)
            if riddle == '42':
                correct += 1
                lightGray('> Plagg: Ding, ding, ding! You\'re correct!')
                time.sleep(2)
                lightGray('> Plagg: I found that book on Adrien\'s desk, but it was actually pretty boring.')
                time.sleep(2)
                if correct == 3:
                    time.sleep(2)
                    lightGray('> Tikki: Plagg! What are you doing?')
                    time.sleep(2)
                    lightGray('> Plagg: Just entertaining myself, Sugarcube.')
                    time.sleep(2)
                    lightGray(f'> Tikki: Honestly... you\'re so immature. Leave {your_name} alone. And stop calling me that.')
                    time.sleep(2)
                    lightGray('> Plagg: Whatever you say, Sugarcube.')
                    time.sleep(2)
                    lightGray('> You gain 3 moves and lose 2 points.')
                    visited_tikki_plagg = True
                    return True
                else:
                    time.sleep(2)
                    lightGray('> Plagg: Unfortunately, you didn\'t get all my questions right, so no prize for you.')
                    time.sleep(2)
                    lightGray('> Plagg: Smell you later!')
                    lightGray('> You lose 1 move and lose 2 points.')
                    visited_tikki_plagg = True
                    return False
            else:
                time.sleep(2)
                lightGray('\n> Plagg: Too bad. Try again next time, buddy. I\'m going to find Adrien...')
                lightGray('> You lose 1 move and lose 2 points.')
                visited_tikki_plagg = True
                return False

        if self.name == 'Phone Guy':
            lightGray('> You notice a mysterious blue telephone on the ground.')
            time.sleep(1)
            lightGray('> It begins ringing...')
            time.sleep(9)
            lightGray('> Phone Guy: Hello? Hello, hello?')
            time.sleep(3)
            lightGray('> Phone Guy: Uh, I wanted to record a message for you to help you get settled into this text adventure game.')
            time.sleep(6)
            lightGray('> Phone Guy: Um, I actually was the player before you. I\'m finishing up my last playthrough now, as a matter of fact.')
            time.sleep(7)
            lightGray('> Phone Guy: So, I know it can be a bit overwhelming, but I\'m here to tell you there\'s nothing to worry about. Uh, you\'ll do fine.')
            time.sleep(8)
            lightGray('> Phone Guy: So, let\'s just focus on getting you through the game, okay?')
            time.sleep(5)
            lightGray('> Phone Guy: Uh, let\'s see, first there\'s an introductory greeting from the game developers that I\'m supposed to read.')
            time.sleep(6)
            lightGray('> Phone Guy: Uh, it\'s kind of a legal thing, you know.')
            time.sleep(3)
            lightGray(f'> Phone Guy: Um, \"Welcome to The Amazing Digital Adventure, {your_name}. A magical place for kids and grown-ups alike, where fantasy and fun come to life.\"')
            time.sleep(9)
            lightGray('> Phone Guy: \"Comp Sci Entertainment is not responsible for damage to property or person.\"')
            time.sleep(4)
            lightGray('> Phone Guy: \"Upon discovering that despair or expiration has occurred, a missing person report will be filed within 90 days, or as soon property and premises have been thoroughly cleaned and checked, and the carpets have been replaced.\"')
            time.sleep(11)
            lightGray('> Phone Guy: Blah, blah, blah. Now that might sound bad, I know, but there\'s surely nothing to worry about.')
            time.sleep(6)
            lightGray('> Phone Guy: Uh, the SCP and NPC characters here do get a bit quirky at night, but do I blame them? No.')
            time.sleep(6)
            lightGray('> Phone Guy: If I were forced to say those same stupid lines for twenty years and I never got a bath? I\'d probably be a bit irritable at night too.')
            time.sleep(9)
            lightGray('> Phone Guy: So, remember, these characters hold a special place in the hearts of children and we need to show them a little respect, right? Okay.')
            time.sleep(8)
            lightGray('> Phone Guy: So, just be aware, the characters do tend to wander a bit. Uh, they\'re left in some kind of free roaming mode at night.')
            time.sleep(8)
            lightGray('> Phone Guy: Uh... something about their code bugging up if they get turned off for too long.')
            time.sleep(5)
            lightGray('> Phone Guy: Uh, they used to be allowed to walk around during the day too. But then there was The Bite of \'87. Yeah.')
            time.sleep(7)
            lightGray('> Phone Guy: I-It\'s amazing that they human body can live without the frontal lobe, you know?')
            time.sleep(5)
            lightGray('> Phone Guy: Uh, now concerning your safety, the only real risk to you as a player here, if any, is the fact that these characters, uh, if they happen to see you after hours, probably won\'t recognize you as a person.')
            time.sleep(14)
            lightGray('> Phone Guy: They\'ll pr- they\'ll most likely see you as an amalgamation of HTML without its CSS on.')
            time.sleep(5)
            lightGray('> Phone Guy: Now since that\'s against the rules here at The Amazing Digital Adventure, they\'ll probably try to... forcefully stuff you inside a Being class.')
            time.sleep(10)
            lightGray('> Phone Guy: Um, now, that wouldn\'t be so bad if the classes themselves weren\'t filled with instance attributes, representation invariants, and functions, especially around the top area.')
            time.sleep(11)
            lightGray('> Phone Guy: So, you could imagine how having your head forcefully pressed inside one of those could cause a bit of discomfort... and expiration.')
            time.sleep(8)
            lightGray('> Phone Guy: Uh, the only parts of you that would likely see the light of day again would be your eyeballs and teeth when they merge with the pre-existing code, heh.')
            time.sleep(7)
            lightGray('> Phone Guy: Y-yeah, they don\'t tell you these things when you sign up. But hey, your first playthrough should be a breeze.')
            time.sleep(5)
            lightGray('> Phone Guy: I\'ll chat with you tomorrow. Uh, check those rooms, and remember to quit the game only if absolutely necessary.')
            time.sleep(6)
            lightGray('> Phone Guy: Gotta conserve your moves. Alright, goodbye.')
            time.sleep(4)
            lightGray('> The phone call ends.')


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

    def __init__(self, name: str, curr_pos: int, points: int) -> None:
        """Initialize a new being.
        """
        self.name = name
        self.curr_pos = curr_pos
        self.points = points

    def dialogue(self) -> Any:
        """The conversation with the NPCs that pops up every time you choose to TALK in the location they are in.
        """
        if self.name == 'Linda Shinx':
            global visited_linda
            visited_linda = True
            return [f'> {your_name}: Wakey wakey, Linda! It\'s time for school!',
            f'> Linda Shinx: I\'m already awake if you couldn\'t tell.',
            f'> {your_name}: Yeah, I can hear your Taylor Swift music from a mile away.',
            f'> Linda Shinx: Obviously. Think about the place where you first met me.',
            f'> {your_name}: Of course, in a concert. Anyways, can you help me remember what happened yesterday?',
            f'> Linda Shinx: Look who needs my help now~. All you need to do is \"shake it off.\" ;)',
            f'> {your_name}: I\'m being serious, Linda. I have a terrible headache and my exam is today!',
            f'> Linda Shinx: Okay, okay, I hear you. Well, first things first, be sure to drink lots of water. Hydrate, or diedrate, y\'know?',
            f'> {your_name}: Drink water... Wait! I didn\'t see my water bottle in my room. Oh my gosh, do you think I lost it?!',
            f'> Linda Shinx: Silly {your_name}. You left it at Sid Smith!',
            f'> {your_name}: Thanks, bestie, I can always count on you. I better get going then!',
            f'> Linda Shinx: Adiós, {your_name}!',
            f'> You gain 2 moves and 5 points!']

        if self.name == 'Tommy Grieves':
            global visited_tommy
            visited_tommy = True
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
            f'> {your_name}: Thanks! I\'ll return it to you during dinner.',
            f'> You gain 2 moves and 9 points!']

        if self.name == 'Sadie Shaymin':
            global visited_sadie
            visited_sadie = True
            return [f'> {your_name}: Morning Sadie!',
            f'> Sadie Shaymin: A purrfect day already, isn\'t it?',
            f'> {your_name}: ...Oookay.',
            f'> Sadie Shaymin: Rude. Anyway, how are you up right meow? I\'m paw-sitive that you ran off to work out after our study session at Graham.',
            f'> {your_name}: Graham Library?',
            f'> Sadie Shaymin: You feline good?',
            f'> {your_name}: ...',
            f'> Sadie Shaymin: Did you fur-get? It was a little cold last night, so we went to that fur-nace of a library. I think you started working on your cheat sheet or something?',
            f'> {your_name}: Oh, alright! See you later.',
            f'> Sadie Shaymin: Cat-ch you later!',
            f'> You gain 2 moves and 16 points!']
            
        if self.name == 'Davis Loo':
            global visited_davis
            visited_davis = True
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
            f'> Davis Loo: はい、がんばってね！またね！ (Yes, good luck! See you!)',
            f'> You gain 2 moves and 16 points!']

        if self.name == 'Marius Maximus Baddius III':
            global visited_marius_maximus_baddius_iii
            global found_handkerchief
            global found_pocket_mirror
            global found_pocket_watch
            global marius_moves_gained
            global marius_end_gained
            global found_items
            if visited_marius_maximus_baddius_iii == False:
                lightGray('> A Strange Ghost: Oh... woe is me!')
                time.sleep(2)
                lightGray(f'> {your_name}: Who are you?')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: I... well, I am the one and only Marius Maximus Baddius the Third!')
                time.sleep(2)
                lightGray(f'> {your_name}: I see...')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Well, won\'t you inquire me of why I am lamenting at this hour?')
                time.sleep(2)
                lightGray(f'> {your_name}: Uhh, before that, who - or rather what - are you?')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: My fellow friend, alas, I am a ghost. I hath lost all of my memories in the Great Fire.')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: All that is left of my pour soul is this rotting husk of a man. Oh! Woe is me! Woe is me!')
                time.sleep(2)
                lightGray(f'> {your_name}: You\'re a ghost. Really. Then I\'m a bird.')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: \'Tis true, \'tis true! However, thyself is not a passerine.')
                time.sleep(2)
                lightGray(f'> {your_name}: It was a joke...')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Ugh, you insolent child! \'Tis not a joking matter!')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Thou needest to assist me. I must regain my memories... so that I can rise to the heavens at last.')
                time.sleep(2)
                lightGray(f'> {your_name}: And what\'s in it for me?')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Oh, dear child, there are many accolades one may receive from serving me.')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Thou shall not leave unsatisfied. You have my word.')
                time.sleep(2)
                lightGray(f'> {your_name}: Now we\'re talking!')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Now then, dear child, if thy chooses to aid myself, thou shalt need to remind me of my past through the possessions that I hath lost.')
                time.sleep(2)
                lightGray('> Marius Maximus Baddius III: Make haste!')
                time.sleep(2)
                lightGray('> You gain 15 moves!')
                marius_moves_gained = True
                visited_marius_maximus_baddius_iii = True
                
            elif found_items == False:
                lightGray('> Marius Maximus Baddius III: Have you been able to find any of my missing possessions? (yes/no)')
                time.sleep(2)
                response = input('\033[1;97m\nYour Answer: \033[0m')
                time.sleep(2)
                if response.lower() == 'yes':
                    if 'Pocket Watch' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: A... A pocket watch? It looks familiar, but I can\'t quite put my finger on it.')
                        time.sleep(2)
                        return_pocketwatch = ''
                        while return_pocketwatch != 'yes':
                            lightGray('> Marius Maximus Baddius III: Could you give it to me so I could inspect it further? (yes/no)')
                            time.sleep(2)
                            return_pocketwatch = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightGray('> Marius shuts his eyes and frowns.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: I can envision a sight like I am right there, right now.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: \'Twas the 14th of February in the year of our Lord 1890.')
                        time.sleep(2)
                        lightGray(f'> {your_name}: That was the Great Fire of UC!')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: Perhaps. Now quiet, child, and let me speak.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: It was... in the afternoon, I presume.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: A woman...? I remember...')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: Apologies. I seem to have forgotten.')
                        found_pocket_watch = True

                    if 'Pocket Mirror' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: A small mirror? I haven\'t seen my reflection in decades...')
                        time.sleep(2)
                        return_pocketmirror = ''
                        while return_pocketmirror != 'yes':
                            lightGray('> Marius Maximus Baddius III: Pray, may you lend me that mirror in your hand? (yes/no)')
                            time.sleep(2)
                            return_pocketmirror = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightGray('> Marius looks at the mirror and admires his reflection. Suddenly, the image begins to shift.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: That face... The woman looks familiar...')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: ...Both women look familiar.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: My Francesca? Why did she leave?')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: And is that... Bernice Sougher? What is she doing here?!')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: ...Oh.')
                        time.sleep(2)
                        lightGray('> The image disappears.')
                        found_pocket_mirror = True
                        
                    if 'Handkerchief' in p.inventory:
                        lightGray('> Marius Maximus Baddius III: Why does that handkerchief have my initials on them?')
                        time.sleep(2)
                        return_handkerchief = ''
                        while return_handkerchief != 'yes':
                            lightGray('> Marius Maximus Baddius III: Could I borrow that from you for a moment? (yes/no) ')
                            time.sleep(2)
                            return_handkerchief = input('\033[1;97m\nYour Answer: \033[0m')
                            time.sleep(2)
                        lightGray('> Marius carefully examines the handkerchief, brushing a ghostly finger against a small splotch of red on the handkerchief.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: Blood? I thought I died in the fire.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: Ow! Why does my stomach hurt?')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: I remember... I got stabbed.')
                        if found_pocket_mirror == True:
                            time.sleep(2)
                            lightGray(f'{your_name}: Bernice sounds sus...')
                        elif found_pocket_watch == True:
                            time.sleep(2)
                            lightGray(f'{your_name}: The woman sounds sus...')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: I felt a sharp pain. And then agony as I bled out and was consumed... by a fire.')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: That\'s all I can recollect.')
                        found_handkerchief = True

                    if found_pocket_watch and found_pocket_mirror and found_handkerchief:
                        lightGray('> You gain 10 moves and 50 points!')
                        time.sleep(2)
                        lightGray('> Marius Maximus Baddius III: Thank you child, for helping me figure out my past.')
                        marius_end_gained = True
                        found_items = True
                        
                    if 'Handkerchief' not in p.inventory and 'Pocket Mirror' not in p.inventory and 'Pocket Watch' not in p.inventory:
                        if p.inventory == []:
                            lightGray('> Marius Maximus Baddius III: I cannot see anything in your hands. Could you please get my possessions for me?')
                        else:
                            lightGray('> Marius Maximus Baddius III: Hmm... I don\'t seem to recall any of the items that you\'re holding. Maybe my possessions are somewhere else?')
                else:
                    lightGray('> Marius Maximus Baddius III: Oh... Could you please go and find them for me?')
            else:
                lightGray('> Marius Maximus Baddius III: I can now ascend to a further plane on the next anniversary of my demise.')


def do_action(w: World, p: Player, location: Location, choice: str) -> None:
    """Allows for the player to move in four cardinal directions.
    """
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
    """Defining bolded text."""
    print("\033[1m{}\033[0m\r".format(skk))

def black(skk):
    """Defining a black color for text."""
    print("\033[30m{}\033[0m\r".format(skk))

def darkRed(skk):
    """Defining a dark red color for text."""
    print("\033[31m{}\033[0m\r".format(skk))

def darkGreen(skk):
    """Defining a dark green color for text."""
    print("\033[32m{}\033[0m\r".format(skk))

def darkYellow(skk):
    """Defining a dark yellow color for text."""
    print("\033[33m{}\033[0m\r".format(skk))

def darkBlue(skk):
    """Defining a dark blue color for text."""
    print("\033[34m{}\033[0m\r".format(skk))

def darkMagenta(skk):
    """Defining a dark magenta color for text."""
    print("\033[35m{}\033[0m\r".format(skk))

def darkCyan(skk):
    """Defining a dark cyan color for text."""
    print("\033[36m{}\033[0m\r".format(skk))

def lightGray(skk):
    """Defining a light gray color for text."""
    print("\033[37m{}\033[0m".format(skk))

def darkGray(skk):
    """Defining a dark gray color for text."""
    print("\033[90m{}\033[0m\r".format(skk))

def red(skk):
    """Defining a red color for text."""
    print("\033[1;91m{}\033[0m\r".format(skk))

def green(skk):
    """Defining a green color for text."""
    print("\033[92m{}\033[0m\r".format(skk))

def yellow(skk):
    """Defining a yellow color for text."""
    print("\033[93m{}\033[0m\r".format(skk))

def blue(skk):
    """Defining a blue color for text."""
    print("\033[94m{}\033[0m\r".format(skk))

def magenta(skk):
    """Defining a magenta color for text."""
    print("\033[95m{}\033[0m\r".format(skk))

def cyan(skk):
    """Defining a cyan color for text."""
    print("\033[1;96m{}\033[0m\r".format(skk))

def white(skk):
    """Defining a white color for text."""
    print("\033[1;97m{}\033[0m\r".format(skk))

# bold("This is bold.")
# black("This is black.")
# darkRed("This is dark red.")
# darkGreen("This is dark green.")
# darkYellow("This is dark yellow.")
# darkBlue("This is dark blue.")
# darkMagenta("This is dark magenta.")
# darkCyan("This is dark cyan.")
# lightGray("This is light gray.")
# darkGray("This is dark gray.")
# red("This is red.")
# green("This is green.")
# yellow("This is yellow.")
# blue("This is blue.")
# magenta("This is magenta.")
# cyan("This is cyan.")
# white("This is white.")
# print("\n")


if __name__ == "__main__":
    w = World("map.txt", "locations.txt", "items.txt")
    p = Player(2, 7) # set starting location of player; you may change the x, y coordinates here as appropriate


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
    spelling = pygame.mixer.Sound('spelling.mp3')
    spelling.set_volume(0.2)

    time.sleep(1)
    your_name = input("\033[1;97m\nEnter your name: \033[0m")
    time.sleep(1)
    white(f'\nHello, {your_name}! Welcome to The Amazing Digital Adventure. Type [MENU] to get a list of commands that you can call at any time. You are able to move in all four cardinal directions too, if the location permits.')
    time.sleep(1)


    while not p.victory and not p.quit and moves > 0:
        # print('MOVES: ' + str(moves))
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
                    if visited_negativity_room == False:
                        pygame.mixer.music.load("tadc.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=16)
                        lst = room_of_negativity.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 1
                        p.score -= 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_negativity_room = True
                    else:
                        lightGray("> You try pulling on the door with all your might, but you can\'t seem to open it.")
                        time.sleep(1)
                elif door == '2':
                    if visited_purple_guy == False:
                        pygame.mixer.music.load("fnaf.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=42.8)
                        lst = purple_guy.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 3
                        p.score -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_purple_guy = True
                    else:
                        lightGray("> The second your hand touches the doorknob, flashbacks of your last encounter in this room flood your mind. You barely escaped last time, so why try again?")
                        time.sleep(1)
                elif door == '3':
                    if visited_connor == False:
                        pygame.mixer.music.load("connor.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=64)
                        if connor.puzzle() == True:
                            moves += 5
                            p.score += 5
                        else:
                            moves -= 1
                            p.score -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_connor = True
                    else:
                        lightGray("> You open the door. Connor just shakes his and closes it back.")
                        time.sleep(1)
                elif door == '4':
                    if visited_tiffany == False:
                        pygame.mixer.music.load("sao.mp3")
                        pygame.mixer.music.set_volume(0.05)
                        pygame.mixer.music.play(loops=-1, start=2.5)
                        lst = tiffany.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_tiffany = True
                    else:
                        lightGray("> You peek through the peephole and see that Tiffany is still busy with his chips. You\'d rather not disturb him.")
                        time.sleep(1)
                elif door == '5':
                    if visited_tikki_plagg == False:
                        pygame.mixer.music.load("mlb.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1)
                        if tikki_plagg.puzzle() == True:
                            moves += 3
                            p.score -= 2
                        else:
                            moves -= 1
                            p.score -= 2
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                    else:
                        lightGray("> Plagg and Tikki are probably still at Adrien\'s place because you don't see either of them in the room.")
                        time.sleep(1)
                else:
                    pygame.mixer.Sound.play(spelling)
            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(spelling)


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
                    if visited_bumbly_mia == False:
                        pygame.mixer.music.load("dog.mp3")
                        pygame.mixer.music.set_volume(0.08)
                        pygame.mixer.music.play(loops=-1)
                        lst = bumbly_mia.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 5
                        p.score += 5
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_bumbly_mia = True
                    else:
                        lightGray("> You walk in. Bumbly and Mia are nowhere to be seen.")
                        time.sleep(1)
                elif door == '2':
                    if visited_kyoko_tomoyo_pocoyo == False:
                        pygame.mixer.music.load("cat.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=0.5)
                        lst = kyoko_tomoyo_pocoyo.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves -= 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_kyoko_tomoyo_pocoyo = True
                    else:
                        lightGray("> You walk in. One of the volunteers asks you to leave due to the one visit per person policy.")
                        time.sleep(1)
                elif door == '3':
                    if visited_chirly == False:
                        pygame.mixer.music.load("birdcage.mp3")
                        pygame.mixer.music.set_volume(0.04)
                        pygame.mixer.music.play(loops=-1, start=18.5)
                        lst = chirly.puzzle()
                        for text in lst:
                            lightGray(text)
                            time.sleep(2)
                        moves += 10
                        p.score += 3
                        pygame.mixer.music.load("kahoot.mp3")
                        pygame.mixer.music.set_volume(0.07)
                        pygame.mixer.music.play(loops=-1, start=0.7)
                        visited_chirly = True
                    else:
                        lightGray("> You walk in. The room is empty. Seems like Chirly flew away.")
                        time.sleep(1)
                else:
                    pygame.mixer.Sound.play(spelling)
            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(spelling)


        # PHONE GUY SCP
        if loc == 11:
            white('\nThere is an unknown entity in this location.')
            time.sleep(1)
            selection = input('\033[1;97m\nWould you like to explore? (yes/no) \033[0m')
            time.sleep(1)
            if selection.lower() == 'yes':
                if visited_phone_guy == False:
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
                    lightGray('> The phone suddenly rings again.')
                    time.sleep(2)
                    lightGray('> Phone Guy: Hello? Hello, hello?')
                    time.sleep(2)
                    lightGray(f'> Phone Guy: Oh, it\'s you again, {your_name}.')
                    time.sleep(2)
                    lightGray('> Phone Guy: Now that you gained a basic sense of this game\'s mechanics, would you like to play a game? (yes/no)')
                    time.sleep(2)
                    response = input('\033[1;97m\nYour Answer: \033[0m')

                    if response.lower() == 'yes':
                        pity = 0

                        time.sleep(2)
                        lightGray('> Phone Guy: Uh, welcome to The Amazing Digital Gacha Gambling Game.')

                        time.sleep(2)
                        lightGray('> Phone Guy: You can exit anytime by typing \"leave.\"')

                        time.sleep(2)
                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                        while answer != 'leave':
                            if pity >= 90:
                                chance = random.randint(1, 2)
                                if chance == 1:
                                    moves += 100
                                    p.score += 100
                                    pity = 0
                                else:
                                    moves += 35
                                    p.score += 35
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
                                            lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightGray('> You won 100 moves and 100 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightGray('> You won 35 moves and 35 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    elif 26 <= rand <= 50:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightGray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightGray('> You won 5 moves and 5 points!')
                                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightGray('> You lost 1 move and won 1 point.')
                                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
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
                                                lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightGray('> You won 100 moves and 100 points!')
                                                lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                                answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightGray('> You won 35 moves and 35 points!')
                                                lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                                answer = input('\033[1;97m\nYour Answer: \033[0m')

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightGray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightGray('> You won 5 moves and 5 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightGray('> You lost 1 move and won 1 point.')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                
                                else:
                                    pygame.mixer.Sound.play(spelling)

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
                                            lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightGray('> You won 100 moves and 100 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightGray('> You won 35 moves and 35 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    elif 4 <= rand <= 28:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightGray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightGray('> You won 5 moves and 5 points!')
                                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightGray('> You lost 1 move and won 1 point.')
                                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
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
                                                lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightGray('> You won 100 moves and 100 points!')
                                                lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                                answer = input('\033[1;97m\nYour Answer: \033[0m')
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightGray('> You won 35 moves and 35 points!')
                                                lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                                answer = input('\033[1;97m\nYour Answer: \033[0m')

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightGray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightGray('> You won 5 moves and 5 points!')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightGray('> You lost 1 move and won 1 point.')
                                            lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                                            answer = input('\033[1;97m\nYour Answer: \033[0m')
                                
                                else:
                                    pygame.mixer.Sound.play(spelling)

                        time.sleep(2)
                        lightGray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')
                    
                    elif response.lower() == 'no':
                        time.sleep(2)
                        lightGray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    else:
                        pygame.mixer.Sound.play(spelling)

                    pygame.mixer.music.load("kahoot.mp3")
                    pygame.mixer.music.set_volume(0.07)
                    pygame.mixer.music.play(loops=-1, start=0.7)
                    visited_phone_guy = True

                else:
                    pygame.mixer.music.load("fnaf.mp3")
                    pygame.mixer.music.set_volume(0.04)
                    pygame.mixer.music.play(loops=-1, start=0)

                    lightGray('> You notice a mysterious blue telephone on the ground.')
                    time.sleep(2)
                    lightGray('> The phone suddenly starts ringing.')
                    time.sleep(2)
                    lightGray('> Phone Guy: Hello, hello, hello?')
                    time.sleep(2)
                    lightGray(f'> Phone Guy: Oh, it\'s you again, {your_name}.')
                    time.sleep(2)
                    lightGray('> Phone Guy: Now that you gained a basic sense of this game\'s mechanics, would you like to play a game?')
                    time.sleep(2)
                    response = input('\033[1;97m\nYour Answer: \033[0m')

                    if response.lower() == 'yes':
                        pity = 0

                        time.sleep(2)
                        lightGray('> Phone Guy: Uh, welcome to The Amazing Digital Gacha Gambling Game.')

                        time.sleep(2)
                        lightGray('> Phone Guy: You can exit anytime by typing \"leave.\"')

                        time.sleep(2)
                        lightGray('> Phone Guy: Do you want to make a single pull or a ten pull? (1 or 10)')
                        answer = input('\033[1;97m\nYour Answer: \033[0m')

                        while answer != 'leave':
                            if pity >= 90:
                                chance = random.randint(1, 2)

                                if chance == 1:
                                    moves += 100
                                    p.score += 100
                                    pity = 0
                                else:
                                    moves += 35
                                    p.score += 35
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
                                            lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightGray('> You won 100 moves and 100 points!')
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightGray('> You won 35 moves and 35 points!')

                                    elif 26 <= rand <= 50:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightGray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightGray('> You won 5 moves and 5 points!')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightGray('> You lost 1 move and won 1 point.')

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
                                                lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightGray('> You won 100 moves and 100 points!')
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightGray('> You won 35 moves and 35 points!')

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightGray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightGray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightGray('> You lost 1 move and won 1 point.')
                                
                                else:
                                    pygame.mixer.Sound.play(spelling)

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
                                            lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                            time.sleep(2)
                                            lightGray('> You won 100 moves and 100 points!')
                                        else:
                                            moves += 35
                                            p.score += 35
                                            time.sleep(2)
                                            lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                            time.sleep(2)
                                            lightGray('> You won 35 moves and 35 points!')

                                    elif 4 <= rand <= 28:
                                        moves += 5
                                        p.score += 5
                                        time.sleep(2)
                                        lightGray('> Phone Guy: Oh, uh look, you got something!')
                                        time.sleep(2)
                                        lightGray('> You won 5 moves and 5 points!')

                                    else:
                                        moves -= 1
                                        p.score += 1
                                        time.sleep(2)
                                        lightGray('> You lost 1 move and won 1 point.')

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
                                                lightGray('> Phone Guy: Congrats, you won the 50/50.')
                                                time.sleep(2)
                                                lightGray('> You won 100 moves and 100 points!')
                                            else:
                                                moves += 35
                                                p.score += 35
                                                time.sleep(2)
                                                lightGray('> Phone Guy: It seems that you have lost the 50/50, oh well...')
                                                time.sleep(2)
                                                lightGray('> You won 35 moves and 35 points!')

                                        elif 4 <= rand <= 28:
                                            moves += 5
                                            p.score += 5
                                            time.sleep(2)
                                            lightGray('> Phone Guy: Oh, uh look, you got something!')
                                            time.sleep(2)
                                            lightGray('> You won 5 moves and 5 points!')

                                        else:
                                            moves -= 1
                                            p.score += 1
                                            time.sleep(2)
                                            lightGray('> You lost 1 move and won 1 point.')

                                else:
                                    pygame.mixer.Sound.play(spelling)

                        time.sleep(2)
                        lightGray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    elif response.lower() == 'no':
                        time.sleep(2)
                        lightGray('> Phone Guy: Um... okay, I\'ll leave you to it. See you on the flip side!')

                    else:
                        pygame.mixer.Sound.play(spelling)

                    pygame.mixer.music.load("kahoot.mp3")
                    pygame.mixer.music.set_volume(0.07)
                    pygame.mixer.music.play(loops=-1, start=0.7)

            elif selection.lower() != 'no':
                pygame.mixer.Sound.play(spelling)


        # DISPLAY OPTIONS
        time.sleep(1)
        white("\nWhat to do?")
        time.sleep(1)
        green("- [MENU]")
        green("- North\n- South\n- West\n- East")
        time.sleep(1)
        choice = input("\033[1;97m\nEnter Action: \033[0m")


        # MENU
        if choice.lower() == "[menu]":
            white("\nWhat to do?")
            time.sleep(1)
            for option in menu:
                green("- " + option.title())
            choice = input("\033[1;97m\nChoose Action: \033[0m")
        

        # CARDINAL DIRECTIONS
        if choice.lower() == "north" or choice.lower() == "south" or choice.lower() == "east" or choice.lower() == "west":
            do_action(w, p, location, choice.lower())
        

        # LOOK
        if choice.lower() == "look":
            lightGray(location.long + '\n')
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

            if (w.items != [] and all([item.curr_position == -1 for item in w.items])) or curr_items == []:
                lightGray("There are no items in this area!\n")
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
                    pygame.mixer.Sound.play(spelling)
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
                    pygame.mixer.Sound.play(spelling)
                    lightGray("You don't have this item.")
                    time.sleep(1)
       

        # TALK
        if choice.lower() == 'talk':
            if loc == 5:
                pygame.mixer.music.load("getaway.mp3")
                pygame.mixer.music.set_volume(0.06)
                pygame.mixer.music.play(loops=-1, start=3)
                if visited_linda == False:
                    moves += 2
                    p.score += 5
                lst = linda_shinx.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 6:
                pygame.mixer.music.load("jojo.mp3")
                pygame.mixer.music.set_volume(0.06)
                pygame.mixer.music.play(loops=-1)
                marius_maximus_baddius_iii.dialogue()
                if marius_moves_gained == True:
                    moves += 15
                    marius_moves_gained = False
                if found_pocket_watch == True:
                    p.inventory.remove('Pocket Watch')
                    found_pocket_watch = False
                if found_pocket_mirror == True:
                    p.inventory.remove('Pocket Mirror')
                    found_pocket_mirror = False
                if found_handkerchief == True:
                    p.inventory.remove('Handkerchief')
                    found_handkerchief = False
                if found_items == True and visited_marius_maximus_baddius_iii == True and marius_end_gained == True:
                    moves += 10
                    p.score += 50
                    marius_end_gained = False

                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 9:
                pygame.mixer.music.load("whistle.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.5)
                if visited_tommy == False:
                    moves += 2
                    p.score += 9
                lst = tommy_grieves.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 15:
                pygame.mixer.music.load("tangled.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.5)
                if visited_sadie == False:
                    moves += 2
                    p.score += 15
                lst = sadie_shaymin.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            elif loc == 16:
                pygame.mixer.music.load("renai.mp3")
                pygame.mixer.music.set_volume(0.04)
                pygame.mixer.music.play(loops=-1, start=0.7)
                if visited_davis == False:
                    moves += 2
                    p.score += 16
                lst = davis_loo.dialogue()
                for text in lst:
                    lightGray(text)
                    time.sleep(2)
                pygame.mixer.music.load("kahoot.mp3")
                pygame.mixer.music.set_volume(0.07)
                pygame.mixer.music.play(loops=-1, start=0.7)

            else:
                lightGray("There is no one to talk to here.")
                time.sleep(1)


        # MISSPELLING
        if choice.lower() not in ['north', 'south', 'east', 'west', '[menu]', 'look', 'inventory', 'score', 'quit', 'grab', 'drop', 'talk', 'quit', 'cheat sheet', 'lucky pen', 'tcard', 'water bottle', 'pocket watch', 'handkerchief', 'pocket mirror']:
            pygame.mixer.Sound.play(spelling)


        # UPDATE MOVES COUNTER
        if choice.lower() in ['north', 'south', 'east', 'west', 'grab', 'drop']:
            moves -= 1


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
    if moves <= 0:
        red("\n\nYou've reached the maximum number of moves. Game over!")
        time.sleep(1)
        magenta("\nYour final score is: " + str(p.score) + "\n")
        time.sleep(1)