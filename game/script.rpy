define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")

image vetadefault:
    "vetadefault1.png"
    pause 2
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

define storypoints = 1

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

    label chapterone:

        scene chapter1
        $ renpy.pause(delay=5,hard=False)

        scene hotelroom
        show vetadefault at right
        show quaindefault at left

        v "Well, Mariatu is staying with another student, so we can start our investigation now."
        q "Let's start with finding Mariatu's lost room key. It has to be somewhere in this hotel."
        v "Sounds like a plan! I'll bring my bag along, too! It has some useful stuff and we can put the
        things we find in here."
        q "I have this map here that we can use to travel to different places."
        v "Let's get this investigation started!"
        $ storypoints += 1

        call screen hotelroom

    label hotelroomlow:

        scene hotelroom

        call screen hotelroom

    screen hotelroom():

        imagemap:

            idle "hotelroombuttons.png"

            #outside
            hotspot (1114, 240, 549, 408) action Jump("roomoutside")

            #bed
            hotspot (180, 701, 1140, 293) action Jump("bed")

            #painting
            hotspot (219, 190, 435, 303) action Jump("roompainting")

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag")

            #map
            hotspot (1785, 916, 91, 134) action Show("map")

            #boot
            hotspot (5, 924, 82, 126) action Call("hotelroommovelow")

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

        scene hotelhallway

        call screen hotelhallway

    screen hotelhallway():

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
            hotspot (1786, 28, 103, 115) action Show("bag")

            #map
            hotspot (1785, 916, 91, 134) action Show("map")

            #boot
            hotspot (5, 924, 82, 126) action Call("hotelhallwaymovelow")

    label room:

        scene hotelhallway

        v "That's my room!"
        q "We can always take a break if you want."
        v "I think it's you who needs a break."

        call screen hotelhallway

    label hallwaydoor:

        scene hotelhallway

        q "This doesn't look like a regular guest room."
        v "It could be for employees only."
        q "There's no sign that says that. Just the room number."
        v "It's locked. Someone doesn't want just anyone in there."
        q "It could be a supply room."
        v "I guess we'll leave it at that."

        $ storypoints += 1

        call screen hotelhallway

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

    label hotelhallwaymovelow:

        scene hotelhallway

        call screen hotelhallwaymove

    screen hotelhallwaymove():

        imagemap:

            idle "hotelhallwayarrow.png"

            #back
            hotspot (18, 952, 105, 72) action Call("hotelhallwaylow")

            #arrow1
            hotspot (490, 441, 105, 83) action Call("hotellobbylow")

            #arrow2
            hotspot (1063, 576, 95, 96) action Call("hotelroomlow")

    label hotellobbylow:

        scene hotelobby

        call screen hotellobby

    screen hotellobby():

        imagemap:

            idle "hotelobbybuttons.png"

            #chandelier
            hotspot (1333, 9, 325, 225)

            #painting
            hotspot (978, 58, 343, 202)

            #desk
            hotspot (978, 58, 343, 202)

            #couch
            hotspot (929, 333, 563, 278)

            #carpet
            hotspot (601, 803, 1128, 271)

            #floor
            hotspot (563, 645, 1336, 123)

            #bag
            hotspot (1786, 28, 103, 115) action Show("bag")

            #map
            hotspot (1785, 916, 91, 134) action Show("map")

            #boot
            hotspot (5, 924, 82, 126) action Call("hotellobbymovelow")


    label chandelier:

        scene hotelobby

        v "It's so pretty!"
        q "Don't stare at it too lo-{nw}"
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
        q "I can't argue with that."

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
        q "Someone's gotta clean it."

        call screen hotellobby

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
        

    #label oasislow:

        #scene oasisbuttonsperson

        #call screen oasis

    #screen oasis():

        #imagemap:

         #   idle "oasisbuttonsitems.jpg"
            
            #water
          #  hotspot (360, 619, 1300, 128) action Jump("water")

            #sand  
           # hotspot (28, 404, 1803, 126) action Jump("sand")

            #sky    
            #hotspot (4, 9, 1900, 339) action Jump("sky")

            #bag
           # hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #map
           # hotspot (1793, 939, 112, 102) action Call("maplow")

            #paper
           # hotspot (1381, 855, 114, 69) action Jump("firstpaper")

            #man
           # hotspot (228, 740, 97, 262) action Jump("Ellis")

    #screen oasistwo():

        #imagemap:

            #idle "oasisbuttonsperson.jpg"
            
            #water
           # hotspot (360, 619, 1300, 128) action Jump("water")

            #sand  
           # hotspot (28, 404, 1803, 126) action Jump("sand")

            #sky    
           # hotspot (4, 9, 1900, 339) action Jump("sky")

            #bag
            #hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #map
           # hotspot (1793, 939, 112, 102) action Call("map")

            #man
            #hotspot (228, 740, 97, 262) action Jump("Ellis")


    screen bag():

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
                action Hide("bag", transition = fade), Hide("journal", transition = fade), Hide("TheSuspiciousDoor"), Hide("TheMissingDoorKey")

            #bag
            hotspot (73, 404, 158, 221) action Hide("journal"), Hide("TheSuspiciousDoor"), Hide("TheMissingDoorKey")

            if storypoints >= 2: 
                textbutton "The Missing Door Key" action Hide("TheSuspiciousDoor"), Show("TheMissingDoorKey") xalign 0.3 yalign 0.3 
                

            if storypoints >= 3:
                textbutton "The Suspicious Door" action Hide("TheMissingDoorKey"), Show("TheSuspiciousDoor") xalign 0.3 yalign 0.4 

    screen TheMissingDoorKey():

        vbox:

            area (990, 292, 502, 495)

            text "We've finally arrived at the Oasis of Destiny, hidden deep in the Avius Desert. Unfortunately, my friend, Mariatu, seems to have lost her room key and is unable to find it. Quain, my partner in mystery solving, has agreed to help me find her key."

    screen TheSuspiciousDoor():

        vbox:

            area (990, 292, 502, 495)

            text "While investigating the hallway, we came across a door at the end of the hallway. It's too small to be a suite, and it doesn't have any signs on it besides the room number. We've decided it's a supply room, but I still have a feeling it's something more than that."
    screen mysteries():

        modal True
        
        if storypoints >= 2:

            imagemap:

                idle "mysterypageone.png"

                #back button
                hotspot (53, 934, 134, 99): 
                    action Hide("bag", transition = fade), Hide("mysteries", transition = fade)

                #bag
                hotspot (73, 404, 158, 221) action Hide("mysteries")

                if storypoints >= 2:
                    hotspot (446, 527, 109, 210) action Show("MissingKey")

    screen MissingKey():

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

    screen map():

        modal True

        imagemap:

            idle "MapConcept.jpg"

            #oasis
           # hotspot (714, 298, 488, 390) action Call("oasislow") 
            
            #hotel
            hotspot (479, 203, 212, 294) action Call("hotellobbylow") 
            
            #market
           # hotspot (1291, 236, 171, 232) action Call("marketlow")
            
            #back
            hotspot (1707, 924, 138, 119) action Call("map", transition = dissolve)


   # label marketlow:

        #scene marketbuttonsperson

       # call screen market

   # screen market():
        #imagemap:

            #idle "marketbuttonsperson.jpg"

            #map
           # hotspot (1795, 939, 110, 99) action Call("maplow")

            #bag
           # hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #shade
           # hotspot (529, 13, 951, 420) action Jump("shade")

            #pottery
            #hotspot (50, 391, 1415, 659) action Jump("pottery")

            #person
           # hotspot (1533, 433, 188, 317) action Jump("documentmissing")

    #label hotellow:

        #scene hotelbuttons

       # call screen hotel

   # screen hotel():
       # imagemap:

           # idle "hotelbuttons.jpg"

            #map
           # hotspot (1793, 939, 112, 102) action Call("maplow")

            #bag
           # hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #bed
           # hotspot (20, 608, 1076, 390) action Jump("bed")

            #view
           # hotspot (1225, 335, 310, 159) action Jump("view")

            #chairs
           # hotspot (1216, 575, 330, 90) action Jump("chairs")

            #flower
          #  hotspot (1601, 379, 273, 524) action Jump("flower")


  #  label water:
       # scene oasisconcept 
       # v "The water looks really refreshing right now. "
       # call screen oasis
   # label sand:
        #scene oasisconcept
       # v "I keep slipping in the sand."
       # call screen oasis
   # label sky:
      #  scene oasisconcept
      #  v "These clouds aren't helping with the heat."
      #  call screen oasis

   #label shade:
        #scene marketconcept
       # v "The canopy doesn't seem to do much with providing shade from the sun."
      #  call screen market

   # label pottery:
       # scene marketconcept
      #  v "A lot of the pottery here looks interesting.
      #  Too bad most are buried in sand."
      #  call screen market

   # label bed:
       # scene hotelconcept
       # v "The bed is so soft. I'll sleep good tonight."
       # call screen hotel

  #  label view:
       # scene hotelconcept
       # v "Sand. So much sand.
      #  I want to roll down one of the dunes."
      #  call screen hotel

   # label chairs:
       # scene hotelconcept
       # v "These chairs are comfy. 
       # Maybe I'll sleep under the stars sometime this week."
       # call screen hotel

   # label flower:
       # scene hotelconcept
       # v "I think these are lilies. My knowledge of flowers is a bit rusty."
       # call screen hotel

   # label firstpaper:
       # scene oasisconcept

        #show vetaconcept at right
      #  show quainplaceholder at left

      #  v "Hey, I found something!"
      #  q "What is that?"
      #  q "Seems like a piece of paper. Throw it out."
      #  v "Hold on, look on the back! There are some lines on here."
      #  q "Alright, it’s got some squiggles. Now throw it out."
      #  v "This could be important!"
     #   q "It's junk. Even if you kept it, what are the chances of you finding the rest of it?"
      #  v "Fine. I'll throw it out."
      #  "Piece of paper sneakily slipped into bag"
       # $ backpack.add_item(paper)

       # call screen oasistwo
#label Ellis:
       # scene oasisconcept

       # show quainplaceholder at left
       # show dude at right

       # menu: 
           # "What should I ask him about?"

           # "Murder":
            #    q "Can you tell me about the murder? What happened?"
             #   dude "A teacher from the city was killed last night.
              #  I didn’t know about it until I woke up this morning.
               # The oasis is frozen over too.
                #Someone with an ice ability must have done it.
                #Considering how rare that ability is around here, an outsider probably did it."
                #jump Ellis

           # "Victim":
              #  q "The victim, did you know anything about her?"
              #  dude "I just know she’s a teacher.
               # Some students had been in that crowd earlier and were saying that she was their teacher."
               # jump Ellis

           # "Suspect":
               # q "Is there someone that you think could be the murderer?"
              #  dude "Someone said they saw the teacher with a student last night.
              #  A lot of people started assuming that the student is the suspect.
              #  While that could be true, it’s probably best to wait until the authorities from the city arrive."
              #  q "Who was the person that saw the teacher and student together?"
              #  dude "I’m not sure.
              #  You could probably ask around at the market. Information spreads there."
              #  jump Ellis

           # "That's all":
               # q "Thank you for the information." 
              #  jump discussion

   # label discussion:
       # scene oasisconcept

       # show vetaconcept at right
       # show quainplaceholder at left

       # v "Well, no new information there besides the whole ice ability thing."
       # q "That and the fact that Ms. Millie and Mariatu were seen together last night. 
       # Did you know about this?"
       # v "Yeah...Mari lost her key as soon as we got to the room. 
       # She had to talk to Ms. Millie about it."
       # q "Why am I not surprised?"
       # v "We should probably check out the market.
       # Seems like a breeding ground for rumors and information."
       # q "Agreed."

       #if backpack.has_item(paper, amount=1):
          #  jump oasistwo

       # else: 
          #  jump oasislow

   # label documentmissing:
       # scene marketconcept

       # show vetaconcept at right
       # show dude at center
       # show quainplaceholder at left

      #  v "Is something the matter, sir?"
       # dude "Oh, I didn't see you two there. 
       # I lost a piece of my paper during the crowd earlier by the crime scene."
        
       # if backpack.has_item(paper, amount=1):
         #   q "..."
          #  v "Do you mean...this piece of paper?"
          #  q "What the-?! Where did you-?!"
         #   dude "YES!
         #   You found it!"
         #   "Piece of paper given to the dude."
         #   $ backpack.remove_item(paper, amount=1)
         #   v "Glad to help!"
         #   call screen market

       # else: 
           # q "Sorry, we don't have it."
           # dude "Ashame."
           # call screen market

    return
