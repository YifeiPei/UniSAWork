# Blckjack simulation
# Python version 3.4, however it shoud work in Python 2.7 as well

# Exercise 1 by Yifei Pei


import random

##################################################
# You have to change only this function. 
# Try not to ruin other code :-)

# I give number to the functions depending on there results
# e.g. the best result function is named player_decision1, then player_decision2 ...
# For unknown reason, I initial function got the best result
# My second best function is the modified basic strategy which is calculating probability
# Perhaps my understanding of the basic strategy had some errors
# This is the first attempt for my submission
# If I got some better idea, I will submit a second time before the deadline
# Or this is going to be my final assignment

# The original function
# For unknown reason, this is my best result function when I make it <12
def player_decision2(player_hand, dealer_hand, deck):
    if counting(player_hand) < 12:
        return("one more")
    else:
        return("stop")

# The function based on the basic strategy on forum
# From my running result, this one isn't better than the last one
def player_decision3(player_hand, dealer_hand, deck):
    
    #If the dealer's up card is 7 or higher 
    if counting(dealer_hand) >= 7:
        #continue to draw cards until you have a soft count of 18 or higher
        if 11 in player_hand:
            while counting(player_hand) < 18:
                return ("one more")
        else:
            #continue to draw cards until you have a hard count of at least 17 
            while counting(player_hand) < 17:
                return ("one more")
    #If the dealer's up card is 6 or lower,  
    if counting(dealer_hand) <= 6:
        #draw cards until you have at least 12. Stop when you have 12 or higher.
        while counting(player_hand) <12:
            return ("one more")
        #return ("stop")
    return ("stop")

# This is the final one I made to combine the basic strategy with probability calculating
# This one is defnitely better than the last function, but still not better than the first one
def player_decision(player_hand, dealer_hand, deck):
    
    #calculating the probability for all cards
    TwoPro = (deck.count(2))/(len(deck))
    ThrPro = (deck.count(3))/(len(deck))
    FouPro = (deck.count(4))/(len(deck))
    FivPro = (deck.count(5))/(len(deck))
    SixPro = (deck.count(6))/(len(deck))
    SevPro = (deck.count(7))/(len(deck))
    EigPro = (deck.count(8))/(len(deck))
    NinPro = (deck.count(9))/(len(deck))
    TenPro = (deck.count(10))/(len(deck))
    ElePro = (deck.count(11))/(len(deck))
    
    if counting(dealer_hand) >= 7:
        if 11 in player_hand:
            while counting(player_hand) < 18:
                if counting(player_hand) <12:
                    return ("one more")
                else: #if the count>=12 the system will compare the probability for the player
                    if counting(player_hand) == 12:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+ElePro) > TenPro:
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 13:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+ElePro) > (NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 14:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+ElePro) > (EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 15:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) > (SevPro+EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 16:
                        if (TwoPro+ThrPro+FouPro+FivPro+ElePro) > (SixPro+SevPro+EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 17:
                        if (TwoPro+ThrPro+FouPro+ElePro) > (FivPro+SixPro+SevPro+EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
        
        else:
            while counting(player_hand) < 17:
                if counting(player_hand) <12:
                    return ("one more")
                else: #The same as the previous chunk
                    if counting(player_hand) == 12:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+ElePro) > TenPro:
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 13:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+ElePro) > (NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 14:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+ElePro) > (EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 15:
                        if (TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) > (SevPro+EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
                    if counting(player_hand) == 16:
                        if (TwoPro+ThrPro+FouPro+FivPro+ElePro) > (SixPro+SevPro+EigPro+NinPro+TenPro):
                            return("one more")
                        else:
                            return("stop")
     
    if counting(dealer_hand) <= 6:
        while counting(player_hand) <12:
            return ("one more")
    
    return ("stop")

# This strategy is based on our discussion on forum that only calculate the probability on player side
# The result is the worst one. Then I realised I cannot only count on player side
# Depending on this result, I added the dealer side analysis for the last function
# The last function is a modification for the basic strategy. Perhaps my implementation has some errors
# I really do not know why my basic strategy and modified basic strategy are not better than <12 strategy
def player_decision4(player_hand, dealer_hand, deck):
    
    #calculating the probability for all cards
    TwoPro = (deck.count(2))/(len(deck))
    ThrPro = (deck.count(3))/(len(deck))
    FouPro = (deck.count(4))/(len(deck))
    FivPro = (deck.count(5))/(len(deck))
    SixPro = (deck.count(6))/(len(deck))
    SevPro = (deck.count(7))/(len(deck))
    EigPro = (deck.count(8))/(len(deck))
    NinPro = (deck.count(9))/(len(deck))
    TenPro = (deck.count(10))/(len(deck))
    ElePro = (deck.count(11))/(len(deck))
    
    #print(TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro+ElePro)
    
    if counting(player_hand) < 12:
        return("one more")
    else: #if the winning probability is larger, the player will hit
        if counting(player_hand) == 12:#[2,3,4,5,6,7,8,9,11] will fit 12 better than 10
            if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+ElePro) > TenPro:
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 13:#[2,3,4,5,6,7,8,11] will fit 13 better than [9,10]
            if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+ElePro) > (NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 14:#[2,3,4,5,6,7,11] will fit 14 better than [8,9,10]
            if (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+ElePro) > (EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 15:#[2,3,4,5,6,11] will fit 15 better than [7,8,9,10]
            if (TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) > (SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 16:#[2,3,4,5,11] will fit 16 better than [6,7,8,9,10]
            if (TwoPro+ThrPro+FouPro+FivPro+ElePro) > (SixPro+SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 17:#[2,3,4,11] will fit 17 better than [5,6,7,8,9,10]
            if (TwoPro+ThrPro+FouPro+ElePro) > (FivPro+SixPro+SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 18:#[2,3,11] will fit 18 better than [4,5,6,7,8,9,10]
            if (TwoPro+ThrPro+ElePro) > (FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 19:#[2,11] will fit 19 better than [3,4,5,6,7,8,9,10]
            if (TwoPro+ElePro) > (ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        if counting(player_hand) == 20:#[11] will fit 20 better than [2,3,4,5,6,7,8,9,10]
            if ElePro > (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro):
                return("one more")
            else:
                return("stop")
        return("stop")
        
# This is an additional part I made after seeing the discussion on forum that
# To calculate the average and add it to both sides
# From my testing, average will not work better, as it is a constant value that
# do not change variables
# Finally I made this function based on probabilities for different cases
# I still cannot figure out why the (<12) function is the best result
# My best result so far is the player_decision1 with 46% chance of win
# Second is still the player_decision2 with 45% chance of win
# The function below is the third best result with 44% chance of win
# which is equal to the basic strategy function and better than
# my own probability on one side 43% chance of win

# Honestly, it seems quite weird running on my computer, because on the forum
# It says that the basic strategy can win 48%
# Also my function below did not count the conditions with soft or hard at the very beginning
# However, I do not have that motivation to do it as my brain is messed up now

def player_decision1(player_hand, dealer_hand, deck):
    
    #average = sum(deck)/len(deck)
    #print (average)
    
    #calculating the probability for all cards
    TwoPro = (deck.count(2))/(len(deck))
    ThrPro = (deck.count(3))/(len(deck))
    FouPro = (deck.count(4))/(len(deck))
    FivPro = (deck.count(5))/(len(deck))
    SixPro = (deck.count(6))/(len(deck))
    SevPro = (deck.count(7))/(len(deck))
    EigPro = (deck.count(8))/(len(deck))
    NinPro = (deck.count(9))/(len(deck))
    TenPro = (deck.count(10))/(len(deck))
    ElePro = (deck.count(11))/(len(deck))
    
    if counting(player_hand) < 12:
        return("one more")
    else:
        if counting(dealer_hand) < counting(player_hand):
            return(player_decision4(player_hand, dealer_hand, deck))
        else:
            
            # counting(player_hand == 12)
            if (counting(dealer_hand) == 13) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+ElePro) < NinPro) & (NinPro > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 14) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+ElePro) < (EigPro+NinPro)) & ((EigPro+NinPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 15) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) < (NinPro+SevPro+EigPro)) & ((NinPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 16) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+FouPro+FivPro+ElePro) < (NinPro+SixPro+SevPro+EigPro)) & ((NinPro+SixPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 17) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+FouPro+ElePro) < (NinPro+FivPro+SixPro+SevPro+EigPro)) & ((NinPro+FivPro+SixPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 12):
                if ((TwoPro+ThrPro+ElePro) < (NinPro+FouPro+FivPro+SixPro+SevPro+EigPro)) & ((NinPro+FouPro+FivPro+SixPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 12):
                if ((TwoPro+ElePro) < (NinPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro)) & ((NinPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 12):
                if (ElePro < (NinPro+TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro)) & ((NinPro+TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro) > TenPro):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 13
            elif (counting(dealer_hand) == 14) & (counting(player_hand) == 13):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+ElePro) < EigPro) & (EigPro > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 15) & (counting(player_hand) == 13):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) < (SevPro+EigPro)) & ((SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 16) & (counting(player_hand) == 13):
                if ((TwoPro+ThrPro+FouPro+FivPro+ElePro) < (SixPro+SevPro+EigPro)) & ((SixPro+SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 17) & (counting(player_hand) == 13):
                if ((TwoPro+ThrPro+FouPro+ElePro) < (FivPro+SixPro+SevPro+EigPro)) & ((FivPro+SixPro+SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 13):
                if ((TwoPro+ThrPro+ElePro) < (FouPro+FivPro+SixPro+SevPro+EigPro)) & ((FouPro+FivPro+SixPro+SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 13):
                if ((TwoPro+ElePro) < (ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro)) & ((ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 13):
                if (ElePro < (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro)) & ((TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro) > (NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 14
            elif (counting(dealer_hand) == 15) & (counting(player_hand) == 14):
                if ((TwoPro+ThrPro+FouPro+FivPro+SixPro+ElePro) < SevPro) & (SevPro > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 16) & (counting(player_hand) == 14):
                if ((TwoPro+ThrPro+FouPro+FivPro+ElePro) < (SixPro+SevPro)) & ((SixPro+SevPro) > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 17) & (counting(player_hand) == 14):
                if ((TwoPro+ThrPro+FouPro+ElePro) < (FivPro+SixPro+SevPro)) & ((FivPro+SixPro+SevPro) > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 14):
                if ((TwoPro+ThrPro+ElePro) < (FouPro+FivPro+SixPro+SevPro)) & ((FouPro+FivPro+SixPro+SevPro) > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 14):
                if ((TwoPro+ElePro) < (ThrPro+FouPro+FivPro+SixPro+SevPro)) & ((ThrPro+FouPro+FivPro+SixPro+SevPro) > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 14):
                if (ElePro < (TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro)) & ((TwoPro+ThrPro+FouPro+FivPro+SixPro+SevPro) > (EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 15
            elif (counting(dealer_hand) == 16) & (counting(player_hand) == 15):
                if ((TwoPro+ThrPro+FouPro+FivPro+ElePro) < SixPro) & (SixPro > (SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 17) & (counting(player_hand) == 15):
                if ((TwoPro+ThrPro+FouPro+ElePro) < (FivPro+SixPro)) & ((FivPro+SixPro) > (SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 15):
                if ((TwoPro+ThrPro+ElePro) < (FouPro+FivPro+SixPro)) & ((FouPro+FivPro+SixPro) > (SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 15):
                if ((TwoPro+ElePro) < (ThrPro+FouPro+FivPro+SixPro)) & ((ThrPro+FouPro+FivPro+SixPro) > (SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 15):
                if (ElePro < (TwoPro+ThrPro+FouPro+FivPro+SixPro)) & ((TwoPro+ThrPro+FouPro+FivPro+SixPro) > (SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 16
            elif (counting(dealer_hand) == 17) & (counting(player_hand) == 16):
                if ((TwoPro+ThrPro+FouPro+ElePro) < FivPro) & (FivPro > (SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 16):
                if ((TwoPro+ThrPro+ElePro) < (FouPro+FivPro)) & ((FouPro+FivPro) > (SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 16):
                if ((TwoPro+ElePro) < (ThrPro+FouPro+FivPro)) & ((ThrPro+FouPro+FivPro) > (SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 16):
                if (ElePro < (TwoPro+ThrPro+FouPro+FivPro)) & ((TwoPro+ThrPro+FouPro+FivPro) > (SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 17
            elif (counting(dealer_hand) == 18) & (counting(player_hand) == 17):
                if ((TwoPro+ThrPro+ElePro) < FouPro) & (FouPro > (FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 17):
                if ((TwoPro+ElePro) < (ThrPro+FouPro)) & ((ThrPro+FouPro) > (FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 17):
                if (ElePro < (TwoPro+ThrPro+FouPro)) & ((TwoPro+ThrPro+FouPro) > (FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 18
            elif (counting(dealer_hand) == 19) & (counting(player_hand) == 18):
                if ((TwoPro+ElePro) < ThrPro) & (ThrPro > (FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 18):
                if (ElePro < (TwoPro+ThrPro)) & ((TwoPro+ThrPro) > (FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            # counting(player_hand) == 19
            elif (counting(dealer_hand) == 20) & (counting(player_hand) == 19):
                if (ElePro < TwoPro) & (TwoPro > (ThrPro+FouPro+FivPro+SixPro+SevPro+EigPro+NinPro+TenPro)):
                    return ("one more")
                else:
                    return ("stop")
            
            
            else:
                return("stop")

##################################################
# Other useful functions

def deck_shuffling(N):
    house = (2,3,4,5,6,7,8,9,10,10,10,10,11)
    deck = list(house * 4 * N)
    random.shuffle(deck)
    return(deck)
    
def draw_card(deck):
    card = deck.pop(random.sample(range(len(deck)), 1)[0])
    return(card)
    
def counting(hand):
    counts = sum(hand)
    for i in range(hand.count(11)):
        if counts > 21:
            counts = counts - 10
        else:
            break
    return(counts)

def compare_hands(dealer_hand, player_hand):
    player_count = counting(player_hand)
    dealer_count = counting(dealer_hand)
    
    #print (player_count, dealer_count)
    
    if player_count == dealer_count:
        return(0.5)
    elif player_count > dealer_count: 
        return(1)
    else: 
        return(0)


##################################################
# Parameters. You can try to play with different parameters.

N = 4                # number of decks 
num_games = 1000000    # number of games

##################################################
# Working code. Probably you should not change anything here

deck = deck_shuffling(N)
outcome = 0

for g in range(num_games):
    dealer_hand = [draw_card(deck)]
    player_hand = [draw_card(deck), draw_card(deck)]
    
    while player_decision(player_hand, dealer_hand, deck) == "one more" and counting(player_hand) <= 21:
        player_hand.append(draw_card(deck))
    else:
        if counting(player_hand) <= 21: 
            while counting(dealer_hand) <= 17:
                dealer_hand.append(draw_card(deck))
            else:
                if counting(dealer_hand) > 21:
                    result = 1
                else:
                    result = compare_hands(dealer_hand, player_hand)                
        else:
            result = 0

    #print (counting(player_hand), counting(dealer_hand))
    outcome = outcome + result
    
    if len(deck) < N * 26:
        deck = deck_shuffling(N)

print("Your player won %s games out of total %s games" % (str(outcome), str(num_games)))




