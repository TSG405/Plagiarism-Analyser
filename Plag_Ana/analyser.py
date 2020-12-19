import time
import re
import math

# Main Function..
def plag_ana():

    unique = []    
    print("\n------------------------------------------------------------\n ----***---- Welcome to the PLAGIARISM ANALYSER ----***----\n------------------------------------------------------------\n ")
    
    text = input("\nEnter your text: \t")
    user_input = text.lower()

    query = re.sub("[^\w]"," ",user_input).split()

    for t in query:
        if t not in unique:
            unique.append(t)
    
    # Parsing the database of list of words [sample]
    sample = open("sample.txt", "r") 
    da = sample.read().lower()
    
    database = re.sub("[^\w]", " ",da).split()

    for t in database:
        if t not in unique:
            unique.append(t)

    t_array1 = []
    t_array2 = []
    mult = 0
    
    for word in unique:
        t_array1Counter = 0
        t_array2Counter = 0

        for tt in query:
            if tt == word:
                t_array1Counter += 1
        t_array1.append(t_array1Counter) 

        for tt in database:
            if tt == word:
                t_array2Counter += 1
        t_array2.append(t_array2Counter)


    for i in range (len(t_array1)):
        mult += t_array1[i] * t_array2[i]


    Vectordatabase = 0
    for i in range (len(t_array2)):
        Vectordatabase += t_array2[i]**2
    Vectordatabase = math.sqrt(Vectordatabase)
    
    
    Vectorquery = 0
    for i in range (len(t_array1)):
        Vectorquery += t_array1[i]**2
    Vectorquery = math.sqrt(Vectorquery)


    result = ((float)(mult / (Vectorquery * Vectordatabase)) * 100)
    
    print("\nPlease Wait...")
    time.sleep(3)
    
    if result>=70.0:
        print("!! WARNING: !!Plagiarized!! [HIGH], analysed percentage: ({}) % ".format(result))
    elif result<70.0 and result>=30.0:
        print("!!Plagiarized!! [MEDIUM], analysed percentage: ({}) % ".format(result))
    elif result<30.0 and result>0.0:
        print("!!Plagiarized!! [LOW], analysed percentage: ({}) % ".format(result))
    else:
        print("!! GOOD TO GO !! analysed percentage: ({}) % ".format(result))


# Driver Code
p=0
while 1:    
    if (p==0):
        plag_ana()
    p=1
    bb=input("\nWant to analyse again?? please press [Y/N] :\t ")
    if (bb.lower() == 'yes' or bb.lower() =='y'):
        plag_ana()
    elif (bb.lower() =='no' or bb.lower() =='n'):
        print("\n !THANK YOU!  ~ TSG405")
        break
    else:
        print("\n!INVALID INPUT! Please try again!")
        
              
@ CODED BY TSG405, 2020
