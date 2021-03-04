'''
Mad Libs Generator
--------------------------
'''

loop = 1
while(loop < 10):
    
# All the question that program asks the user

    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word):")
    noun3 = input("Choose a noun: ")
    
# Displays story based on user input

    print("------------------------------")
    print("be kind to your {} - footed {}".format(noun,p_noun))
    print("For a duck may be somebody's {}, ".format(noun2))
    print ("Be kind to your {} in {}".format(p_noun,place))
    print ("Where the weather is always {},".format(adjective))
    print ()
    print ("You may think that is this the {},".format(noun3))
    print ("Well it is.")
    print ("------------------------------------------")

# Loop back to "loop=1"
    loop = loop+1

