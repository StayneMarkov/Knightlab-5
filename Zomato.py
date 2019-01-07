size = input("Enter the size of the cafe: ")
prox = input("Enter the proximity of the place from  the centre: ")
place= input("Enter the nearest well known place: ")
st_name=input("Enter the starter: ")
mocktail=input("Enter the mocktail: ")
foodadj=input("Enter an adjective relating to food (good or bad): ")
cookadj=input("Enter an adjective relating to the cooking: ")
drinkadj=input("Enter an adjective for the mocktail: ")
mainc=input("Enter the main course: ")
stdout=input("Enter the standout from the main course: ")
foodadj2=input("Enter an adjective for the standout factor: ")
dessert=input("Enter the dessert ordered: ")
foodadj3=input("Enter an adjective to describe the dessert: ")
adj=input("Enter an adjective to explain the experience: ")
food=input("Enter food rating out of 5: ")
ambi=input("Enter ambience rating out of 5: ")
service=input("Enter the service rating out of 5: ")

with open("zom.txt",'w') as zomat:
    print ("This was a " +size+ " cafe situated in the " +prox+ " of " +place+ ". We ordered the " +st_name+ " as starter and " +mocktail+ ".The " +st_name+ " was "+foodadj+ " and "
           +cookadj+". The drink was " +drinkadj+ ".We then requested " +mainc+ ".The " +stdout+ " was " +foodadj2+ ". As dessert, we ordered "+dessert+". It was "+foodadj3+
           ".Overall a " +adj+ "experience.      Food: " +food+ "/5    Ambience: " +ambi+ "/5    Service: " +service+ "/5" , file=zomat) 
