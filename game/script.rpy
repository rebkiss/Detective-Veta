# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Veta")
define q = Character("Quain")
image dude = Placeholder("boy")
define dude = Character("dude")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene oasisconcept

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vetaconcept at right
    show dude at left

    label conversation:

    # These display lines of dialogue.

    menu:
        "What should I ask?"

        "Victim":
            v "Can you tell me more about the victim?"
            dude "I saw the teacher walking around at night."
            v "Where was she going?"
            dude "Seems like she was heading towards the water. 
            I've seen her on multiple visits here in the past. 
            I wouldn't be surprised if she wanted to check out the water and see if anything's changed."
            v "Was that where you saw her last?"
            dude "No, I didn't see anything after that.
            Some lady supposedly saw the whole thing happen."
            jump conversation

        "Suspect":
            v "Can you tell me more about the suspect? Why is she the suspect?"
            dude "Someone said that they saw the suspect with the teacher last night."
            v "Do you know why she was with the teacher?"
            dude "Don't know. I wasn't there. You should probably ask the lady who saw it. 
            She lives in the outskirts of town."
            jump conversation

        "Goodbye":
            v "I guess it's time to pay this lady a visit."

    # This ends the game.

    return
