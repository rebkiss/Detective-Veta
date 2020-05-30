define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")


label start:

    label oasislow:

        scene oasisbuttons

        call screen oasis

    screen oasis():

        imagemap:

            idle "oasisbuttons.jpg"
            
            #water
            hotspot (264, 616, 1346, 119) action Jump("water")

            #sand  
            hotspot (22, 850, 1885, 219) action Jump("sand")

            #sky    
            hotspot (4, 9, 1900, 339) action Jump("sky")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #map
            hotspot (1793, 939, 112, 102) action Call("maplow")


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

        scene marketbuttons

        call screen market

    screen market():
        imagemap:

            idle "marketbuttons.jpg"

            #map
            hotspot (1795, 939, 110, 99) action Call("maplow")

            #bag
            hotspot (1790, 38, 118, 105) action Show("bag", transition = dissolve)

            #shade
            hotspot (635, 19, 824, 429) action Jump("shade")

            #pottery
            hotspot (27, 507, 1584, 557) action Jump("pottery")

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

    return
