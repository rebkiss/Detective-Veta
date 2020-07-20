define v = Character("Veta")
define q = Character("Quain")
define r = Character("Receptionist")
image quainflip = im.Flip("quaindefault1.png", horizontal = True )
image black = "#000"
define m = Character("Mariatu")
define unknown = Character("????")
define fade = Fade(0.5, 0.0, 0.5)
define ms = Character("Ms. Millie")
define e = Character("Ellis")
define p = Character("Seller")
define a = Character("Aimon")


image vetadefault:
    "vetadefault1.png"
    pause 1
    "vetadefault2.png"
    pause 0.5
    repeat

image quaindefault:
    "quaindefault1.png"
    pause 2
    "quaindefault2.png"
    pause 0.5
    repeat

#bag
default profile_highlights = False
default journal_highlights = False
default mysteries_highlights = False
default items_highlights = False

#profiles
default profile_veta = False
default profile_quain = False

#flags
define storypoints = 1
define ptalk = 1
define etalk = 1

default backpack = Container()

$ inventory = Item('Student ID') ### example

init python:

    #inventory stuff
    class Item(object):
        def __init__(self, name):
            self.name = name

    class InvItem(object):
        def __init__(self, item, amount):
            self.item = item
            self.amount = amount

    class Container(object):
        def __init__(self):
            self.inventory = []

        def add_item(self, item, amount=1):
            self.inventory.append(InvItem(item, amount))

        def has_item(self, item, amount=1):
            if item in [i.item for i in self.inventory]:
                if self.find_item(item).amount >= amount:
                    return(self.find_item(item).amount)
                else:
                    return(False)
            else:
                return(False)
            
        def find_item(self, item):
            return(self.inventory[[i.item for i in self.inventory].index(item)])

        def remove_item(self, item, amount=1):
            if self.has_item(item):
                self.find_item(item).amount -= amount
                if self.find_item(item).amount <= 0:
                    self.inventory.pop(self.inventory.index(self.find_item(item)))
                    return('gone')
                else:
                    return('more left')
            else:
                return('not found')
    
    paper = Item('paper')


 ## Attempt to make a party system so investigation varies depending on party members
    class Person(object):
        def __init__(self, name):
            self.name = name

    class Group(object):
        def __init__(self, member):
            self.member = member
    
    class Party(object):
        def __init__(self, party):
            self.party = []

        def add_member(self, member, amount=1):
            self.party.append(Party(name, member))

        def has_member(self, member, amount=1):
            if member in [i.member for i in self.party]:
                if self.find_member(member).amount >= amount:
                    return(self.find_member(member).amount)
                else:
                    return(False)
            else:
                return(False)
       
        def find_member(self, member):
            return(self.party[[i.member for i in self.party].index(member)])

        def remove_member(self, member, amount=1):
            if self.has_member(member):
                self.find_member(member).amount -= amount
                if self.find_member(member).amount <= 0:
                    self.party.pop(self.party.index(self.find_member(member)))
                    return('gone')
                else:
                    return('more left')
            else:
                return('not found')



# game starts here
label start:

    label prologue:

        scene black with fade

        scene caravan with fade

        "We arrived at the Oasis of Destiny long after sunset."
        "Our field trip began before sunrise at the school, and now we're in the middle of the desert."
        "This trip is like a rite of passage for us, every student at our school goes on a field trip here before graduating."

        v "*stretching* Hnnnnngh...My legs are sore from sitting in the caravan all day."
        q "Well, we're here at last. The oasis is quite beautiful."
        v "We should definitely check it out tomorrow."
        q "I don't remember agreeing to spending this field trip trailing after you."
        v "Oh, come on! Don't be like that. You know things are more interesting when I'm around."
        q "*snort*"

        scene black with fade

        unknown "Oh, there you two are!"

        scene arriving with fade
        ms "I have both of your room keys over here."
        v "Thank you, Ms. Millie."
        q "I'm going to my room."
        v "Which room are you in? I'm in 110."
        q "111."
        v "Cool, let's walk together then."

        scene black with fade

        "At the time, I didn't realize that would be the last time I talked to Ms. Millie."

        scene hotelhallway with fade

        
        show vetadefault1 at right
        show quainflip:
            xalign 0.7

        v "Oh, here's my room."
        unknown "WHERE IS IT?"
        v "Um..."

        show mariatusad at left

        m "Oh, I'm sorry! I didn't realize you were there."
        q "Is something the matter, Mariatu?"
        v "Wait, let me guess. You lost your room key?"
        m "*sniffle* Yes, I lost it. I just got it a moment ago!"
        v "Lucky for you, we're in the same suite, so I have a key. Did you drop it somewhere?"
        m "I'm not sure. When I got my key, I had put it straight into my bag. But now I can't find it!"
        q "So it didn't fall out?"
        m "*sniffle* No!"
        v "...Well, tell you what. Quain and I will go look for it while you stay with one of our other classmates in the mean time."
        m "Are you sure?"
        v "Quain?"
        q "Leave the mystery solving to us."

        show mariatuhappy at left
        hide mariatusad

        m "Of course, you guys are the experts!"
        jump chapterone


    label chapterone:

        scene chapter1 with fade
        $ renpy.pause(delay=5,hard=False)

        scene hotelroom with fade
        show vetadefault at right
        show quaindefault at left

        v "Well, Mariatu is staying with another student, so we can start our investigation now."
        q "Let's start with finding Mariatu's lost room key. It has to be somewhere in this hotel."
        v "Sounds like a plan! I'll bring my bag along, too! It has some useful stuff and we can put the
        things we find in here."
        q "I have this map here that we can use to travel to different places."
        v "Let's get this investigation started!"
        $ storypoints += 1

        call screen hotelroom with fade

    label hotelroomlow:

        scene hotelroom 

        if storypoints == 7:
            jump newkey 

        call screen hotelroom with fade

    screen hotelroom():

        tag location

        imagemap:

            idle "hotelroombuttons.png"

            #outside
            hotspot (1114, 240, 549, 408) action Jump("roomoutside")

            #bed
            hotspot (180, 701, 1140, 293) action Jump("bed")

            #painting
            hotspot (219, 190, 435, 303) action Jump("roompainting")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transition = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("hotelroommovelow")

    label roomoutside:

        scene hotelroom 

        v "Wow, the sand outside looks like it's blue!"
        q "I'm more concerned with the fact that the window doesn't have curtains or blinds."
        v "Ms. Millie did say that the school booked a cheap hotel."
        q "A hotel so cheap that they can't afford curtains."
        v "At least the view is beautiful."
        q "I suppose."

        call screen hotelroom 

    label bed:

        scene hotelroom 

        v "*lays on bed* These beds are really comfy!"
        q "They certainly are."
        v "This comforter matches my clothes, too!"
        q "Indeed, you blend right in. I almost forgot you were here. Almost."
        v "Wow, the betrayal. I thought we were friends, detective partners."
        q "Well, I agree that we are partners. Not so sure about friends."
        v "Hmph."

        call screen hotelroom

    label roompainting:

        scene hotelroom 

        v "It's a cactus."
        q "Thank you for pointing out the obvious."
        v "You're welcome."

        call screen hotelroom 

    label newkey:

        scene hotelroom with fade

        show mariatusad at left
        show vetadefault1 at right
        show quainflip:
                xalign 0.7

        m "Oh, you're back! Did you manage to find my key?"
        v "No, but we were able to get you a spare key."
        q "Make sure you don't lose it."
        m "Thank you! Thank you! I'll be sure to take extra care of this one!"
        q "Well, I think it's time to turn in for the night. We have to meet up with the rest of the class in the morning."
        v "Alright then."
        hide quainflip

        m "I'm going to let Ms. Millie know about my key. I'd rather get a scolding now than first thing in the morning."
        v "Well, you have a key now, so you can get back into the room. I'm going to bed."
        m "Goodnight!"

        $ storypoints += 1

        scene black with fade

        jump morning

    label morning:

        scene black with fade
        scene hotelroomday with fade

        "The next morning"
        v "Nnnnnnehhhh...."
        v "What's that noise...?"

        show mariatuhappy at left
        show vetadefault1 at right

        v "What's going on?"
        show mariatusad
        hide mariatuhappy
        m "I'm not sure, but there's a crowd of people down by the oasis."
        v "It's too noisy to go back to sleep, so let's check it out."
        m "Oh! I don't remember how to get there."
        v "It's easy, just look at the map!"

        $ storypoints += 1

        call screen hotelroomday

    label hotelroommovelow:

        scene hotelroom

        call screen hotelroommove

    screen hotelroommove():

        imagemap:

            idle "hotelroomarrow.png"

            #arrow
            hotspot (18, 570, 129, 94) action Call("hotelhallwaylow")

            #back
            hotspot (18, 952, 105, 72) action Call("hotelroomlow")

    label hotelhallwaylow:

        scene hotelhallway with fade

        call screen hotelhallway

    screen hotelhallway():

        tag location

        imagemap:

            idle "hotelhallwaybuttons.png"

            #room
            hotspot (970, 177, 297, 596) action Jump("room")

            #door
            hotspot (243, 131, 144, 372) action Jump("hallwaydoor")

            #window
            hotspot (5, 94, 101, 112) action Jump("hallwaywindow")

            #light1
            hotspot (519, 164, 82, 88) action Jump("hallwaylight")

            #light2
            hotspot (737, 191, 109, 112) action Jump("hallwaylight")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transition = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("hotelhallwaymovelow")

            if storypoints == 4:
                imagebutton auto "recepidcard.png" xalign 0.5 yalign 0.5 action Jump("receptidcard")


    label room:

        scene hotelhallway

        v "That's my room!"
        q "We can always take a break if you want."
        v "I think it's you who needs a break."

        call screen hotelhallway 

    label hallwaydoor:

        scene hotelhallway with fade

        show vetadefault at right
        show quaindefault at left

        q "This doesn't look like a regular guest room."
        v "It could be for employees only."
        q "There's no sign that says that. Just the room number."
        v "It's locked. Someone doesn't want just anyone in there."
        q "It could be a supply room."
        v "I guess we'll leave it at that."

        $ storypoints += 1

        call screen hotelhallway with fade

    label hallwaywindow:

        scene hotelhallway

        v "I can't see!"
        q "I can see just fine."
        v "That's because you're tall."

        call screen hotelhallway 

    label hallwaylight:

        scene hotelhallway

        v "These lights are very aesthetic."
        q "They certainly set the mood."

        call screen hotelhallway 

    label receptidcard:

        scene hotelhallway with fade

        show vetadefault at right
        show quaindefault at left

        v "There's something stuck under the door!"
        q "It's a card. This looks like the receptionist's ID card."
        v "I could've sworn there wasn't anything there the last time we checked though."
        q "Maybe the receptionist dropped it here when she was heading to the lobby? This could be an unmarked employee room."
        v "I guess so. Or maybe whoever stole her card dropped it here?"
        q "Perhaps. Right now we should return the card though."
        "Receptionist ID Card added to the bag!"

        $ backpack.add_item(recepidcard)

        $ storypoints += 1

        call screen hotelhallway with fade

    label hotelhallwaymovelow:

        scene hotelhallway

        call screen hotelhallwaymove

    screen hotelhallwaymove():

        imagemap:

            idle "hotelhallwayarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Jump("hotelhallwaylow")

            #arrow1
            hotspot (490, 441, 105, 83) action Jump("hotellobbylow")

            #arrow2
            hotspot (1063, 576, 95, 96) action Jump("hotelroomlow")

    label hotellobbylow:

        scene hotelobby with fade

        if storypoints >= 3:
            jump hotellobbyreceplow

        else:
            jump hotellobbymid

    label hotellobbymid:

        scene hotelobby with fade
        call screen hotellobby

    screen hotellobby():

        tag location

        imagemap:

            idle "hotelobbybuttons.png"

            #chandelier
            hotspot (1333, 9, 325, 225) action Jump("chandelier")

            #painting
            hotspot (978, 58, 343, 202) action Jump("lobbypainting")

            #desk
            hotspot (978, 58, 343, 202) action Jump("desk")

            #couch
            hotspot (929, 333, 563, 278) action Jump("couch")

            #carpet
            hotspot (601, 803, 1128, 271) action ("carpet")

            #floor
            hotspot (563, 645, 1336, 123) action Jump("floor")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Call("hotellobbymovelow")


    label chandelier:

        scene hotelobby

        v "It's so pretty!"
        q "Don't stare at it for too lo-{nw}"
        v "MY EYES!!"
        q "I WARNED YOU!"
        v "I've gone blind. Quain, please be my eyes."
        q "I can't believe this."

        call screen hotellobby  

    label lobbypainting:

        scene hotelobby

        v "It's a nice painting of sand."
        q "There's sand a few feet away though..."
        v "Maybe some people forget that they're in the middle of the desert."
        q "What kind of person forgets that they're in the desert?"
        v "Mariatu."
        q "...I can't argue with that."

        call screen hotellobby

    label desk:

        scene hotelobby

        q "There's no receptionist."
        v "Maybe they're on break?"

        call screen hotellobby 

    label couch:

        scene hotelobby

        v "This is a comfy couch."
        q "Isn't it called a sofa?"
        v "Pretty sure it's a couch."
        q "A couch doesn't have armrests."
        v "Says who?"
        q "Says the people who make them."
        v "Oh really? And who told you that?"
        q "One of the furniture sellers back home."
        v "Hmm...I still think it's a couch."
        q "*facepalm*"

        call screen hotellobby  

    label carpet:

        scene hotelobby

        q "This is a nice carpet."
        v "Too bad it has some sand on it."

        call screen hotellobby  

    label floor:

        scene hotelobby

        q "The marble floors are certainly eye-catching."
        v "It's so shiny. I'm surprised there isn't sand on it."
        q "Someone's gotta be cleaning it."

        call screen hotellobby 

    label hotellobbyreceplow:

        scene hotelobbyrecep
        
        call screen hotellobbyrecep

    screen hotellobbyrecep():

        tag location

        imagemap:

            idle "hotelobbyrecep.png"

            #chandelier
            hotspot (1333, 9, 325, 225) action Jump("chandeliertwo")

            #painting
            hotspot (978, 58, 343, 202) action Jump("lobbypaintingtwo")

            #recep
            hotspot (33, 233, 229, 277) action Jump("recep")

            #couch
            hotspot (929, 333, 563, 278) action Jump("couchtwo")

            #carpet
            hotspot (601, 803, 1128, 271) action Jump("carpettwo")

            #floor
            hotspot (563, 645, 1336, 123) action Jump("floortwo")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Call("hotellobbymovelow")


    label chandeliertwo:

        scene hotelobby

        v "It's so pretty!"
        q "Don't stare at it for too lo-{nw}"
        v "MY EYES!!"
        q "I WARNED YOU!"
        v "I've gone blind. Quain, please be my eyes."
        q "I can't believe this."

        call screen hotellobbyrecep  

    label lobbypaintingtwo:

        scene hotelobby

        v "It's a nice painting of sand."
        q "There's sand a few feet away though..."
        v "Maybe some people forget that they're in the middle of the desert."
        q "What kind of person forgets that they're in the desert?"
        v "Mariatu."
        q "...I can't argue with that."

        call screen hotellobbyrecep

    label couchtwo:

        scene hotelobby

        v "This is a comfy couch."
        q "Isn't it called a sofa?"
        v "Pretty sure it's a couch."
        q "A couch doesn't have armrests."
        v "Says who?"
        q "Says the people who make them."
        v "Oh really? And who told you that?"
        q "One of the furniture sellers back home."
        v "Hmm...I still think it's a couch."
        q "*facepalm*"

        call screen hotellobbyrecep  

    label carpettwo:

        scene hotelobby

        q "This is a nice carpet."
        v "Too bad it has some sand on it."

        call screen hotellobbyrecep  

    label floortwo:

        scene hotelobby

        q "The marble floors are certainly eye-catching."
        v "It's so shiny. I'm surprised there isn't sand on it."
        q "Someone's gotta be cleaning it."

        call screen hotellobbyrecep  

    label recep:

        if storypoints >= 3:

            scene hotelobby with fade

            show receptionistupset at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            r "Good evening! How may I help you?"
            q "Is everything alright, ma'am?"
            r "Frankly, no. My boss is going to chew me out for sure."
            v "What's wrong?"
            r "I lost my ID card somehow! It was in my purse before I changed into my uniform, but it was gone when I checked afterwards."
            v "Quain, we should help her."
            q "I see no harm in searching for her ID. She seems too distraught to help us with the key anyway."
            v "We'll help you look for your ID!"
            show receptionisthappy at left
            r "Really?! Thank you so much!"

            scene hotelobby with fade

            show vetadefault at right
            show quaindefault at left

            v "I wonder where her ID is? Did we pass by an employee only door in the hallway?"
            q "No, but we did pass by a suspicious door..."

            $ storypoints += 1

            call screen hotellobbyrecep with fade 

        elif storypoints >= 4:

            scene hotelobby with fade

            show receptionistupset at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            r "I hope you can find my ID card..."

            call screen hotellobbyrecep with fade

        elif storypoints >= 5:

            scene hotelobby with fade

            show receptionistupset at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7
            
            r "How is the search going?"
            q "Good news, we found it in the hallway."
            "Receptionist ID Card handed over!"
            show receptionisthappy
            r "Oh, thank you so much! You don't know how much this means to me. If you need any help, please let me know!"

            scene hotelobby with fade

            show vetadefault at right
            show quaindefault at left

            v "Now that she's not worrying about her card, we can ask her about the key."
            q "Maybe we can ask about the door as well."

            $ storypoints += 1

            call screen hotellobbyrecep

        elif storypoints >= 6:
            jump recepdiscussion

    label recepdiscussion:
         
        scene hotelobby with fade

        show receptionisthappy at left
        show vetadefault1 at right
        show quainflip:
            xalign 0.7

        r "How can I help you?"
        menu: 
                "Mariatu's Key" if storypoints >= 6:
                    v "My friend lost her room key and we haven't found it yet. Has anyone brought it here?"
                    r "Hmm, I just started my shift, but let me see if there's anything here on the desk. Room number?"
                    v "110."
                    show receptionistupset
                    hide receptionisthappy
                    r "...Sorry, I don't have it. We do keep spare keys, but they're under lock and key. Wait right here, I'll get it from the back!"
                    hide receptionistupset with fade
                    v "Well that's unfortunate."
                    q "At least there's a spare key. We've searched everywhere for the key in the hotel."
                    v "I'm starting to think that the key didn't just fall out of her bag."
                    q "No, this is looking less like an accident."
                    show receptionisthappy at left with fade
                    r "Here's one of the spare keys! Be sure to not lose it!"
                    $ backpack.add_item(sparekey)
                    "Spare key added to the bag!"
                    jump recepdiscussion
                
                "Suspicious Door":
                    q "We noticed the door down the hallway. It's not marked for employees, but it's far too small to be a suite."
                    r "Hmm, I'm not really sure what that door is for. I actually just started working here less than a week ago."
                    q "Your ID card was stuck under the door. I'm assuming you've never opened that door before?"
                    r "That's correct. I've never been down that hallway before. The employee rooms are down this hallway behind me."
                    q "I see."
                    jump recepdiscussion

                "New Job":
                    v "So you're new to the job?"
                    r "Yes! I've lived here all my life in the outskirts of the town. The hotel was hiring and I took the opportunity for better pay."
                    q "Where were you working before?"
                    r "I was working in the market for one of the pottery sellers. It was hard work and the pay wasn't worth it."
                    jump recepdiscussion
                "Goodbye":
                    jump hotellobbylow


    label hotellobbymovelow:

        scene hotellobby

        call screen hotellobbymove

    screen hotellobbymove():

        imagemap:

            idle "hotelobbyarrow.png"

            #arrow
            hotspot (532, 490, 103, 100) action Call("hotelhallwaylow")

            #back
            hotspot (18, 952, 105, 72) action Call("hotellobbylow")

    screen bag():

        tag bagmenu

        modal True

        imagemap:

            ground "bagmenu.png"

            #back button
            hotspot (53, 934, 134, 99) action Hide("bag", transition = fade)

            #profiles
            hotspot (515, 522, 195, 117):
                action Show("profiles")
                hovered SetVariable("profile_highlights", True)
                unhovered SetVariable("profile_highlights", False)
                if profile_highlights:
                    add "profileshover.png" xalign 0.3 yalign 0.54

            #journal
            hotspot (500, 682, 236, 168):
                action Show("journal")
                hovered SetVariable("journal_highlights", True)
                unhovered SetVariable("journal_highlights", False)
                if journal_highlights:
                    add "journalhover.png" xalign 0.3 yalign 0.76

            #mysteries
            hotspot (836, 662, 73, 175):
                action Show("mysteries")
                hovered SetVariable("mysteries_highlights", True)
                unhovered SetVariable("mysteries_highlights", False)
                if mysteries_highlights:
                    add "mysterieshover.png" xalign 0.45 yalign 0.74

            #items
            hotspot (743, 341, 87, 280):
                action Show("items")
                hovered SetVariable("items_highlights", True)
                unhovered SetVariable("items_highlights", False)
                if items_highlights:
                    add "itemshover.png" xalign 0.41 yalign 0.42

    screen profiles():

        modal True

        if storypoints >= 1:
            imagemap:

                idle "profilespageone.png"

                #back button
                hotspot (53, 934, 134, 99): 
                    action Hide("bag", transition = fade), Hide("profiles", transition = fade)

                #bag
                hotspot (73, 404, 158, 221) action Hide("profiles")    

                #veta
                hotspot (446, 530, 106, 99):
                    action NullAction()
                    hovered SetVariable("profile_veta", True)
                    unhovered SetVariable("profile_veta", False)
                    if profile_veta:
                        add "profilesvetahover.png" xalign 0.25 yalign 0.541

                #quain
                hotspot (561, 530, 107, 98):
                    action NullAction()
                    hovered SetVariable("profile_quain", True)
                    unhovered SetVariable("profile_quain", False) 
                    if profile_quain:
                        add "profilesquainhover.png" xalign 0.3 yalign 0.54           


    screen journal():

        modal True

        imagemap:

            idle "journalpageone.png"

            #back button
            hotspot (53, 934, 134, 99):
                action Hide("bag", transition = fade), Hide("journal", transition = fade), Hide("journalentry")

            #bag
            hotspot (73, 404, 158, 221) action Hide("journal"), Hide("journalentry") 

            if storypoints >= 2: 
                textbutton "The Missing Door Key" action Show("TheMissingDoorKey") xalign 0.3 yalign 0.3 
                

            if storypoints >= 3:
                textbutton "The Suspicious Door" action Show("TheSuspiciousDoor") xalign 0.3 yalign 0.4 

            if storypoints >= 4:
                textbutton "Missing ID" action Show("MissingID") xalign 0.3 yalign 0.5



    screen TheMissingDoorKey():

        tag journalentry

        vbox:

            area (990, 292, 502, 495)

            text "We've finally arrived at the Oasis of Destiny, hidden deep in the Avius Desert. Unfortunately, my friend, Mariatu, seems to have lost her room key and is unable to find it. Quain, my partner in mystery solving, has agreed to help me find her key."

    screen TheSuspiciousDoor():

        tag journalentry

        vbox:

            area (990, 292, 502, 495)

            text "While investigating the hallway, we came across a door at the end of the hallway. It's too small to be a suite, and it doesn't have any signs on it besides the room number. We've decided it's a supply room, but I still have a feeling it's something more than that."

    screen MissingID():

        tag journalentry

        vbox:

            area (990, 292, 502, 495)

            text "We found the receptionist in the lobby, but she was too upset with her missing ID to be of much help to us. We decided to help her look for it. While we didn't pass by any doors marked for employees, we did pass by a suspicious door earlier..."

    screen FoundID():

        tag journalentry

        vbox:
            area (990, 292, 502, 495)

            text "We went back to the hallway where the suspicious door was and found the ID card just under the door. Quain thinks that the door is an unmarked employee room, but I have a feeling it's more than that. For now, we should return the ID card."

    screen mysteries():

        modal True
        
        if storypoints >= 2:

            imagemap:

                idle "mysterypageone.png"

                #back button
                hotspot (53, 934, 134, 99): 
                    action Hide("bag", transition = fade), Hide("mysteries", transition = fade), Hide("MissingKey")

                #bag
                hotspot (73, 404, 158, 221) action Hide("mysteries"), Hide("MissingKey")

                if storypoints >= 2:
                    hotspot (446, 527, 109, 210) action Show("MissingKey")

    screen MissingKey():

        tag mystery

        vbox:

            area (447, 263, 1010, 244) 

            text "My friend, Mariatu, lost her room key sometime between when Ms. Millie gave her the key and when we got to our room. Mariatu is very forgetful, but I have a feeling she didn't just drop it somewhere."



    screen items():

        modal True

        imagemap:

            idle "itemspageone.png"

            #back button
            hotspot (53, 934, 134, 99): 
                action Hide("bag", transition = fade), Hide("items", transition = fade)

            #bag
            hotspot (73, 404, 158, 221) action Hide("items")

            if backpack.has_item(recepidcard):
                textbutton "Receptionist ID Card" action Show("Receptidcard") xalign 0.3 yalign 0.3

            if backpack.has_item(necklace):
                textbutton "Necklace" action Show("Necklace") xalign 0.3 yalign 0.3
 

    screen sketchmap():

        modal True

        imagemap:

            idle "MapConcept.jpg"

            #oasis
            if storypoints >= 9:
                hotspot (714, 298, 488, 390) action Call("oasissouthernlow") 
            
            #hotel
            if storypoints >= 9:
                hotspot (479, 203, 212, 294) action Call("hotellobbydaylow")

            if storypoints <= 8:
                hotspot (479, 203, 212, 294) action Call("hotellobbylow")

            #market
            if storypoints >= 12:
                hotspot (1291, 236, 171, 232) action Call("marketlow")
            
            #back
            hotspot (1707, 924, 138, 119) action Hide("sketchmap", transition = dissolve)

    label oasiseasternlow:

        scene oasiseastern

        call screen oasiseastern
    
    screen oasiseastern():

        tag location

        imagemap:

            idle "oasiseasternbuttons.png"

            #water
            hotspot (9, 536, 689, 311) action Jump("eastwater")

            #tree
            hotspot (799, 109, 578, 781) action Jump("easttree")

            #building
            hotspot (1609, 1, 304, 869) action Jump("eastbuilding")

            #tents
            hotspot (1479, 384, 122, 294) action Jump("easttents")

            #far buildings
            hotspot (19, 410, 444, 100) action Jump("eastfar")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("oasiseasternmovelow")

    label oasiseasternmovelow:

        scene oasiseastern

        call screen oasiseasternmove

    screen oasiseasternmove():

        imagemap:

            idle "oasiseasternarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Jump("oasiseasternlow")

            #arrow
            hotspot (43, 461, 110, 98) action Jump("oasissouthernlow")

    label eastwater:

        scene oasiseastern

        v "I bet the water is nice and cold right now."
        q "You can't swim in there. It's frozen."
        v "I'm not. I can't even swim."
        q "Good thing it's frozen then."

        call screen oasiseastern

    label easttree:

        scene oasiseastern

        v "Look at these palm trees! There's so much shade under here."
        q "...Did you forget to put on sunscreen?"
        v "No..."

        call screen oasiseastern

    label eastbuilding:

        scene oasiseastern

        q "This looks like another hotel."
        v "Seems much smaller than our hotel though, and our hotel is cheap."
        q "Maybe it's for the rich?"
        v "Or maybe they have conference rooms, like for meetings or parties."
        q "That's a good guess."

        call screen oasiseastern

    label easttents:

        scene oasiseastern

        q "That must be where the market is."
        v "It's certainly colorful. Definitely catches the eye."
        q "Once they catch your eye, they go after your money next."
        v "People need to make a living here you know."
        q "I didn't say it was a bad thing."

        call screen oasiseastern

    label eastfar:

        scene oasiseastern

        q "The western part of the oasis seems to have a lot more buildings than over here."
        v "I think I can see our hotel over there."
        q "How I long for my bed..."

        call screen oasiseastern

    label oasissouthernlow:

        scene oasissouthern

        if storypoints == 9:

            jump milliedeath

        else:

            call screen oasissouthern
    
    screen oasissouthern():

        tag location

        imagemap:

            idle "oasissouthernbuttons.png"

            #crime scene
            hotspot (976, 493, 429, 180) action Jump("crimescene")

            #frozen water
            hotspot (0, 342, 1894, 109) action Jump("frozenwater")

            #sand
            hotspot (8, 112, 1692, 203) action Jump("sand")

            #bushes
            hotspot (13, 518, 784, 225) action Jump("bushes")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("oasissouthernmovelow")

    label oasissouthernmovelow:

        scene oasissouthern

        call screen oasissouthernmove

    screen oasissouthernmove():

        imagemap:

            idle "oasissouthernarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Jump("oasissouthernlow")

            #left
            hotspot (43, 456, 114, 103) action Jump("oasiswesternlow")

            #right
            hotspot (1757, 500, 120, 110) action Jump("oasiseasternlow")

    label milliedeath:

        scene black

        m "The commotion seems to being coming from here."
        v "Wait.......look in the water!!"

        scene milliedeath

        m "WAIT....THAT'S MS. MILLIE!!!"
        v "The oasis is entirely frozen over too!"
        unknown "Look, she's the one that did it!"
        m "M-ME??"
        unknown "I saw her with the victim last night!"
        unknown "She probably froze the water, too!"
        m "WHAT?! I didn't do this! I would never!"
        v "Mariatu! Let's get back to the hotel! Hurry!"

        scene black with fade

        jump safe

    label safe:

        scene hotelroom with fade

        show mariatusad at left
        show vetadefault1 at right

        m "I...I can't believe they think I did it."
        v "But you didn't do it, right?"
        m "Of course I didn't do it! Ms. Millie was perfectly fine when I saw her."
        m "Sure I got a scolding, but that doesn't mean I should kill her!"
        v "Well, those people seem adamant about you as the killer. We'll need to prove your innocence."

        show quainflip:
            xalign 0.7

        q "I don't think that's a good idea."
        v "Ack! When did you get here?"
        m "Perfect! Quain should accompany you!"
        v "What?"
        q "I'd rather not."
        m "You're not going to leave Veta to investigate on her own, are you?"
        q "..."
        q "I guess that's a worse idea. Someone has to babysit her."
        v "Hey! I'm not a child!"
        q "Do you want to interrogate people on your own?"
        v "...Well..."
        v "Now that you mention it, I guess I'll let you tag along."
        m "I'll check on the other students in the meantime. Thank you for doing this!"
        v "Of course!"

        scene black with fade

        q "Let's check out the oasis first."

        $ storypoints += 1

        call screen hotelroomday

    label crimescene:

        scene oasissouthern

        q "There's Ms. Millie."
        v "*shudder* I really don't like looking at her."
        q "Me neither, but we need to bring her killer to justice."
        v "I hope we can catch whoever did this soon."

        call screen oasissouthern

    label frozenwater:

        scene oasissouthern

        v "The oasis is completely frozen."
        q "I wonder who did this."
        v "Someone with ice abilities for sure."
        q "Someone powerful for sure. We'll need to be careful while investigating."
        v "I'd rather not meet the same end as Ms. Millie."

        call screen oasissouthern

    label sand:

        scene oasissouthern

        v "I keep slipping in this sand."
        q "You've got boots on."
        v "I know tha- WHOA!!"
        q "Lucky I caught you."
        v "Would you like a gold star for that?"
        q "No, I would like to stop touching your sweaty hand."
        v "If you weren't my friend-{nw}"
        q "We're not friends."

        call screen oasissouthern

    label bushes:

        scene oasissouthern

        v "The sky is beautiful."
        q "The sky needs more clouds over the sun."
        v "The sky is almost beautiful."

        call screen oasissouthern
        
    label oasiswesternlow:

        scene oasiswestern

        call screen oasiswestern
    
    screen oasiswestern():

        tag location

        imagemap:

            idle "oasiswesternbuttons.png"

            #buildings
            hotspot (1757, 500, 120, 110) action Jump("westbuildings")

            #tree
            hotspot (934, 69, 471, 787) action Jump("westtree")

            #Ellis
            #if storypoints >= 10:
                #hotspot  action Jump("Ellis")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("oasiswesternmovelow")

    label oasiswesternmovelow:

        scene oasiswestern

        call screen oasiswesternmove

    screen oasiswesternmove():

        imagemap:

            idle "oasiswesternarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Jump("oasiswesternlow")

            #arrow
            hotspot (1751, 492, 131, 123) action Jump("oasissouthernlow")

    label westbuildings:

        scene oasiswestern

        v "There are a lot of hotels around here, ours included."
        q "This is probably where the tourists stay, to separate them from the locals."
        v "I can see that. There are three souvenir shops that I can see from here alone."
        q "I should get a souvenir for my parents now that I think about it."
        v "We can check those shops out, but maybe hold off on buying anything until we see what the market has."

        call screen oasiswestern

    label westtree:

        scene oasiswestern

        v "Let's take a break in the shade."
        q "I guess we can rest our legs. The oasis is larger than expected."
        v "Here, let me get some water for us."

        call screen oasiswestern

    label Ellis:

        if etalk == 1:

            scene oasiswestern

            e "Good morning, you two. Tourists seeing the sights?"
            q "Yes, something like that."
            e "Well, I'm terribly sorry about the commotion earlier today. It's not everyday someone gets murderered here!"
            q "We're actually investigating the murder. Can we ask you some questions?"
            e "If it'll help find the killer!"

            $ etalk += 1
            
            jump oasiswesternlow

        elif etalk >= 2:

            scene oasiswestern

            menu:

                "Victim":
                    q "Can you tell us what you know about the victim?"
                    e "She's a teacher if I remember correctly. I've seen her a few times over the years with her classes."
                    q "Has she done anything over those years that would upset someone?"
                    e "No! In fact, a lot of the locals liked her because she brought business here. Those students of hers always buy a lot of our goods."
                    q "Hmm, so none of the locals seem to want her dead..."
                    v "Maybe someone else knows more about Ms. Millie."
                    jump Ellis

                "Suspect":
                    q "Do you know anything about the suspect?"
                    e "I think she's one of the teacher's students. Rumors are going around that she's the one that froze the oasis too."
                    q "She's definitely one of the students, but she doesn't have ice abilities. She doesn't have any abilities."
                    v "Aside from forgetting things."
                    q "If she is the killer, what motive does she have?"
                    e "I heard she got into an arguement with the teacher late last night! Probably something to do with that."
                    jump Ellis

                "Ms. Millie's Friends":
                    q "Is there anyone else you know that was close to the victim?"
                    e "Hmm...I think there was someone in the market that knows her better than I do. I don't know specifically who, but she was a frequent there."
                    q "So someone at the market knows more information."
                    v "I think it's time we visited the market."

                "Goodbye":
                    jump oasiswesternlow 
        else:
            e "How's the investigation?"


    label marketlow:

        scene market

        if storypoints == 12:
            
            jump bumpaimon
        else:

            call screen market

    screen market():

        tag location

        imagemap:

            idle "market.png"

            #pottery stand
            hotspot (0, 5, 786, 886) action Jump("potterystand")

            #food cart
            hotspot (909, 143, 471, 521) action Jump("foodcart")

            #stalls
            hotspot (1447, 6, 233, 596) action Jump("stalls")

            #if storypoints >= 13:
                #hotspot  action Jump("potteryseller")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

    label potteryseller:

        scene market

        if storypoints >= 13:

            scene market with fade

            show potteryseller at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            q "Good morning, sir. Could we ask you some questions?"
            p "Hmph. I'm too busy at the moment to answer your silly questions."
            p "...But, if you're willing to help me, I'll be happy to help you."
            q "What do you need help with, sir?"
            p "It's my knife. I lost my fettling knife and now I can't make my pottery without it."
            q "Don't worry, sir. We'll help you find it."
            v "I don't remember seeing a knife anywhere."
            q "Maybe someone knows where it is?"

            $ storypoints += 1

            call screen market
        
        elif storypoints >= 14:

            scene market with fade

            show potteryseller at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            p "Found my knife yet?"
            q "No, sir. We'll keep looking."

            call screen market

        elif storypoints >= 15:

            scene market with fade

            show potteryseller at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            p "Found my knife yet?"
            q "Yes, sir. We got it right here."
            "Fettling Knife handed over"
            p "Ah, yes. This is definitely my knife. Where did you find it?"
            q "Actually, the receptionist at the hotel we're staying at found it."
            v "She said she used to work for you and recognized the knife."
            p "...I'm glad she's doing well."
            p "Go ahead and ask away. You earned it."

            $ storypoints += 1

            call screen market

        else:

            scene market with fade

            show potteryseller at left
            show vetadefault1 at right
            show quainflip:
                xalign 0.7

            p "How can I help you?"

            menu:
                "Victim":
                    
                    q "There was a murder earlier today. Do you happen to know anything about the victim."
                    p "A lot of us market sellers know Millie alright. Her class field trips helped bring in money in the slow season."
                    q "Do you know anyone who might have some kind of ill will towards her?"
                    p "Not that I know of. She was well liked by most everyone."
                    q "Is there anyone else that she happened to be close to here at the market?"
                    p "Hmm...That food cart was something she frequented every time she visited."

                    if ptalk == 1:
                        $ ptalk += 1
                    else:
                        jump potterystand

                "Food Cart" if ptalk >= 2:

                    q "So Ms. Millie visited that food cart over there often?"
                    p "Very. The food there is delicious, but I think they were close friends."
                    q "Do you know where the food cart seller is now? Or when they'll return?"
                    p "He might be prepping his food right now. You should probably check back later."
                    v "Maybe we should check out that food cart before he comes back."
                    q "Agreed."

                    $ storypoints += 1

                    jump potteryseller

                "Goodbye":

                    call screen market


            
    label potterystand:

        scene market

        v "Look at all of these!"
        q "Fine craftsmanship indeed."
        v "Glad I told you to wait until we got here to buy a souvenir?"
        q "I was waiting anyway without you telling me to."

        call screen market

    label bumpaimon:

        scene market with fade

        "THUD!"

        show vetadefault1 at right with fade
        show quainflip with fade:
            xalign 0.7 

        v "Ooof!"
        unknown "Ack! I'm sorry!"

        show aimonupset at left

        unknown "I'm terribly sorry! Are you okay?"
        v "Um...yeah, I'm fine."

        show aimonhappy at left
        hide aimonupset

        unknown "Thank goodness! My name's Aimon, by the way. I was looking for something before I bumped into you."
        a "You haven't seen a necklace lying around, have you?"
        q "Depends on what the necklace looks like."
        a "It's a pig necklace. Pink. I think I dropped it by the oasis, but I didn't see it."
        v "Actually, we did find a necklace like that on our way here. Is it this one?"
        a "Yes! You found it! It was a gift from a close friend and I've been feeling sick since I lost it. Thank you!"

        $ backpack.remove_item(necklace)

        "Necklace handed over to Aimon"

        a "Thank you again! I'll see you around!"

        hide aimonhappy

        v "Interesting fellow."

    label foodcart:

        scene market

        if storypoints == 17:

            v "This must be the food cart that boy was talking about."
            q "There's no here manning the cart. I guess we'll have to wait until the owner comes back to ask questions."
            v "I guess you're rig-{nw} ACK!!"
            q "What's wrong?"
            v "My...my head feels like it's going to explode!!"
            q "Did you hurt yourself today? Hit your hit somewhere?"
            v "I touched the cart for a second and now I-I can't see!"
            q "Here's my arm, hang onto it. Let's find a medical professional. There has to be a hospital or clinic somewhere around here."
            v "Wait! I can see something! It's a picture."
            q "I don't see any pictures."
            v "I think it's in my head. I can see the food cart. And Ms. Millie! And someone else!"
            "Investigate the picture!"

            call screen market

        else:

            v "There's no one here."
            q "Must be on break."
            v "But I'm hungry..."

    #screen foodcartsnapshot():

        #imagemap:

            #idle

            #seller
            #hotspot  action Jump("snapshotseller")

            #Ms. Millie
            #hotspot  action Jump("snapshotMs")

            #foodcart
            #hotspot  action Jump("snapshotcart")

            #necklace
            #hotspot  action Jump("snapshotnecklace")

    #label snapshotseller:

        #scene

        #call screen foodcartsnapshot

    #label snapshotMs:

        #scene

        #call screen foodcartsnapshot

    #label snapshotcart:

        #scene

        #call screen foodcartsnapshot

    #label snapshotnecklace:

        #scene 

        #call screen foodcartsnapshot

    label hotelroomdaylow:

        scene hotelroomday 

        call screen hotelroomday with fade

    screen hotelroomday():

        tag location

        imagemap:

            idle "hotelroomdaybuttons.png"

            #outside
            hotspot (1114, 240, 549, 408) action Jump("roomoutsideday")

            #bed
            hotspot (180, 701, 1140, 293) action Jump("bedday")

            #painting
            hotspot (219, 190, 435, 303) action Jump("roompaintingday")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transition = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("hotelroomdaymovelow")

    label roomoutsideday:

        scene hotelroomday 

        v "Wow, the sand outside looks like it's blue!"
        q "I'm more concerned with the fact that the window doesn't have curtains or blinds."
        v "Ms. Millie did say that the school booked a cheap hotel."
        q "A hotel so cheap that they can't afford curtains."
        v "At least the view is beautiful."
        q "I suppose."

        call screen hotelroomday 

    label bedday:

        scene hotelroomday 

        v "*lays on bed* These beds are really comfy!"
        q "They certainly are."
        v "This comforter matches my clothes, too!"
        q "Indeed, you blend right in. I almost forgot you were here. Almost."
        v "Wow, the betrayal. I thought we were friends, detective partners."
        q "Well, I agree that we are partners. Not so sure about friends."
        v "Hmph."

        call screen hotelroomday

    label roompaintingday:

        scene hotelroomday 

        v "It's a cactus."
        q "Thank you for pointing out the obvious."
        v "You're welcome."

        call screen hotelroomday 

    label hotelroomdaymovelow:

        scene hotelroomday

        call screen hotelroomdaymove

    screen hotelroomdaymove():

        imagemap:

            idle "hotelroomdayarrow.png"

            #arrow
            hotspot (18, 570, 129, 94) action Call("hotelhallwaydaylow")

            #back
            hotspot (18, 952, 105, 72) action Call("hotelroomdaylow")

    label hotelhallwaydaylow:

        scene hotelhallwayday with fade

        call screen hotelhallwayday

    screen hotelhallwayday():

        tag location

        imagemap:

            idle "hotelhallwaydaybuttons.png"

            #room
            hotspot (970, 177, 297, 596) action Jump("roomday")

            #door
            hotspot (243, 131, 144, 372) action Jump("hallwaydoorday")

            #window
            hotspot (5, 94, 101, 112) action Jump("hallwaywindowday")

            #light1
            hotspot (519, 164, 82, 88) action Jump("hallwaylightday")

            #light2
            hotspot (737, 191, 109, 112) action Jump("hallwaylightday")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transition = fade)

            #boot
            hotspot (5, 924, 82, 126) action Jump("hotelhallwaydaymovelow")

            if storypoints == 4:
                imagebutton auto "recepidcard.png" xalign 0.5 yalign 0.5 action Jump("receptidcard")


    label roomday:

        scene hotelhallwayday

        v "That's my room!"
        q "We can always take a break if you want."
        v "I think it's you who needs a break."

        call screen hotelhallwayday 

    label hallwaydoorday:

        scene hotelhallway

        show vetadefault at right
        show quaindefault at left

        q "This doesn't look like a regular guest room."
        v "It could be for employees only."
        q "There's no sign that says that. Just the room number."
        v "It's locked. Someone doesn't want just anyone in there."
        q "It could be a supply room."
        v "I guess we'll leave it at that."

        call screen hotelhallwayday

    label hallwaywindowday:

        scene hotelhallwayday

        v "I can't see!"
        q "I can see just fine."
        v "That's because you're tall."

        call screen hotelhallwayday 

    label hallwaylightday:

        scene hotelhallwayday

        v "These lights are very aesthetic."
        q "They certainly set the mood."

        call screen hotelhallwayday 

    label hotelhallwaydaymovelow:

        scene hotelhallwayday

        call screen hotelhallwaydaymove

    screen hotelhallwaydaymove():

        imagemap:

            idle "hotelhallwaydayarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Jump("hotelhallwaydaylow")

            #arrow1
            hotspot (490, 441, 105, 83) action Jump("hotellobbydaylow")

            #arrow2
            hotspot (1063, 576, 95, 96) action Jump("hotelroomdaylow")

    label hotellobbydaylow:

        scene hotelobby with fade

        if storypoints >= 9:
            jump hotellobbydayreceplow

        else:
            jump hotellobbydaymid

    label hotellobbydaymid:

        scene hotelobby with fade
        call screen hotellobbyday

    screen hotellobbyday():

        tag location

        imagemap:

            idle "hotelobbybuttons.png"

            #chandelier
            hotspot (1333, 9, 325, 225) action Jump("chandelierday")

            #painting
            hotspot (978, 58, 343, 202) action Jump("lobbypaintingday")

            #desk
            hotspot (978, 58, 343, 202) action Jump("deskday")

            #couch
            hotspot (929, 333, 563, 278) action Jump("couchday")

            #carpet
            hotspot (601, 803, 1128, 271) action ("carpetday")

            #floor
            hotspot (563, 645, 1336, 123) action Jump("floorday")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Call("hotellobbydaymovelow")


    label chandelierday:

        scene hotelobby

        v "It's so pretty!"
        q "Don't stare at it for too lo-{nw}"
        v "MY EYES!!"
        q "I WARNED YOU!"
        v "I've gone blind. Quain, please be my eyes."
        q "I can't believe this."

        call screen hotellobbyday  

    label lobbypaintingday:

        scene hotelobby

        v "It's a nice painting of sand."
        q "There's sand a few feet away though..."
        v "Maybe some people forget that they're in the middle of the desert."
        q "What kind of person forgets that they're in the desert?"
        v "Mariatu."
        q "...I can't argue with that."

        call screen hotellobbyday

    label deskday:

        scene hotelobby

        q "There's no receptionist."
        v "Maybe they're on break?"

        call screen hotellobbyday 

    label couchday:

        scene hotelobby

        v "This is a comfy couch."
        q "Isn't it called a sofa?"
        v "Pretty sure it's a couch."
        q "A couch doesn't have armrests."
        v "Says who?"
        q "Says the people who make them."
        v "Oh really? And who told you that?"
        q "One of the furniture sellers back home."
        v "Hmm...I still think it's a couch."
        q "*facepalm*"

        call screen hotellobbyday  

    label carpetday:

        scene hotelobby

        q "This is a nice carpet."
        v "Too bad it has some sand on it."

        call screen hotellobbyday  

    label floorday:

        scene hotelobby

        q "The marble floors are certainly eye-catching."
        v "It's so shiny. I'm surprised there isn't sand on it."
        q "Someone's gotta be cleaning it."

        call screen hotellobbyday 

    label hotellobbydayreceplow:

        scene hotelobbyrecep
        
        call screen hotellobbydayrecep

    screen hotellobbydayrecep():

        tag location

        imagemap:

            idle "hotelobbyrecep.png"

            #chandelier
            hotspot (1333, 9, 325, 225) action Jump("chandeliertwoday")

            #painting
            hotspot (978, 58, 343, 202) action Jump("lobbypaintingtwoday")

            #recep
            hotspot (33, 233, 229, 277) action Jump("recepday")

            #couch
            hotspot (929, 333, 563, 278) action Jump("couchtwoday")

            #carpet
            hotspot (601, 803, 1128, 271) action Jump("carpettwoday")

            #floor
            hotspot (563, 645, 1336, 123) action Jump("floortwoday")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag", transition = fade)

            #map
            hotspot (1785, 916, 91, 134) action Show("sketchmap", transtion = fade)

            #boot
            hotspot (5, 924, 82, 126) action Call("hotellobbydaymovelow")


    label chandeliertwoday:

        scene hotelobby

        v "It's so pretty!"
        q "Don't stare at it for too lo-{nw}"
        v "MY EYES!!"
        q "I WARNED YOU!"
        v "I've gone blind. Quain, please be my eyes."
        q "I can't believe this."

        call screen hotellobbydayrecep  

    label lobbypaintingtwoday:

        scene hotelobby

        v "It's a nice painting of sand."
        q "There's sand a few feet away though..."
        v "Maybe some people forget that they're in the middle of the desert."
        q "What kind of person forgets that they're in the desert?"
        v "Mariatu."
        q "...I can't argue with that."

        call screen hotellobbydayrecep

    label couchtwoday:

        scene hotelobby

        v "This is a comfy couch."
        q "Isn't it called a sofa?"
        v "Pretty sure it's a couch."
        q "A couch doesn't have armrests."
        v "Says who?"
        q "Says the people who make them."
        v "Oh really? And who told you that?"
        q "One of the furniture sellers back home."
        v "Hmm...I still think it's a couch."
        q "*facepalm*"

        call screen hotellobbydayrecep  

    label carpettwoday:

        scene hotelobby

        q "This is a nice carpet."
        v "Too bad it has some sand on it."

        call screen hotellobbydayrecep  

    label floortwoday:

        scene hotelobby

        q "The marble floors are certainly eye-catching."
        v "It's so shiny. I'm surprised there isn't sand on it."
        q "Someone's gotta be cleaning it."

        call screen hotellobbydayrecep  

    label recepday: 

        jump recepdaydiscussion

    label recepdaydiscussion:
         
        scene hotelobby with fade

        show receptionisthappy at left
        show vetadefault1 at right
        show quainflip:
            xalign 0.7

        r "How can I help you?"
        menu: 
            "Suspicious Door":
                q "We noticed the door down the hallway. It's not marked for employees, but it's far too small to be a suite."
                r "Hmm, I'm not really sure what that door is for. I actually just started working here less than a week ago."
                q "Your ID card was stuck under the door. I'm assuming you've never opened that door before?"
                r "That's correct. I've never been down that hallway before. The employee rooms are down this hallway behind me."
                q "I see."
                jump recepdiscussion

            "New Job":
                v "So you're new to the job?"
                r "Yes! I've lived here all my life in the outskirts of the town. The hotel was hiring and I took the opportunity for better pay."
                q "Where were you working before?"
                r "I was working in the market for one of the pottery sellers. It was hard work and the pay wasn't worth it."
                jump recepdiscussion

            "Fettling Knife" if storypoints == 14:

                q "Good morning, ma'am. The pottery seller in the market lost his fettling knife. Do you happen to know where it is?"
                r "Actually...now that you mention it, I did happen to find a fettling knife on my walk to work this morning."
                r "It was just lying there in the sand. I was running late, so I didn't get a chance to return it."
                r "This definitely is his knife though. His name is engraved on the handle. Here you go!"
                $ backpack.add_item(knife)
                v "Now we can return the knife!"

                $ storypoints += 1

                jump recepdiscussion

            "Goodbye":
                jump hotellobbydaylow


    label hotellobbydaymovelow:

        scene hotellobby

        call screen hotellobbydaymove

    screen hotellobbydaymove():

        imagemap:

            idle "hotelobbyarrow.png"

            #arrow
            hotspot (532, 490, 103, 100) action Call("hotelhallwaydaylow")

            #back
            hotspot (18, 952, 105, 72) action Call("hotellobbydaylow")

    return
