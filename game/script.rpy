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
        imagemap:

            idle "MenuImage.jpg"

            #journal
            hotspot (340, 155, 337, 352) 
            
            #profiles
            hotspot (839, 157, 337, 350)

            #mysteries
            hotspot (1351, 158, 336, 349)

            #items
            hotspot (579, 601, 335, 351)

            #save
            hotspot (1109, 602, 337, 349)

            #back
            hotspot (1704, 891, 167, 149) action Hide("bag", transition = dissolve)

    


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
