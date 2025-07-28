#######################################################
#
#
#
#
#######################################################

define Dusky = Character('Dusky', color="#ff0000")
define Acy = Character('Acy', color="#da229c")
define Behuta = Character('Behuta', color="#5516e9")
define Chiikawa = Character('Chiikawa', color="#f32fa1")

label start:

    play music "audio/LLSS02.mp3" fadein 1.0
    
    # This is the first scene of the game.
    "You are Chavid, a Sophomore student at Northern Illinois University, studying Computer Science."
    "Today you have CSCI 466, a class that teaches you about databases and web development."
    "You wake up in your Stevenson B dorm, going down the elevator with the spilled drink and hurry off to meet your friend"

label scene1:

    scene bg stevo

    "Damn. I hate walking all the way just to meet my friend at Altgeld Hall."
    "Why do we have to meet here? It's so far away from the dorms?"

label scene2:

    scene bg altgeld
    
    show dusky normal
    Dusky "Hey Chavid! How are you doing!"
    
    menu:
        "Terrible. Stevo ran out of italian ice and I had to drink a fucking soda!":
            "You lean in distressed."
            show dusky sad
            Dusky "Damn Chavid, I love you I always have. i want to be with you forever."
            
        "I'm okay":
            "You say with an evil fucked up voice." 
            show dusky normal
            Dusky "Oh,"
            
        "Just shut up and let's go to 466":
            "You groan with Behuta-ness"
            show dusky blushing
            Dusky "Oh, okay, I guess we can go to class then."

    scene black with fade
    jump scene3

label scene3:

    scene bg psychcs

    "You arrive at the Computer Science building."

    show dusky tired
    Dusky "We're late for class, we gotta learn HTML!"
    
    hide dusky
    "Damn, I love HTML!"
    "You rush to the classroom."

label scene4:

    scene bg lab

    show acy normal
    Acy "Hey guys! You're just in time for the HTML lecture. Behuta is programming a website around his Jimmy Johns being late again."
    hide acy

    show dusky laughing
    Dusky "With his can of monster he pours into a coffee mug?"
    hide dusky

    show acy worried
    Acy "Yeah. He said he switched to coffee but he's lying. He still drinks monster."
    hide acy

    "You sit down at your desk and open your laptop, ready to learn about HTML and web development."

    scene black with fade

    scene bg classroom1

    show behuta
    Behuta "Hey guys. Today I will read off slides and tell Chiikawa to stop asking me questions about php."
    hide behuta

    show chiikawa normal
    Chiikawa "What about your Jimmy Jo-"
    hide chiikawa

    show behuta
    Behuta "I will also tell him to stop asking me about my Jimmy Johns order."
    hide behuta

    show chiikawa normal
    Chiikawa "What flavor monster do-"
    hide chiikawa

    show behuta
    Behuta "I will also tell him to stop asking me about my monster addiction."
    hide behuta

    # This ends the game.
    return