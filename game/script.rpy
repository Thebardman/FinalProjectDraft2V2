# Declare characters used by this game. The color argument colorizes the
# name of the character.

# This defines the blur effect so Ren'Py knows what it is

#Main character but his inner thoughts are italicized
define Ji = Character("John",color = "#25AD2E", who_font ="fonts/atwriter.ttf",who_size = 60 , what_font="fonts/atwriter.ttf", what_italic=True)
define J = Character("John", color = "#25AD2E", who_font ="fonts/atwriter.ttf", who_size = 60 ,what_font="fonts/atwriter.ttf")
define N = Character(None, what_font= "fonts/XTypewriter-Bold.ttf")

define M = Character("Mary",color = "#aa9615", who_font= "fonts/Roman_New_Times.otf", who_size = 90, what_font="fonts/LTMuseum-Bold.ttf" )
define T = Character("Toilet",color = "#ffffff",who_font ="fonts/atwriter.ttf", who_size = 60, what_font= "fonts/XTypewriter-Regular.ttf" )

#Extra characters for easier coding 
#Dead characters
define Dj = Character("John",color = "#25AD2E", who_font ="fonts/XTypewriter-Bold.ttf",who_size = 60 , what_font="fonts/XTypewriter-Bold.ttf", what_italic=True)
define Dt = Character("Toilet",color = "#ffffff",who_font ="fonts/XTypewriter-Bold.ttf", who_size = 60, what_font= "fonts/XTypewriter-Bold.ttf" )

#Complex characters
define D = Character(None, 
    window_yalign=0.5, 
    what_xalign=0.5, 
    what_text_align=0.5,
    window_background=None,
    what_yalign=0.5,             # Centers vertically
    what_outlines=[(2, "#000", 0, 0)],    # Adds a black outline so it's readable over any BG
    what_color="#930707ce", what_font="fonts/Roman_New_Times.otf", what_size = 100
)
#Complex characters
define Dj2 = Character(None, 
    window_yalign=0.5, 
    what_xalign=0.5, 
    what_text_align=0.5,
    window_background=None,
    what_yalign=0.5,             # Centers vertically
    what_outlines=[(2, "#000", 0, 0)],    # Adds a black outline so it's readable over any BG
    what_color="#196d1f", what_font="fonts/XTypewriter-Bold.ttf", what_size = 100
)
# The game starts here.

#Variables for cutting off choices
default CabinetBranch = True
default ChairBranch = True
default ToiletBranch = True
default RunCount = 0

label start:
# This is warning at the beginning so people know what they are getting into
    Dj2 "{color=#ffffff}WARNING{/color}" 
    Dj2 "{color=#ffffff}{size=80} This game has themes of insanity, death, thalossophobia, torture, and vulgar language.{/color}{/size}"
    Dj2 "{color=#ffffff}{size=80} Depictions may include: blood, gore, feces, uncomfortable noises, and ghosts. {/color}{/size}"
    Dj2 "{color=#ffffff}{size=80} Viewer discretion is advised.  {/color}{/size}"




label Beginning:
#Play rain noises or something

    scene bg starting
    
    play music "audio/rainBackground_1.wav" volume 0.2
    
    N "The rain was heavy. Each drop tearing through the valley."
    N "This lone house existed in the valley. The only semblance of hospitality."
    N "It was a meticulous trap laid by its creator. Just for me..."

   
    jump The_Forgotten
    hide bg starting
label The_Forgotten:

    scene bg livingroom
    show john idle
    Ji " The rain beat down making a sporadic rhythm of wooden clicks and bobs against the house."
    Ji "I was thoroughly surprised by the lack of electronics and modern appliances in this home."
    Ji "The only electronics were a brown telephone, the fridge, the stove and the homes lighting system."
    
    Ji " This place was not kind in any way. Everything about it felt wrong. Something... No, this region is giving me the heebie jeebies." 
    Ji "An example being, there was sunlight only an hour ago but this sudden rain storm rushed in all of sudden."
    Ji "My car mysteriously breaking down and having a flat when all I did was drive on flat dirt, or the issues with the engine."
    Ji " Most importantly, all this land being as abandoned as it is with no sort of expansion."
    Ji " All this land, and only a single home in a valley..."

    jump Empty_Thoughts

label Empty_Thoughts:
    scene bg livingroom
    show john annoyed
    Ji "I stared at the brown phone. It was my siren's call. This dinky rotary phone straight out of the 70's."
    J " God I hate how brown this thing is..."
    Ji " It reminds me of shit with how weirdly colored it is."

    J "{b} tap tap tap {/b}..."

    J "There has to be something to do here..."
    menu:
        "Look for a Book?" if CabinetBranch:
            jump The_Cabinets
        "Pace Around?" if ToiletBranch:
            jump Pace_Maker
        "Get a Chair?" if ChairBranch:
            jump Foreboding
    return



#-----------------------------------------------
#-- Book Route Start
#-----------------------------------------------
label The_Cabinets:
    scene bg kitchen
    show john idle
    Ji " I moved around this weird house looking for anything that looked remotely interesting. Anything. A book, a pencil, paper?"
    Ji " How are you going to have nothing to entertain yourself here?"
    Ji " As I rounded the corner into a room I hit head first into a tall cabinet."
    show john frustrated
    J "Why? Why do you put it there?"
    show john idle
    play sound "audio/rummagingThroughBooks_1.wav" volume 0.5
    Ji "As I looked up there there were, a set of books."
    Ji "I found something to finally free myself from this place."
    jump Ol_Times

label Ol_Times:
    show john annoyed
    Ji "{font=fonts/LTMuseum-MediumItalic.ttf}The Art of Baking 100 Different Cakes by Mary DeLou{/font}"
    J "You got to be fucking with me... Who the fuck owns a recipe book, when you don't have shit for fucking miles!?"
    Ji "Add the fact that I'm hungry as shit and the only thing in this damn house are old cans preserved fruits and veggies that look older than dinosaur shit."
    show john idle
    J "Breathe... Breathe...Read the damn book and move onto the next."
    Ji "If it wasn't for the fact that I had lost my sanity, this would have been perfect reading weather."
    Ji "To spite myself even more I walked into the kitchen to read this book."
    play sound "audio/flippingPagesInBook_1.wav" volume 0.5
    jump Meat_Poundcake

label Meat_Poundcake:
    Ji "I sat at the table beginning at the table of contents. Vanilla, Chocolate, Strawberry, Mixed Berry...\"Meat\"?"
    show john surprised
    play sound "audio/flippingPagesInBook_1.wav" volume 0.5
    J  "What? It can't be real. Page 59..."
    J "To start the meat poundcake you first need an assortment of red colored fruits. Begin by mashing the..."
    Ji "And I'm done with that. Really had me scared of what the hell this damn cake was."
    hide john
    show grandma idle
    M "That won't do~"
    hide grandma
    show john surprised
    J "Huh who's there?"
    play sound "audio/heartbeatCrescendo.wav" volume 1.0
    hide john
    show grandma idle
    M "If you are going to read a recipe, you might as well see it through the end dear."
    hide grandma
    jump With_Elbow_Grease

label With_Elbow_Grease:
    show john idle
    Ji "There are at the entry to the kitchen stood a thing I had never seen. It was a wax person with a melted exterior."
    hide john
    play sound "audio/grandmaScreech_1.wav" volume 0.5
    show grandma hunting
    M "The first step is to acquire red fruit."
    hide grandma
    show john frustrated
    Ji "I got up from the chair and backed away only to get charged by the creature."
    hide john
    show john injured
    J "AUGHh!"
    Ji "It lifted me off the ground by the throat and armpit. My windpipe was getting crushed under the force of the creatures grip."
    J "I couldn't speak, nor could I fight back."
    hide john
    show grandma hunting
    M "Remember to always wash your fruit."
    hide grandma hunting
    show john injured
    Ji "I felt a sudden pull and this crazy lady began flying to the other side of the house. Her grip on my throat not loosening at all"
    hide john injured
    jump Face_wash

label Face_wash:
    show bg bathroom
    show john injured
    Ji "This ghost lady then stopped in front of the bathroom."
    Ji "The door was thrust open and I realized what she was going to do."
    hide john injured
    show grandma hunting
    M   " This giant bowl will do."
    hide grandma hunting
    show john injured
    J "NO! NO! NO! NO! NO!"
    hide john
    show toilet idle
    Ji "I felt myself getting thrust face first into the toilet bowl and being drowned in the water."
    Ji "After a few seconds the ghost lady pulled my face back out"
    hide toilet
    show grandma hunting
    M "hmm... Not enough."
    hide grandma 
    show john injured
    J "Please..."
    hide john
    show toilet idle
    Ji "I was thrust back into the toilet. My lungs were on fire from the lack oxygen, and my constant struggle under this psychopath's grasp."
    hide toilet
    show john injured
    J "Stop...Please..."
    hide john
    show grandma idle
    M "hmm... Good enough."
    hide grandma
    show toilet bloody
    Ji "The toilet was covered in my blood. I felt sick from the sight and the drowning I endured."
    hide toilet
    show john injured
    Ji "We began to fly out of the bathroom and now to somewhere else. My life felt voilated beyond comprehension."
    hide john
    jump Fruit_mash


label Fruit_mash:
    show bg kitchen
    show grandma idle
    M "Now that your fruit is all clean, we begin the next step."
    hide grandma
    show grandma hunting
    M "You {b}mash{/b} the berries to a pulp"
    hide grandma
    show john injured
    J "please... I'm..."
    play sound "audio/bangingOnCabinet.wav" 
    Ji "I blacked out immediately  upon being slammed repeatedly against the stove with no chance of escape. "
    
    scene bg kitchenbloody
    D "The kitchen was painted {color=#B31F05}red{/color}. In the heat of cooking mistakes always happen. Some, greater than others..." with dissolve
    scene black with fade

    jump Fit_For_All


label Fit_For_All:
    show john injured
    Ji "It felt like a joke... A toilet. Right there. Staring at me from the abyss."
    J " I... Why? Why the fuck am I seeing a toilet as my FINAL SENDOFF?!"
    Ji "The gray ceramic toilet stood there. No noise, no sudden movement, perfectly still."
    Ji "I fell to my knees sobbing. But there was nothing to fall on but nothingness. No tears to be made."
    Ji "Yet there it stood. Never getting small or far away... It waited for me. "
    Ji "When nothing else would." 
    Ji "{color=#752B24}A fucking toilet.{/color}"
    
    $CabinetBranch = False
    $RunCount += 1
    jump Abyss

#-----------------------------------------------
#-- Book Route end
#-----------------------------------------------

#-----------------------------------------------
#-- Toilet Route start
#-----------------------------------------------

label Pace_Maker:
    scene bg livingroom
    show john idle
    Ji "I paced around the entire house relentlessly. The rain did not stop." 
    Ji "My boredom never waning. My patience, at rock bottom."
 
    show john frustrated
    J "{b}AHHHHH! WHY! WHY DID i ACCEPT TO COME TO THIS STUPID PLACE?! NOTHING ABOUT THIS PLACE MAKES SENSE.{/b}"
    J "{b}WHY THE FUCK DO WE OWN SOME RANDOM VALLEY IN THE MIDDLE OF NOWHERE!{/b}"

    Ji "Nothing made sense. It never did. From the stat of arriving here, to my car car breaking down"
    
    show john annoyed
    J "AHHHHH! WHY! WHY DID i ACCEPT TO COME TO THIS STUPID PLACE?! NOTHING ABOUT THIS PLACE MAKES SENSE."
    J "WHY THE FUCK DO WE OWN SOME RANDOM VALLEY IN THE MIDDLE OF NOWHERE!"
   
    Ji "Nothing made sense. It never did. From the start of arriving here, to my car car breaking down"
    #Queue toilet flushing
    T "Flush"
    Ji "If matters were not worse, the toilet is being used by a ghost. Not that it made my life any better."
    jump Malfunction

label Malfunction:
    scene bg bathroom
    show john idle
    Ji "I walked towards the bathroom in a rush. My impatience had grown so big that even a malfunctioning toilet seemed more interesting than anything else."
    Ji "I opened the door to the bathroom and there it was. This white ceramic shitter that is distracting me from my cruel reality."   
    Ji "I began inspecting the toilet's pipes and the internal buoy for any issues. There was nothing wrong with it."
    show john annoyed
    J "What the hell is wrong with you? Is there some sort of backflow from the rain water causing something else to happen?"
    hide john
    show toilet idle
    T "Bloop"
    hide toilet
    show john surprised
    Ji "The toilet somehow bubbled. I am not sure how it did that."

    jump Going_Once

label Going_Once:
    show john idle
    Ji "Seeing as I didn't know what was exactly happening I tried flushing the toilet."
    hide john
    show toilet idle
    T "Flush"
    hide toilet
    show john idle
    J "Well, you still work. I guess..."
    hide john
    show toilet idle 
    T "Bloop"
    hide toilet
    show john idle
    Ji "The toilet once again bubbled. This toilet is weird; Just like this house. It's all either really old or, on the verge of collapse. With not much else to do I began going back to my pacing around."
    hide john
    show toilet idle
    T "Swoosh"
    hide toilet
    show john idle
    Ji "I had only made my way out the bathroom only to hear it go off again."
    hide john
    show toilet idle
    T "Bloop Bloop Bloop"
    hide toilet
    show john idle
    jump One_Or_Two

label One_Or_Two:
    Ji "I begun pacing once more throughout the house. If anything this was more entertaining than doing nothing."
    hide john
    show toilet idle
    T "Flush"
    hide toilet
    show john idle
    Ji "The toilet kept flushing randomly now. I tried to act like it didn't exist but it would sudde-"
    hide john
    show toilet idle
    T "Bloop Bloop Bloop"
    hide toilet
    show john idle
    Ji "Like that. The toilet just kept making noise. I don't know what feels more annoying now, the lack of control over my situation or the ghost who keeps flushing my god damn toilet."
    hide john
    show toilet idle
    T "Swoosh"
    hide toilet
    show john idle
    Ji "I darted towards the bathroom with a fire inside and a click of my tongue ready to fire."
    hide john
    jump Potty_Mouth

label Potty_Mouth:
    show john annoyed
    
    J "SHUT THE FUCK UP! ALL THIS BLOOP! BLOOP! BLAH! BLAH! HOW ABOUT YOU LET ME WALK IN PEACE!?"
   
    hide john
    show toilet idle
    T "Bloop"

    hide toilet
    show john annoyed
    J "NO! I HAVE DEALT WITH NOTHING BUT STUPID SHIT ALL DAY! IF YOU THINK I AM NOT WILLING TO BREAK SOMETHING I WILL!"

    hide john
    show toilet idle
    T "Bloop"
    hide toilet
    show john annoyed
    Ji "This toilet was something sent to piss me off. It doesn't fucking shut up! It keeps making all this goddamn noise!"
    Ji "All I want is some peace in this rotting shit hole of a house but, that is nigh impossible."
    "..."
    Ji "Silence there was. It was just me, and this stupid toilet."
    jump Shit_Faced

label Shit_Faced:
    J "You like pissing people off or is this something special just for me?"
    hide john
    show toilet idle
    T "Bloop"
    hide toilet
    show john frustrated
    J "HAHAHAHAHAHAHA! I'm actually going insane... I'm talking to a fucking toilet like it can actually talk."
    hide john
    show toilet idle
    T "Bloop Bloop"
    hide toilet
    show john idle
    J "If you can understand what I'm saying, bubble five time."
    hide john
    show toilet idle
    T "Bloop Bloop Bloop Bloop Bloop"
    "..."
    hide toilet
    show john surprised
    J "Oh what th-"
    hide john
    show toilet idle
    T "Bloop"
    hide toilet
    show john annoyed
    J "Oh. You're the bitchy type of ghost... I mumbled"
    jump English_Please



label English_Please:
    show john surprised
    J "What the fuck was it... Uh, Oh yeah! Ouija board... Bubbles... Bubble once for yes, and two for no."
    J "Why are you pissing me off?"
    hide john
    show toilet idle
    T "Swoosh"
    hide toilet
    show john frustrated
    J "Motherfucker! I said BUBBLES! YES! OR NO!"
    show john idle
    J " Deep breathes... Okay... did you intentionally piss me off?"
    hide john
    show toilet idle    
    T "Bloop"
    hide toilet
    show john annoyed
    J "Bitch. Why? Fuck... That's on me. Are you an evil ghost?" 
    hide john
    show toilet idle 
    T "Bloop Bloop"
    hide toilet
    show john idle
    J "That's a fucking lie."
    hide john
    show toilet idle 
    T "Bloop Bloop"
    jump Magic_Toilet

label Magic_Toilet:
    hide toilet
    show john idle
    J "Why are you here?"
    hide john
    show toilet idle 
    T "Flush"
    hide toilet
    show john idle
    J "Uh, are you from here?"
    hide john
    show toilet idle 
    T "Bloop bloop"
    hide toilet
    show john idle
    J "Are you a demon?"
    hide john
    show toilet idle 
    T "Bloop bloop"
    hide toilet
    show john idle
    J "Why does this place suck ass?"
    hide john
    show toilet idle 
    T "Bloop"
    hide toilet
    show john idle
    J "... You don't like this place?"
    hide john
    show toilet idle 
    T "Bloop"
    hide toilet
    show john idle
    J "Did you break my car?"
    hide john
    show toilet idle 
    T "Bloop bloop"
    hide toilet
    show john idle
    J "Fuck... are there more haunted things or ghosts here?"
    T "Bloop"
    jump Constipation

label Constipation:
    play music "audio/heartbeatCrescendo.wav" volume 0.7
    Ji "I was so focused on this toilet that I didn't hear the rain stop. My mind was racing. What other ghost's existed here?"
    J "Is there a ghost after me?"
    hide john
    show toilet idle 
    T "Bloop"
    hide toilet
    show john idle
    J "Can I fight it?"
    hide john
    show toilet idle 
    T "Swoosh"
    hide toilet
    show john annoyed
    J "Shit. Uh, can I live till the mechanic arrives?"
    "..."
    J "Answer me toilet!"
    hide john
    show toilet bloody 
    T "Bloop Bloop"
    hide toilet
    show john idle
    J "This can't be happening."
    Ji "I began pacing back and forth. I then realized the rain had stopped."
    jump Dogwater

label Dogwater:
    Ji "Seeing my chance to get out I dashed for door."
    hide john
    show toilet bloody 
    T "BLOOP BLOOP"
    hide toilet
    show john idle
    Ji "I slammed against the front door trying to open it. I grabbed the door knob but it wouldn't budge."
    Ji "In my panicked state I couldn't hear the strange noises coming from outside the door. It sounded like bubbles. A lot of bubbles."
    hide john
    show toilet bloody 
    T "BLOOP BLOOP"
    hide toilet
    show john idle
    J "WHAT TOILET? I NEED TO GET OUT NOW I'M GOING TO DIE!"
    hide john
    show toilet bloody 
    T "BLOOP BLOOP"
    hide toilet
    show john idle
    D "Oh Dear is it locked? Let me help." with dissolve
    window hide
    "{size=80}creak... BOOM{/size}"
    hide toilet
    show john injured
    Dj " Before I realized it I was hit with an immense torrent of water that started slicing through the house. My body was crushed from the force of the water."
    D "Finch... Making them struggle will never work." with dissolve
    window hide
    jump Clogged

label Clogged:

    show john injured
    Dj "It's cold. I was running and then I got crushed."
    hide john
    show toilet bloody 
    Dt "Bloop"
    hide toilet
    show john injured
    Dj "You can hear me thinking?"
    hide john
    show toilet bloody 
    Dt "Bloop"
    hide toilet
    show john injured
    Dj "Am I dead?"
    hide john
    show toilet bloody 
    Dt "Bloop"
    hide toilet
    show john injured
    Dj "So heaven and hell are real?"
    hide john
    show toilet bloody 
    Dt "Bloop Bloop"
    hide toilet
    show john injured
    Dj "Then where are we?"
    hide john
    show toilet bloody 
    Dt "Flush"
    hide toilet
    show john injured
    Dj "Is there anything to do here?"
    hide john
    show toilet bloody 
    Dt "Bloop"
    hide toilet bloody
    scene black with fade
    D "Darkness holds every answer. Darkness hides all. No matter how far they may go. Darkness is all there is in the abyss." with dissolve
    window hide
    
    $ToiletBranch = False
    $RunCount += 1
    jump Abyss

#-----------------------------------------------
#-- Toilet Route End
#-----------------------------------------------

#-----------------------------------------------
#-- Chair Route Start
#-----------------------------------------------

label Foreboding:
    scene bg chair
    show john annoyed
    Ji "I can't stand this. I can't stand the absolute emptiness of this place."
    show john idle
    Ji "I paced quickly to the living room to grab a chair and dragged it over to the window."
    show john frustrated
    Ji "The noise it made against the wood was frustrating; just like my resentment for this place."
    show john idle
    Ji "I set it up to look out the window but, did I really wish to do so? Was this really all I could do?"
    jump Party_for_One

label Party_for_One:
    show john idle
    Ji "I sat down and stared out the window. The rain was soothing. A mild distraction from the ever encompassing anxiety of this place."
    Ji "For a moment, I had felt peace. Peace in the fact that this chair was front row seat to my execution."
    Ji "As I watched the rain from the window something was darting for the window."
    Ji "First it was nothing."
    scene bg chairbloody
    show john injured
    Ji "next it was dot."
    Ji "finally, an eyeshot."
    Dj "Who was it? I wish I knew..."
    scene black with fade
    D "Not my finest work but, enjoyable indeed." with dissolve
    window hide
    $ChairBranch = False
    $RunCount += 1
    jump Abyss



#-----------------------------------------------
#-- Chair Route End
#-----------------------------------------------

#-----------------------------------------------
#-- Enter Abyss
#-----------------------------------------------
label Abyss:
    if RunCount == 1:
        Dj2 "Is there really something out here?"
        scene black with fade
        jump Empty_Thoughts
    elif RunCount == 2:
        Dj2 "I'm not dead. I'm not dead. I'm not dead. I'm not dead. I'm not dead. I'm not dead."
        scene black with fade
        jump Empty_Thoughts
    elif RunCount ==3:
        Dj2 "What is it you are waiting for? Leave me alone..."
        scene black with fade
        return