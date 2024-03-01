default inventory = []
default code_input = ""
image paper = "paper.png"

init python:
    # Function to add an item to the inventory
    def add_to_inventory(item):
        if item not in inventory:
            inventory.append(item)

    # Function to remove an item from the inventory
    def remove_from_inventory(item):
        if item in inventory:
            inventory.remove(item)

    # Function to use an item
    def use_item(item):
        if item == "cryptex":
            renpy.show_screen("cryptex_screen")

    def toggle_inventory():
        if renpy.get_screen("inventory_screen"):
            renpy.hide_screen("inventory_screen")
        else:
            renpy.show_screen("inventory_screen")

    
    def check_code():
        
        global code_input  # Make sure to access the global variable

        if code_input.strip().upper() == "MAGIC":
            renpy.notify("The cryptex opens revealing a paper inside!")
            renpy.hide_screen("cryptex_screen")
            # Replace 'secret_plan.png' with the path to your actual image file
            renpy.show("paper")
            jarl = "revealed"
            # Add a pause so the player can take in the revealed image
            # renpy.pause(5)
            # # Hide the image after a few seconds or by player's click
            # renpy.hide("paper.png")
        else:
            renpy.notify("Nothing happens. It seems that was not the correct code.")


define g = Character('Geralt', image="geralt", color="#c8ffc8")
define j = Character('Jarl Bjorn', color="#c8ffc8")
define a = Character('Astrid', image="astrid", color="#c8ffc8")
define n = Character('Niham', image="siren", color="#c8ffc8")

default astrid_state = 0 # <0 0 >0
default astrid_epilogue = ""

default niham_state = 'cursed' # cursed, dead, normal
default niham_epilogue = ""

default ritual = False # True False
default ritual_epilogue = ""

default jarl = "alive" # alive, dead, reward, revealed
default jarl_epilogue = ""

# -----------------------------------PART 1-----------------------------------------------------------------
screen always:
    fixed:
        xalign 0.95  # Align the button to the right side
        yalign 0.05  # Align the button to the top
        textbutton _("Inventory") action Function(toggle_inventory)

    

label inventory:
    call screen inventory_screen
    return

# Function to show the inventory screen
label show_inventory:
    call screen inventory_screen
    return

screen inventory_screen():
    vbox:
        for item in inventory:
            textbutton item:
                action Function(use_item, item)
        textbutton "Close" action Hide("inventory_screen")


screen cryptex_screen():
    grid 3 1 spacing 9:  # 2 rows, 1 column, 10 pixels of spacing
        # First row content
        add "cryptex_image.jpg"  # Add your cryptex image here
        $ code_input = ""
        input value VariableInputValue("code_input")        # Second row content
        vbox:  # Use a vbox for vertical layout of text and input
            text "In a whispered chant of five,"
            text "what ancient power brings tales alive?"

    # Position the "Try the code" button below the grid
    textbutton "Try the code" action Function(check_code)

    # Add a button to close the cryptex screen
    textbutton "Close" action Hide("cryptex_screen")


label start:
    scene bg tavern
    show screen always

    "Geralt enters the Novigrad tavern and sits down at a vacant table, ordering a mug of ale from an elven woman. A couple minutes later, two strangers approach him. "

    show warrior def at right

    "Stranger" "I can't believe it, the famous Geralt of Rivia."

    g profile "I didn't think I was so famous that people still talk about me on the skellige, and I didn't think I'd meet his people outside the islands."

    "Stranger" "So it's obvious where we're from?"

    g "I've been to the islands and well remember your gaze, as cold as the local waters. Surely it wasn't just the desire to play gwent that drove you this far."

    "Stranger" "You're right, Jarl Bjorn does need the services of a witcher. "

    g "Too bad, but I'm scheduled for dinner, sword sharpening, and pleasant conversation under the moon with a certain charming elf. Why don't you come back next week and see if there's an opening in my schedule?"
    
    "Stranger" "Sorry Geralt, but the Jarl doesn't have time to wait, especially this order is worth 20 others."

    g "When a witcher is offered too much, no good can come of it."

    "Stranger" "Don't worry, the task is not difficult for an experienced witcher, the high fee is only for the urgency, Jarl Bjorn is not in the best situation right now, so this money will be less of a problem for him."

    g "Fuck...and I thought I was gonna have the day off....."

label skellige_arriving:
    scene bg skellige_1
    "Skellige"
    "Home of warlike and brave sailors, who are commonly called pirates on the Big Land. And for good reason: since the islands are barren, sea robbery has become the main source of income for their inhabitants. The territory of the five large islands is divided among the clans, headed by the Jarls."

    scene bg skellige_2
    "A few rocky islets, where more sheep than people live. A tribe of drunken, slow-witted shepherds and fishermen. Conquer them? It couldn't be easier. That's what many of the lords of the Continent thought. All their strategies crashed on the cliffs of Skellige"

    scene bg skellige_3
    "The Skellige Islands are inhabited by seven clans. Each clan is considered by the locals to be the most warlike and brave, and will gladly challenge anyone who questions it to a duel. All of them, however, recognize the supremacy of the king, who is elected by vote. "

    scene bg skellige_4
    "The people of Skellige are of a different mold than the people of the Continent. They are bolder, tougher and less sensitive to pain. And most importantly, instead of fearing death, they look forward to it."

    scene bg skellige_5
    "The people of Skellige are more closely tied to nature than the people of the Continent. Nowhere else are druids more honored than on Skellig. Nowhere else do hunters have such respect for the beast. Nowhere else do they keep bears in their armies"

label ship_arriving:
    scene bg fog_ship
    "The fog covered almost all the water, practically depriving the crew of visibility. The silence was suddenly broken by a very pleasant song that was coming from some unknown place."

    "One of the sailors came closer to the board looking behind it, when suddenly something pulled him into the water. "

    "Sailor" "Man overboard!"

    "A harpy flies up from behind him, holding the sailor in its claws."

    menu:
        "Aard": 
            jump aard_ship_arriving

        "Igni":
            jump igni_ship_arriving
    
    label aard_ship_arriving:
        "you have knocked the harpy down and it falls into the water with the sailor."
    
    label igni_ship_arriving:
        "You have setted the harpy's wings on fire and it falls on board where it is killed instantly."
    
    g profile "It's strange that the harpies decided to attack the ship, but it's even stranger that there are sirens nearby."

    "After the harpy, 3 more harpies attacked the ship, but the witcher had no trouble dealing with them. "

    g "Harpies rarely attack big ships."

    "Sailor" "It's been happening a lot lately, that's why we called you here, because it's not normal even for the local waters, we've already lost a lot of good warriors, one consolation is that they died in battle."


label initial_jarl_talk:
    scene bg talk_with_jarl

    j "Greetings, witcher, I'm glad you took the time to visit our islands."

    g profile "Oh, Bjorn, how could I refuse to be so *kindly* invited to visit?"

    j "Don't worry, there's plenty in my coffers to make up for it."

    j "I needed you because Skellige is facing a threat my warriors cannot deal."

    j "Our ships are under increasing attack from the sea beasts, and at first it started with small losses, but soon the ships stopped coming home altogether."

    j "As ruler of the islands I can't ignore this problem, but my powers aren't unlimited, warriors, Nilfgardians, raids from Tsidaris, I can still deal with that, but sea beasts, that's a job for you Geralt."

    menu:
        "First, let's talk about payment":
            jump jarl_answer_1

        "I think I need more information":
            jump jarl_answer_2

        "No problem, I'm ready to help you":
            jump jarl_answer_3
    
    label jarl_answer_1:
        "I think 500 crones will motivate you to get the job done right, and fast."
    label jarl_answer_2:
        "If I knew more... go to the druids, they must know something, here's a paper just in case you're here to do my bidding, it'll get you through to a druid of any clan, but I'd advise you to go to Drih."
    label jarl_answer_3:    
        "Good, I knew I could count on you, here's a piece of paper just in case you're here doing my bidding, it'll get you through to any clan druid, but I'd advise you to go to Dreech."

    j "Go, witcher."

    "When you was about to leaving the room, you have noticed strange box at the table."
    "Cryptix. Usually it is used to send sicret messages, interesting, what Jarl could hiding."
    "You looked back and noticed that he not looking at you, it great moment to take it."

    menu:
        "Take the glinting object.":
            $ add_to_inventory("cryptex")
            "You have found a cryptex! It's now in your inventory."
        "Ignore it.":
            pass


# -----------------------------------PART 2-----------------------------------------------------------------

label druid_1:
    scene bg skellige_clan
    "As Geralt of Rivia steps into the heart of the clan's territory, the atmosphere is thick with anticipation. The villagers, adorned in the rugged garb of Skellige, cast wary glances his way, their expressions a mix of hope and dread. The Witcher's reputation precedes him; a solver of supernatural grievances, yet a harbinger of the violence that often follows."

    "He's led to a clearing where Astrid and an elder Druid stand waiting. Astrid, her stance embodying the fierce spirit of Skellige warriors, nods in recognition of Geralt. The Druid, cloaked in robes that whisper of ancient traditions and the deep, interconnected life of the isle, regards Geralt with a solemn gaze."

    "Druid" "Witcher"

    "Druid" "Skellige reels under the siren's curse. Niham's sorrowful wrath decimates our fleets, claiming lives and livelihoods. Her song of vengeance draws men to their doom, entwined in a fate most dire"

    "Astrid interjects, her voice firm, yet not without empathy"

    a profile"The siren was wronged, Witcher. Her love, twisted into a weapon against her. Yet, innocents pay the price for a feud they had no hand in"

    'The Druid turns his gaze towards the sea, where the setting sun casts a blood-red hue over the waters—a stark reminder of the violence that lurks beneath the waves.'

    "Druid" "We seek an end to this bloodshed. Your blade and your wisdom, Witcher, may guide us to peace or damnation. The choice is yours"

    "Author" "Geralt, silent, contemplates the moral quagmire laid before him. The request is clear—end Niham's torment and, with it, the threat to Skellige. Yet, the path to such an end is mired in shades of grey. To kill Niham is to silence a voice that sings of betrayal and lost love, yet to let her live risks further innocents."

    "Author" "As the trio stands in the dwindling light, the Witcher is acutely aware that his decision will ripple through the fates of all involved—Astrid, whose ambitions for her people hinge on resolving this crisis; the Druid, whose duty to the natural order and the traditions of Skellige guides his plea; and Niham, a creature of both beauty and sorrow, whose heart, once capable of love, now harbors only despair and vengeance."

    "Author" "In this moment, Geralt realizes the weight of the path he chooses will not just shape the destiny of Skellige but will also echo the values he embodies as a Witcher—whether to uphold the pursuit of justice, no matter the complexity, or to seek a resolution that might offer a semblance of peace to all parties entangled in this tragic tale."



# -----------------------------------PART 3-----------------------------------------------------------------

label astrid_1:
    scene bg skellige_road
    "In the quiet of the Skellige night, Astrid and Geralt find solace by a flickering fire, far from the ears of the clan. Astrid’s silhouette dances in the light, her features etched with resolve and an earnest plea for understanding. She begins, her voice a blend of strength and introspection."

    a profile "A life at sea, Geralt, teaches you about the currents beneath the surface—the unseen forces that shape our destinies. I stand now, caught in such a current, torn between the land that is my blood and the sea that offers escape from the disdain of my kin"

    "Geralt listens, his eyes reflecting the firelight, acknowledging the depth of her turmoil."

    a "Skellige is my heart, Witcher. Yet, in its beat, I find dissonance. My spirit, my prowess—seen but unacknowledged because I am not born a man. To leave is to abandon the very essence of who I am. To stay... is to fight a tide that may never turn in my favor."

    "A pause allows the gravity of her words to settle, the crackling fire punctuating her resolve."

    a "But there is more than my fate at stake here. Niham, the siren—her tale is one of love warped into a weapon of vengeance. I implore you, before the edge of your sword sings her final note, grant her an audience. Listen. Her pain might mirror the injustice we both fight against. Perhaps, in understanding her, we find a path to mend what has been broken"

    "Geralt nods, the weight of her request not lost on him"

    menu:
        "No, that monster should be killed":
            $ astrid_state -= 1 # -1 astrid
        "Astrid, your courage to seek understanding over vengeance is a rare compass. I will heed your counsel. Niham will have her voice heard. And you... You have my word, I'll weigh my actions with the justice they deserve":
            $ astrid_state += 1 # +1 astrid
        "I will do my best to make wise decision":
            pass # 0 astrid
    
# -----------------------------------PART 3-----------------------------------------------------------------

label niham_1:
    scene bg niham_trap
    "Geralt placed one of the witcher's traps in the sea."

    "As Niham struggles within the confines of Geralt's enchantment, her ethereal voice breaks the silence of the night, her words a blend of sorrow and rage."

    n cursed "You've caught me, Witcher, yet it's not the net that binds me but my own heart's despair. Once, I knew love beyond the bounds of sea and shore, a love that was torn from me as swiftly as it came"

    g profile "Your tale is heavy with loss. But vengeance... Is it the path you seek, or is there room for peace in your heart?"

    n "Peace? What peace is there when the world has seen fit to rip every shred of happiness from my grasp? Yet, you ask of my desires... They took him from me, cursed me to this fate. My voice, once a melody of joy, now a harbinger of doom"

    g "The curse you bear, it silences more than just your song. It keeps hidden the one who wronged you. If there was a way, would you seek retribution or restitution?"

    menu:
        "Your pain, it's a heavy burden. Let's find the one who cursed you. There's more to your story, and it doesn't end here, with vengeance":
            jump niam_alive

        "I've seen too much suffering born of revenge. I'm sorry, but your cycle of vengeance ends with me tonight":
            $ niham_state = "dead"
            jump niam_dead

# -----------------------------------PART 4.1 -----------------------------------------------------------------
label niam_alive:
    scene bg campfire
    "Following the decision to aid Niham, Geralt seeks out Astrid once more, this time to discuss the path forward. They convene in a secluded part of the village, where the urgency of their mission can be discussed away from overheard whispers."
    $ astrid_state += 2
    a profile "So, you've chosen the path of mercy for Niham. It's a decision that speaks to the honor I saw in you, Witcher"

    g profile "Mercy has its place, but it's answers we're after. Niham's curse—there's more to it, and she deserves a chance at redemption"

    a "Indeed, and redemption might just lie within our grasp. There's a druid, an elder of deep knowledge and deeper connection to the ancient magics of Skellige. He's secluded, forsaken society for the whispers of the forest and the sea"

    g "An elder druid? Sounds like the sort we need. But will he help us? And does he know the ritual to break Niham's curse?"

    a "His help won't come easily. He's a man of principles, living by the old ways. But if anyone can break the curse, it's him. We'll need to convince him of the justice in our cause, of the balance it will restore"

    jump druid_2
    
# -----------------------------------PART 4.2 -----------------------------------------------------------------

label niam_dead:
    scene bg campfire

    $ astrid_state -= 2
    "Their dialogue lays the groundwork for the next phase of the journey, emphasizing the themes of justice, balance, and the power of ancient magics. Astrid's guidance not only provides Geralt with a new ally in the quest to save Niham but also deepens the bond between them, united by a shared commitment to righting the wrongs of the past."

    "After Geralt makes the grave decision to end Niham's suffering, he meets with Astrid again to report the outcome. Their meeting is tinged with a somber air, reflective of the heavy choice made."

    a profile "You've made your choice, Witcher. The siren's song has been silenced. Was there truly no other way?"

    g profile "It was a decision not made lightly. But in the end, it was mercy—freeing her from a curse she could never escape"

    a "I understand the weight of such decisions, even if I wish it could have been different. What's done is done. We must now look to the future and the safety of Skellige"

    "The conversation reflects the complexity of the choices faced in the Witcher's world, where the line between right and wrong is often blurred."

    jump jarl_final_niham_dead

# -----------------------------------PART 5 -----------------------------------------------------------------


label druid_2:
    scene bg skellige_clan
    "In the heart of an ancient forest, Geralt and Astrid find themselves before the elder druid, a figure as much a part of the land as the trees and stones that surround him. The air is alive with the hum of ancient magic, a palpable tension that speaks to the power and danger of the ritual they seek."

    "Druid" "The ritual you seek treads upon sacred ground, Witcher. The site is old, older than the clans, older than the legends that whisper through Skellige's winds"

    g profile "I'm aware of the risks. But if there's a chance to save Niham, to undo the wrongs done to her, it's a path I must consider"

    "Druid" "Consider well, for the magic bound in that place is wild, untamed. To invoke it is to risk not just your own fate but that of the land itself. The spirits guard it fiercely; their wrath is not lightly incurred"

    a profile "And what of Niham? What becomes of her if we turn away from this chance?"

    "Druid" "Her fate then lies in the hands of the gods, or at the edge of your blade. The choice is a heavy burden, one that carries the weight of consequences far beyond our own lives"

    g "If the land turns against me, if the people of Skellige see me as a desecrator, so be it. The chance to mend a broken soul, to restore balance—this is the essence of a Witcher's path"

    "The elder druid nods, an understanding passing between them, a recognition of the sacrifices made in the pursuit of a greater good."

    "Druid" "Then go forth, with my warning in your heart. The site lies deep within the Gedyneith forest, shrouded by enchantments. Only with the purest intent may you pierce its veil"

    "Author" "The decision lays bare before Geralt: to risk the ire of Skellige and the ancient spirits for a chance at redemption, or to choose a safer path, leaving the siren to her fate. The choice is not just about the fate of one siren but speaks to the very nature of the Witcher's journey—walking the line between the dark and the light, making choices that weigh heavily upon the soul."

    menu:
        "perform the ritual":
            $ ritual = True
            $ niham_state = "normal"
            jump ritual # status: performed, scene of ritual
        "to kill the siren":
            $ niham_state = "dead"
            $ astrid_state -= 3
            jump jarl_final_niham_dead
    
    label ritual:
        scene bg ritual

        "Under the ancient canopy of the forest, Geralt stands within a circle of runes, his voice steady as he begins the incantation"

        g profile "Ancient spirits of the wood, hear my plea, bend the weave of fate, release what is bound, and return what was taken"

        "His words, laced with the power of old magic, resonate through the grove, causing the air to shimmer with ethereal energy"

        "Astrid, watching from the edge, mutters under her breath"

        a profile "Be cautious, Witcher. The spirits are listening, and they demand respect"

        "As Geralt continues, the ground pulses, and a faint, luminous fog envelops the clearing. He raises a vial containing a drop of Niham's blood, mixed with the essence of rare herbs, and releases it into the air. The concoction dissolves into a spectral light, weaving through the trees, seeking the grove's heart."

        g "Spiritus elementum, ad me veni, curam da, vincula rumpi"

        "Geralt intones, the ancient language flowing like water, commanding the elements to aid in their quest for redemption"

        scene bg ritual_evil

        "Author" "The ritual's climax is marked by a surge of power, the grove responding with a low, mournful groan. The vibrant life force that once animated the sacred site begins to wane, leaves turning a sickly shade, a sign of the grove's desecration."

        "Astrid steps forward, her voice filled with awe and concern"

        a "The curse is lifted, but at what cost? The grove mourns its own vitality now."

        "Geralt, his gaze lingering on the fading beauty around them, responds with a heavy heart"

        g "The balance has been shifted. We've achieved our aim, but the spirits exacted their price. We must live with the consequences of our actions, however unintended."

        "Author" "As they leave the sacred site, the once vibrant grove stands a testament to the ritual's success and its somber toll. The air is still, filled with the echo of a promise kept and the sorrow of a sanctuary lost."


# -----------------------------------PART 6 -----------------------------------------------------------------

label niham_back:
    scene bg niham_trap
    "Following the potent ritual within the ancient forest, Geralt and Astrid return to where Niham, the siren, awaits, her fate hanging in the balance of the magic they've unleashed. As they draw near, the transformation is palpable. Niham, once a figure of sorrow and vengeance, now radiates a serene grace, her voice echoing the tranquil depths of the sea it once belonged to."

    n normal "The chains that bound my spirit, my voice, they dissolve into the ether. I am reborn, yet not as I once was. This gift of freedom, it's more than I dared hope for"

    "Her voice, crystalline and melodious, fills the air with the purity of her regained essence. Geralt, witnessing the siren's transformation, feels the weight of their actions — a burden lifted, a soul unchained."

    g profile "Your freedom is deserved, Niham. The curse was a shackle no being should bear. But now, we must address the shadows of the past. The Jarl's deeds, hidden in darkness, must be brought to light."

    "Niham's gaze meeting the moon's glow, begins to unravel the tale of deceit and ambition that led to her curse. Her words paint a vivid picture of the Jarl — a man driven by a hunger for power so profound that it led him to curse love itself, to turn it into a weapon of manipulation and control."
    
    n "The Jarl, cloaked in the guise of righteousness, saw in my love a threat to his ascendancy. He twisted our bond, using it to forge my curse, to cement his throne. His fear of losing power turned him into a monster, one who would drown his own blood in the sea of his ambitions"

    "Astrid, absorbing every word, realizes the depth of the betrayal that has poisoned their land. The Jarl's actions, once shrouded in secrecy, now lay bare before them, a truth as chilling as the northern winds."

    a profile "Such treachery cannot stand. The Jarl's fear of losing power has brought nothing but pain and suffering to our shores. We must confront him, expose his deeds to the clans. Justice must be served, not just for Niham, but for all of Skellige"

    "Author" "Their resolve hardens, a shared determination to right the wrongs inflicted by the Jarl's ambition. The journey ahead is fraught with peril, a path that could change the fate of Skellige forever. Yet, in this moment of revelation, Geralt, Astrid, and Niham stand united, bound by a quest for truth and justice in the face of corruption and deceit."


# -----------------------------------PART 7 -----------------------------------------------------------------

label jarl_final:
    scene bg talk_with_jarl
    "A rugged landscape, the sea crashes against cliffs with relentless force. GERALT and ASTRID approach the Jarl's hall, determination etched on their faces"

    "The hall is grand, adorned with relics of Skellige's rich history. JARL BJORN sits upon his throne, a false air of confidence surrounding him. He smiles as Geralt and Astrid enter, mistaking their presence as a simple formality of reporting back"

    j "Witcher, I trust the siren's song has been silenced?"

    "Geralt locks eyes with the Jarl, his gaze unwavering"

    g profile "The siren's tale told more than you bargained for, Jarl. About love twisted into betrayal. About a curse born from your ambition."

    "The Jarl's smile fades, replaced by a flicker of fear. Astrid steps forward, her voice resonant and strong"

    a profile "Skellige deserves the truth. Your reign of lies ends now."

    "The Jarl stands, attempting to assert his authority, but his voice betrays his panic"

    j "You dare challenge your Jarl? Your words are treason!"

    "Geralt draws a step closer, his voice low but filled with power"

    g "We dare because justice demands it. You cursed Niham, caused untold suffering, all for power"

    "Silence hangs heavy. The Jarl looks around, realizing his guards won't save him from the truth"

    j "That not a sicret that power could be built on the blood, but look around."
    j "Does those people suffer? With me Skellige had returned its glory!"
    j "Tough lands required same Jarl, how you couldn't get it? Or you think that little naive girl could do the same?"
    j "I know who are you Geralt. Politic is not for the witchers, you have done great job, and you deserve the reward, so name it: Gold? Titles?"

    "Geralt turns to Astrid, giving her the lead. She looks around at the assembled crowd, their faces a mix of shock and anger"

    a "We want justice. Right Gerald?"

    menu:
        "Accept the Jarl's Reward":
            $ astrid_state -= 1
            jump reward # jarl status: reward

        "Reveal His Secret to the People and let them decide":
            $ astrid_state += 1
            $ jarl = "revealed"
            jump reveal # jarl status: reveal
        "Kill Him":
            $ jarl = "dead"
            jump kill # jarl status: killed
    
    label reward:
        "In the dimly lit hall of Jarl Bjorn, Geralt and Astrid stand firm, their resolve unwavering despite the turmoil that brought them here. Geralt's voice breaks the heavy silence"

        g profile " are here for the reward you promised."

        "The Jarl, a mix of relief and suspicion in his eyes, nods to a servant who brings forth a chest. The clink of gold echoes, a stark reminder of the price of silence in the face of injustice. As they accept the chest, their exchange is terse, the air charged with unspoken truths. "

        "Geralt's gaze lingers on the Jarl, a silent vow that though the gold may weigh down their pockets, it does not tip the scales of justice. Astrid's eyes meet Geralt's, a shared understanding that this gold does not cleanse the Jarl's sins nor does it bind their tongues forever. "

        "They turn to leave, the weight of the gold a heavy reminder of the compromise made, a momentary peace bought at the cost of a deeper silence."
    
    label reveal:
        g profile "People of Skellige, we've been bound by a lie. The danger that threatened us wasn't just the siren, but a betrayal from within"

        a profile "The Jarl, whom we trusted with our lives, used dark magic for his gain, at the cost of innocent lives."

        j "These accusations are baseless! You'd take the word of outsiders over your Jarl?"

        g "We have proof. The siren, Niham, was cursed because of a love the Jarl saw as a threat to his power. A love he destroyed"

        j "What proof do you  have? How can people trust these words?"

        a "We seek no power or favor. Only justice. Let the thing decide. Let every voice be heard, and the truth be the judge"

    label kill:
        "In the dimly lit hall, tension coils like a serpent. Geralt and Jarl Bjorn stand apart, the air between them charged with the inevitable clash of justice against treachery."

        g profile "Your reign of deceit ends now, Jarl. Skellige will be free of your corruption"

        j "You think you can judge me, Witcher? I am the Jarl. I am the law here!"

        a profile "You were the law. Now, you're nothing but a traitor to your people"

        "Jarl Bjorn, with desperation sharpening his movements, draws his sword—a gleaming blade that has never known honor. Geralt meets his gaze, the finality of this moment reflected in his eyes."

        g "This is your last chance. Surrender and face judgment, or..."

        j "I will never bow to the likes of you!"

        "The Jarl lunges, driven by fury, but Geralt, ever the master of the dance of death, parries and strikes. The fight is brutal but brief; the Jarl's skills are no match for the Witcher's."

        "With a final, decisive move, Geralt ends the Jarl's tyranny. As Bjorn falls, the hall falls silent, the weight of the moment settling on all present."

        g "Let this be a new beginning for Skellige. May your leaders be just, and your will strong"


    jump Epilog


label jarl_final_niham_dead:
    
    scene bg talk_with_jarl

    "Geralt and Astrid stand before JARL BJORN, the air thick with tension. The hall is dimly lit, shadows dancing across the Jarl's face as he regards them with a mix of anticipation and wariness."

    j "The siren, Niham... I trust the matter is resolved?"

    g profile "The siren will no longer trouble Skellige. She's been dealt with."

    "The Jarl's eyes narrow, searching Geralt's face for a hint of deception, but finds none"

    j "And what of her accusations? Her... tales of my involvement?"

    a profile "We found no evidence to support her claims against you. Skellige's peace has been restored, at a heavy price."

    "The Jarl relaxes slightly, though the weight of his deeds lingers in the air."

    j "Then you shall have your reward, Witcher. Skellige is in your debt."

    "Geralt accepts, his mind heavy with the moral complexity of their choices. As they turn to leave, Astrid whispers to Geralt, a promise hanging between them."

    "Author" "The truth of the Jarl's deeds may never be known to all, but we will watch. Should he falter, should injustice arise again, we will be there."

    "Author" "They exit the hall, leaving the Jarl to his throne and his secrets. Outside, the wind carries the faintest echo of a siren's lament, a reminder of the price of peace and the shadows that lurk beneath the surface of justice."

    # jarl status: reward
# -----------------------------------Epilog -----------------------------------------------------------------

label Epilog:

    if astrid_state < 0:
        $ astrid_epilogue = "After all the events Astrid has been through in this short time, she has become too disillusioned with the injustice of the world she lives in. So she sadly put aside her dreams of leadership and changes."
    elif astrid_state == 0:
        $ astrid_epilogue = "The witch's arrival taught Astrid that the world is full of both good and evil that lurks in every heart. Justice is not for the peoples of Skellige, now the young warrior realized it and decided to go to a Big Land, in search of a new life."
    elif astrid_state > 0:
        $ astrid_epilogue = "Astrid has found proof of what she herself believes - justice will always win out. She was able to find the courage and determination to become the head of her clan and prove to Skellige that she deserves the best."

    # cursed, dead, normal
    if niham_state == "dead":
        $ niham_epilogue = "Niamh was another victim of 'forbidden' love, and an example of which there are many in history. She had to take her story and secrets to the bottom of the ocean."
    elif niham_state == "normal":
        $ niham_epilogue = "The Witcher was able to save Niamh's body by breaking her curse and giving her back her voice. She may have been half monster, but she was also half human, with a human heart capable of love, and that was worth fighting for."

    # True False
    if ritual:
        $ ritual_epilogue = "The desecration of Skellige's sacred sites could not go unnoticed and the people hated Geralt for the price the inhabitants had to pay. "

    # alive, dead, reward, revealed
    if jarl == "alive":
        $ jarl_epilogue = "Jarl Skellige remained in power and continued to rule these lands, if he had any secrets they remained undiscovered."
    elif jarl == "dead":
        $ jarl_epilogue = "Jarl Skellige paid with his life for the way he achieved power. Unfortunately, this has led to more instability among the clans, and God only knows what tomorrow holds for the people."
    elif jarl == "reward":
        $ jarl_epilogue = "Jarl Skellige remained in power and continued to rule these lands, if he had any secrets they remained undiscovered."
    elif jarl == "revealed":
        $ jarl_epilogue = "Jarl Skellige remained in power and continued to rule these lands, despite the secrets he kept, the people decided that this was not the greatest price to pay for a ruler who was able to deal with the Skellige people and lead the lands to dawn."

    scene bg astrid_epilogue
    "[astrid_epilogue]"

    scene bg niham_epilogue
    "[niham_epilogue]"

    scene bg ritual_epilogue
    "[ritual_epilogue]"

    scene bg jarl_epilogue
    "[jarl_epilogue]"

    scene bg end
    "But now Geralt of Rivia has to go further into his wanderings, in search of a new contract, because in these troubled times, there is always a job for a witcher."

return 