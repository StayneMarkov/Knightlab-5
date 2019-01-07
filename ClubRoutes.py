def msg(room):
    if room['msg']=='':
        return "You have entered " +room['name']+" ."
    else:
        return room['msg']

def get_choice(room,dire):
    if dire=='N':
        choice=0
    elif dire=='E':
        choice=1
    elif dire=='S':
        choice=2
    elif dire=='W':
        choice=3
    else:
        return -1

    if room['directions'][choice]==0:
        return 4
    else:
        return choice



def club():
    dirs =(0,0,0,0)
    London={"name":"London","directions":dirs,"msg":''}
    Emirates={"name":"The Emirates","directions":dirs,"msg":''}
    Stamford_Bridge={"name":"Stamford Bridge","directions":dirs,"msg":''}
    Wembley={"name":"Wembley","directions":dirs,"msg":''}
    Anfield={"name":"Anfield","directions":dirs,"msg":''}
    Old_Trafford={"name":"Old Trafford","directions":dirs,"msg":''}
    Etihad={"name":"Etihad","directions":dirs,"msg":''}

    #NESW
    London["directions"]=(Wembley,Emirates,0,Stamford_Bridge)
    Emirates["directions"]=(Old_Trafford,0,0,London)
    Stamford_Bridge["directions"]=(Anfield,London,0,0)
    Wembley["directions"]=(0,Old_Trafford,London,Anfield)
    Anfield["directions"]=(0,Wembley,Stamford_Bridge,0)
    Old_Trafford["directions"]=(0,Etihad,Emirates,Wembley)
    Etihad["directions"]=(0,0,0,Old_Trafford)

    room=London
    print ("Hello. Welcome to EPL.")

    epl = True
    while epl:
           dire = input("Which direction would you like to go? Press N for North, S for South, E for East and W for West. Type quit if you want to quit")
           if dire=="quit":
               print ("Thank you for seeing EPL")
               break;
           else:
               choice=get_choice(room,dire)
               if choice == -1:
                   print("Please enter N,S,E,W")
               elif choice ==4:
                   print("You cannot go into that direction")
               else:
                   room=room['directions'][choice]
                   print (msg(room))
                   
                   
club()
