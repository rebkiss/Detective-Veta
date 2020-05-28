define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")


label start:

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
            hotspot (1793, 939, 112, 102) action
                
        

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


    return
