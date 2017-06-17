from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take"
	
    next = raw_input("> ")
    if int() in next:
        how_much = int(next)
    else:
	    dead("man, learn to type a number")
		
    if how_much < 50:
        print "nice your not greedy u win"
        exit(0)
    else:
	    dead("greedy bstard")
		
		
def bear_room():
    print "there is a bear here"
    print " the bear has lot of honey"
    print "the fat ber is in front of another door"
    print "hoow do u move dis bear"
    bear_moved = False
	
    while True:
	    next = raw_input("> ")
		
	    if next == "take honey":
		    dead("the bear looks at you and slaps u")
	    elif next == "taunt bear" and not bear_moved:
		    print "the bear has moved from the door, u can go through"
		    bear_moved = True
	    elif next == "taunt bear" and bear_moved:
		    dead("the bear get angry and eats ur leg")
	    elif next == "open door" and bear_moved:
		    gold_room()
	    else:
		    print "i got no idea what that means"
			
		
def cthulhu_room():
    print "here u see the great evil Cthulhu"
    print "he stares at u and u go insane"
    print "do u flee, or eat ur own head"
    
    next = raw_input("> ")
	
    if "flee" in next:
        start()
    elif "head" in next:
        dead("that was tasty")
    else:
	    cthulhu_room()
		

def dead(why):
    print why, "good job"
    exit(0)
	
def start():
    print "you are in a dark room"
    print "there is a door to your right and left"
    print "which one do u take"
	
    next = raw_input("> ")
	
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
	    dead("u stumble around and starve")
		

start()
