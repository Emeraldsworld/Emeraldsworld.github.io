# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#??? is collapsa before she is revealed
define n = Character("Natalie")
define b = Character("Bianca")
define q = Character("???")
define i = Character("Iris")
define t = Character("Teacher")
define c = Character("Collapsa")
define slowdissolve = Dissolve(.5) 
default good = 0 
default bad = 0
default goodending = 50
# The game starts here.

screen health:
    # This is the timer bar we will use to display the countdown.
    bar value goodending range 100 xalign 0.5 yalign 0.9 xmaximum 300 at top

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 3.0
     
    scene bg cafe
   

    # These display lines of dialogue.

    #the multiple bgs
    #cue peaceful music and school noises
    #school bg
    show screen health 
    "It was the first day of the new year at Sadington High, ripe with potential. Students flushed into the building in packs, quipping back and forth amongst each other."
    show nat sad with Dissolve(.5):
        zoom 1.3
        xalign 0.5 
        yalign 0.7
    play music "audio/my_music/Natalie's Theme.mp3" fadein 2.0
    #upset natalie
    n "Eeeugh. I could barely get out of bed this morning, and now I have to go to school…? Summer went by so fast... At least I can work on my art project during study hall. It's turning out better than I thought it would."
    #cruel Bianca
    
    "Bianca entered the cafeteria, the queen bee of the school, her hive buzzing around her. Her disgusted gaze fixed on Natalie, her victim of choice since freshman year."
    show nat sad :
        zoom 1.3
        xalign 0.3
        yalign 0.7
    stop music fadeout 2.0

    show bianca evil with Dissolve(.5) :
        zoom 1.3
        xalign 0.8
        yalign 0.7
    
    b "What is that?"
    play music "audio/my_music/Bianca's Theme.mp3"
    #happy natalie
    show nat happy with Dissolve(.5): 
        zoom 1.3
        xalign 0.3
        yalign 0.7
    n "My art project I was working on over summer, it's-"
    #regular bianca
    b "It's disgusting. Who would draw something like that? Are you trying to curse the school?"
    #cue rip sound
    #angry natalie
    show nat angry with Dissolve(.5):
        zoom 1.3
        xalign 0.3
        yalign 0.7

    n "What the- why would you do that?!"
    
    #signal collapsa, but she isnt there
    show nat sad with Dissolve(.5): 
        zoom 1.3
        xalign 0.1 
        yalign 0.7
    show bianca evil with Dissolve(.5):
        zoom 1.3
        xalign 0.5
        yalign 0.7
    q "Punch her. She's asking for it."
    #natalie scared

    n "What? Who said that?"

    q "Punch. Her. She destroyed your art. Destroy her face."

    n "What... do I do?"

    menu: 
        "Punch Bianca":
            jump choice1_punch

        "Run Away":
            jump choice2_run

label choice1_punch:
    $ goodending += 10
    #where the bar will be when figured out

    "+ 1 point! Your becoming friends with Collapsa!"
    "The Health Bar lets you know how close you are becoming friends or enemies with collapsa. You don't want to see what happens if you two become enemies."
    #upset bianca  
    b "EAGH! What is wrong with you?!"
    #angry natalie
    n "What's wrong with me?! You tore up my art!"
    show nat angry with Dissolve(.5): 
        zoom 1.3
        xalign 0.1
        yalign 0.7
    #regular bianca
    hide bianca evil with Dissolve(.5)
    "Natalie runs to the bathroom."
    jump bathroom

label choice2_run:
    #bathroom bg
    scene bg bathroom
    $ goodending -= 10
    #where meter will be
    if good == 1: 
        #upset natalie
        "Natalie ran to the bathroom feeling embarassed."
        b "What a Freakshow."
        "-1 point! Collapsa hates you."
        "Why does Bianca hate me? What did I ever do to her!? She was never like this to me in middle school…"
        show natalie sadblink with Dissolve(.5) :
            zoom 1.3
            xalign 0.5 
            yalign 0.7
        jump bathroom2

label bathroom: 
    if bad == 1:
        #upset natalie
        #bathroom bg
        n "Why does Bianca hate me? What did I ever do to her!? She was never like this to me in middle school…"
        show natalie sadblink with Dissolve(.5): 
            zoom 1.3
            xalign 0.5 
            yalign 0.7
        jump bathroom2

label bathroom2:
    q "She realized what an easy target you were~..."
    hide bianca evil with Dissolve(.5)
    #scared natalie
    show nat angry with Dissolve(.5):
        zoom 1.3
        xalign 0.3
        yalign 0.7
    n "What?! Who said that?!"
    #cue collapsa
    show collapsa evil with Dissolve(.5):
        zoom 1.3
        xalign 0.8
        yalign 0.7
    q "I'm right here. Turn around."
        
    #confused natalie or scared
    n "Wait- you're...in the mirror? But there's no one here!"
    #smug collapsa
    q "You're here, aren't you?"
        
    n "But you aren't me!"
    q "That's right. I'm Collapsa...and someone's looking for you."
    n "What? Wait, don't go!"
    #worried iris
    hide collapsa evil with Dissolve(.5)
    show iris sad with Dissolve(.5) :
        zoom 1.3
        xalign 0.8
        yalign 0.7
    show nat sad with Dissolve(.5) :
        zoom 1.3
        xalign 0.3
        yalign 0.7
    i "Natalie? Who are you talking to?"
    n "You...  didn't see her?"
    i "See who?"
    "Rinnnnnng"
    #cue bell ringing sound
    n "I- I should go."
    i "Natalie? Is something wrong? Who were you talking to?"
    n "I don't want to be late for class…"
    hide iris sad with Dissolve(.5)
    hide nat sad with Dissolve(.5)
    jump demoend

    label Hallway:
    #change to the hallway bg
    "Students are rushing to their classes, ushered by the bell, but a group of girls casually take up half the hallway, gossiping amongst themselves."
    show bianca evil with Dissolve(.5):
        zoom 1.3
        xalign 0.8
        yalign 0.7
    show nat sad with Dissolve(.5):
        zoom 1.3
        xalign 0.3
        yalign 0.7
    b "Is that Natalie? Are you too scared to say anything after your little outburst earlier?" 
    show nat sad with Dissolve(.5):
        zoom 1.3
        xalign 0.1
        yalign 0.7
    show collapsa evil behind bianca with Dissolve(.5):
        zoom 1.3
        xalign 0.5
        yalign 0.7
        alpha 0.8
    c "Natalie, Ignore that b-"
    n "What? Now you care about me?"
    c "I don't care about anything. Now go stand up for yourself before I kill her."
    n "Should I listen to her...?"
    menu: 
        "Stand up against Bianca":
            jump choice1_standup

        "go to class":
            jump choice2_class
label choice1_standup:
    $ goodending += 10
    "+1 point, Your becoming friends with Collapsa."
    hide collapsa evil
    n "Hey, Bianca! Come over here?...Please?"
    b "Why do you think you can boss me around? We aren't friends, even if you say please."
    n "I know. But I wanted to sound nice. "
    b "Nice? How pathetic."
    n "Nice isn't pathetic. You're pathetic. You're so jealous of me that you always want to bully me instead of improving yourself. You want to be an artist, but you don't practice. Instead, you try to ruin your competitor’s paintings and confidence, so you can feel better about yourself. That is pathetic. Not being nice."
    b "Wow. You think that I am jealous. No, you are."
    n "Ok. Are you asking to get punched?"
    b "You're too much of a wuss to punch m-"
    #cue punch sound
    n "I hope that you end up bruised."
    b "ARGH! That hurt! You are such a-"
    t "What is all this- Girls! Detention after school! Both of you!"
    hide bianca evil
    hide nat sad
    

label choice2_class:
    $ goodending -= 10
    hide bianca evil
    "-1 point, Collapsa is hating you even more."
    c "Wow, You're a chicken. You're such a coward that you have to run away from your fears instead of protecting yourself. You're so weak."
    n "I am not weak! I just....I don't want to get in trouble. I would rather walk away than stand up for myself. If I stand up for myself…then I would be just like Bianca. If I ignore her, she'll stop."
    c "Yeah, maybe. Or maybe she'll try even harder to get on your nerves. Maybe you should show her who's boss."
    n "I don't know..."
#(cue classroom bg, collapsa/bia leaves, bell sound)
    t "Hello Students! Today we will be talking about how to write emotion into stories."
    hide collapsa evil
    hide nat sad 
    #cue mini game tutorial
    # This ends the game.

label demoend :
    "Thanks for playing! This is the end of this Demo. More is coming soon!"
    return
