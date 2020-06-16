define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")

default profile_highlights = False
default journal_highlights = False
default mysteries_highlights = False
default items_highlights = False

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

    label oasislow:

        scene oasisbuttonsperson

        call screen oasis

    screen oasis():

        imagemap:

            idle "oasisbuttonsitems.jpg"
            
            #water
            hotspot (360, 619, 1300, 128) action Jump("water")

            #sand  
            hotspot (28, 404, 1803, 126) action Jump("sand")

            #sky    
            hotspot (4, 9, 1900, 339) action Jump("sky")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #map
            hotspot (1793, 939, 112, 102) action Call("maplow")

            #paper
            hotspot (1381, 855, 114, 69) action Jump("firstpaper")

            #man
            hotspot (228, 740, 97, 262) action Jump("Ellis")

    screen oasistwo():

        imagemap:

            idle "oasisbuttonsperson.jpg"
            
            #water
            hotspot (360, 619, 1300, 128) action Jump("water")

            #sand  
            hotspot (28, 404, 1803, 126) action Jump("sand")

            #sky    
            hotspot (4, 9, 1900, 339) action Jump("sky")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #map
            hotspot (1793, 939, 112, 102) action Call("maplow")

            #man
            hotspot (228, 740, 97, 262) action Jump("Ellis")


    screen bag():

        modal True

        imagemap:

            ground "bagmenu.png"

            #back button
            hotspot (51, 938, 138, 95) action Hide("bag", transition = dissolve)

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

        imagemap:

            idle "profilespage.png"

            #back button
            hotspot (51, 938, 138, 95) action Hide("bag", transition = dissolve)

    screen journal():

        modal True

        imagemap:

            idle "journalpageone.png"

            #back button
            hotspot (51, 938, 138, 95) action Hide("bag", transition = dissolve)

    screen mysteries():

        modal True
        
        imagemap:

            idle "mysteries.png"

            #back button
            hotspot (51, 938, 138, 95) action Hide("bag", transition = dissolve)

    screen items():

        modal True

        imagemap:

            idle "itemspageone.png"

            #back button
            hotspot (51, 938, 138, 95) action Hide("bag", transition = dissolve)

    label maplow:

        scene mapconcept

        call screen map

    screen map():
        imagemap:

            idle "MapConcept.jpg"

            #oasis
            hotspot (714, 298, 488, 390) action Call("oasislow") 
            
            #hotel
            hotspot (479, 203, 212, 294) action Call("hotellow") 
            
            #market
            hotspot (1291, 236, 171, 232) action Call("marketlow")
            
            #back
            hotspot (1706, 925, 140, 119) action Hide("map", transition = dissolve)


    label marketlow:

        scene marketbuttonsperson

        call screen market

    screen market():
        imagemap:

            idle "marketbuttonsperson.jpg"

            #map
            hotspot (1795, 939, 110, 99) action Call("maplow")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #shade
            hotspot (529, 13, 951, 420) action Jump("shade")

            #pottery
            hotspot (50, 391, 1415, 659) action Jump("pottery")

            #person
            hotspot (1533, 433, 188, 317) action Jump("documentmissing")

    label hotellow:

        scene hotelbuttons

        call screen hotel

    screen hotel():
        imagemap:

            idle "hotelbuttons.jpg"

            #map
            hotspot (1793, 939, 112, 102) action Call("maplow")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #bed
            hotspot (20, 608, 1076, 390) action Jump("bed")

            #view
            hotspot (1225, 335, 310, 159) action Jump("view")

            #chairs
            hotspot (1216, 575, 330, 90) action Jump("chairs")

            #flower
            hotspot (1601, 379, 273, 524) action Jump("flower")


    label water:
        scene oasisconcept 
        v "The water looks really refreshing right now. "
        call screen oasis
    label sand:
        scene oasisconcept
        v "I keep slipping in the sand."
        call screen oasis
    label sky:
        scene oasisconcept
        v "These clouds aren't helping with the heat."
        call screen oasis

    label shade:
        scene marketconcept
        v "The canopy doesn't seem to do much with providing shade from the sun."
        call screen market

    label pottery:
        scene marketconcept
        v "A lot of the pottery here looks interesting.
        Too bad most are buried in sand."
        call screen market

    label bed:
        scene hotelconcept
        v "The bed is so soft. I'll sleep good tonight."
        call screen hotel

    label view:
        scene hotelconcept
        v "Sand. So much sand.
        I want to roll down one of the dunes."
        call screen hotel

    label chairs:
        scene hotelconcept
        v "These chairs are comfy. 
        Maybe I'll sleep under the stars sometime this week."
        call screen hotel

    label flower:
        scene hotelconcept
        v "I think these are lilies. My knowledge of flowers is a bit rusty."
        call screen hotel

    label firstpaper:
        scene oasisconcept

        show vetaconcept at right
        show quainplaceholder at left

        v "Hey, I found something!"
        q "What is that?"
        q "Seems like a piece of paper. Throw it out."
        v "Hold on, look on the back! There are some lines on here."
        q "Alright, it’s got some squiggles. Now throw it out."
        v "This could be important!"
        q "It's junk. Even if you kept it, what are the chances of you finding the rest of it?"
        v "Fine. I'll throw it out."
        "Piece of paper sneakily slipped into bag"
        $ backpack.add_item(paper)

        call screen oasistwo

    label Ellis:
        scene oasisconcept

        show quainplaceholder at left
        show dude at right

        menu: 
            "What should I ask him about?"

            "Murder":
                q "Can you tell me about the murder? What happened?"
                dude "A teacher from the city was killed last night.
                I didn’t know about it until I woke up this morning.
                The oasis is frozen over too.
                Someone with an ice ability must have done it.
                Considering how rare that ability is around here, an outsider probably did it."
                jump Ellis

            "Victim":
                q "The victim, did you know anything about her?"
                dude "I just know she’s a teacher.
                Some students had been in that crowd earlier and were saying that she was their teacher."
                jump Ellis

            "Suspect":
                q "Is there someone that you think could be the murderer?"
                dude "Someone said they saw the teacher with a student last night.
                A lot of people started assuming that the student is the suspect.
                While that could be true, it’s probably best to wait until the authorities from the city arrive."
                q "Who was the person that saw the teacher and student together?"
                dude "I’m not sure.
                You could probably ask around at the market. Information spreads there."
                jump Ellis

            "That's all":
                q "Thank you for the information." 
                jump discussion

    label discussion:
        scene oasisconcept

        show vetaconcept at right
        show quainplaceholder at left

        v "Well, no new information there besides the whole ice ability thing."
        q "That and the fact that Ms. Millie and Mariatu were seen together last night. 
        Did you know about this?"
        v "Yeah...Mari lost her key as soon as we got to the room. 
        She had to talk to Ms. Millie about it."
        q "Why am I not surprised?"
        v "We should probably check out the market.
        Seems like a breeding ground for rumors and information."
        q "Agreed."

        if backpack.has_item(paper, amount=1):
            jump oasistwo

        else: 
            jump oasislow

    label documentmissing:
        scene marketconcept

        show vetaconcept at right
        show dude at center
        show quainplaceholder at left

        v "Is something the matter, sir?"
        dude "Oh, I didn't see you two there. 
        I lost a piece of my paper during the crowd earlier by the crime scene."
        
        if backpack.has_item(paper, amount=1):
            q "..."
            v "Do you mean...this piece of paper?"
            q "What the-?! Where did you-?!"
            dude "YES!
            You found it!"
            "Piece of paper given to the dude."
            $ backpack.remove_item(paper, amount=1)
            v "Glad to help!"
            call screen market

        else: 
            q "Sorry, we don't have it."
            dude "Ashame."
            call screen market

    return
