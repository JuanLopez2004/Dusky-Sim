#######################################################
#
#
#
#
#######################################################

define Dusky = Character('Dusky', color="#E03B8B")

label start:

    play music "audio/nevermeant.mp3" fadeout 1.0 fadein 1.0
    
    # This is the first scene of the game.
    "You wake up in your Stevo B dorm and hurry off to meet your friend"


label scene1:

    play music "audio/nevermeant.mp3" fadeout 1.0 fadein 1.0 loop

    scene bg altgeld
    
    show dusky normal
    Dusky "Hey Chavid! How are you doing! I love restech!"
    
    menu:
        "That's amazing! I love restech.":
            "You lean in with excitement."
            show dusky happy
            Dusky "Yes! I knew you'd understand! Restech is the best!"
            
        "I'm okay":
            "You say with an evil fucked up voice." 
            show dusky normal
            Dusky "Oh,"
            
        "just shut up and let's go to CSCI 466":
            "You groan with lehuta-ness"
            show dusky blushing
            Dusky "Oh, okay, I guess we can go to class then."

    scene black with fade
    jump scene2

label scene2:

    scene bg psychcs

    "You arrive at the computer science building."

    show dusky tired
    Dusky "We're late for class, we gotta learn HTML!"
    
    hide dusky
    "Damn, I damn love HTML."
    "You rush to the classroom."

    # This ends the game.
    return