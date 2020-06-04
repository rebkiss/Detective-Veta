define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")


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
                if self.findmember(member).amount >= amount:
                    return(self.findmember(member).amount)
                else:
                    return(False)
            else:
                return(False)
       
        def find_member(self, member):
            return(self.party[[i.member for i in self.party].index(member)])

        def remove_member(self, member, amount=1):
            if self.has_member(member):
                self.findmember(member).amount -= amount
                if self.findmember(member).amount <= 0:
                    self.party.pop(self.party.index(self.findmember(member)))
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

            idle "menuconcept.jpg"

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("journaltwo"), Hide("profile"), Hide("mystery"), Hide("itemone"), Hide("itemtwo")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Hide("journalone"), Hide("journaltwo"), Show("profile"), Hide("mystery"), Hide("itemone"), Hide("itemtwo")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Hide("journalone"), Hide("journaltwo"), Hide("profile"), Show("mystery"), Hide("itemone"), Hide("itemtwo")]

            #items
            hotspot (18, 737, 335, 129) action [Hide("journalone"), Hide("journaltwo"), Hide("profile"), Hide("mystery"), Show("itemone"), Hide("itemtwo")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("journalone"), Hide("journaltwo"), Hide("profile"), Hide("mystery"), Hide("itemone"), Hide("itemtwo")]

    screen journalone():
        imagemap:

            idle "journaloneconcept.png"

            #right arrow
            hotspot (937, 870, 53, 45) action [Show("journaltwo"), Hide("journalone")]

            #journal
            hotspot (17, 273, 338, 128) action [Hide("journalone"), Show("journalone")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Show("profile"), Hide("journalone")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Show("mystery"), Hide("journalone")]

            #items
            hotspot (18, 737, 335, 129) action [Show("itemone"), Hide("journalone")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("journalone")]

    screen journaltwo():
        imagemap:

            idle "journaltwoconcept.png"
            
            #left arrow
            hotspot (627, 870, 47, 48) action [Show("journalone"), Hide("journaltwo")]

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("journaltwo")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Show("profile"), Hide("journaltwo")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Show("mystery"), Hide("journaltwo")]

            #items
            hotspot (18, 737, 335, 129) action [Show("itemone"), Hide("journaltwo")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("journaltwo")]

    screen profile():
        imagemap:

            idle "profileconcept.png"

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("profile")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Hide("profile"), Show("profile")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Show("mystery"), Hide("profile")]

            #items
            hotspot (18, 737, 335, 129) action [Show("itemone"), Hide("profile")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("profile")]

    screen mystery():
        imagemap:

            idle "mysteryconcept.png"

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("mystery")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Show("profile"), Hide("mystery")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Hide("mystery"), Show("mystery")]

            #items
            hotspot (18, 737, 335, 129) action [Show("itemone"), Hide("mystery")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("mystery")]

    screen itemone():
        imagemap:

            idle "itemoneconcept.png"

            #right arrow
            hotspot (937, 869, 56, 52) action [Show("itemtwo"), Hide("itemone")]

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("itemone")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Show("profile"), Hide("itemone")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Show("mystery"), Hide("itemone")]

            #items
            hotspot (18, 737, 335, 129) action [Hide("itemone"), Show("itemone")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("itemone")]

    screen itemtwo():
        imagemap:

            idle "itemtwoconcept.png"

            #left arrow
            hotspot (622, 869, 51, 49) action [Show("itemone"), Hide("itemtwo")]

            #journal
            hotspot (17, 273, 338, 128) action [Show("journalone"), Hide("itemtwo")]
            
            #profiles
            hotspot (17, 428, 337, 127) action [Show("profile"), Hide("itemtwo")]

            #mysteries
            hotspot (18, 582, 336, 130) action [Show("mystery"), Hide("itemtwo")]

            #items
            hotspot (18, 737, 335, 129) action [Show("itemone"), Hide("itemtwo")]

            #back
            hotspot (192, 921, 139, 93) action [Hide("bag", transition = dissolve), Hide("itemtwo")]

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
            #jump documentmissingone

        else: 
            q "Sorry, we don't have it."
            dude "Ashame."
            call screen market
            #jump documentmissingtwo

    #label documentmissingone:
            #scene marketconcept

            #show vetaconcept at right
            #show dude at center
            #show quainplaceholder at left

            #q "..."
            #v "Do you mean...this piece of paper?"
            #q "What the-?! Where did you-?!"
            #dude "YES!
            #You found it!"
            #"Piece of paper given to the dude."
            #$ backpack.remove_item('paper')
            #v "Glad to help!"
            #call screen market

   #label documentmissingtwo:
            #scene marketconcept

            #show vetaconcept at right
            #show dude at center
            #show quainplaceholder at left           
            
            #q "Sorry, we don't have it."
            #dude "Ashame."
            #call screen market

    return
