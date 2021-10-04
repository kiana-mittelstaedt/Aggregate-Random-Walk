import random

def ranWalk(n):
    
    pos = 0                          # initialize position at principal node
    posList = [0]                    # create list of active nodes
    coinToss = 0                     # tracker for num of coin tosses

    while True:
        num = random.randint(0,1)    # "flip a coin" 
        coinToss += 1                # accumulate tosses

        if num == 0:                 # if flip heads
            pos += 1                 # move one to the right
            if pos > max(posList):   # if new positive node reached
                posList.append(pos)  # add new node to list
                pos = 0              # reset to principal node
                
        else:                        # if flip tails
            pos -= 1                 # move one to the left 
            if pos < min(posList):   # if new negative node reached
                posList.append(pos)  # add new node to list
                pos = 0              # reset to principal node
                
        if len(posList) == n:        # if n nodes are active
            break

    return [min(posList),max(posList),coinToss]


def mcRanWalk(trials,n):

    output = []                      # initialize list to collect tuples
    result = {}                      # initialize dict to store frequencies          
    tossList = []                    # initialize list to collect total tosses
    
    for i in range(trials):          
        trial = ranWalk(n)           # run number of specified trials using ranWalk fn
        numToss = trial.pop()        # pop number of tosses from fn output
        tossList.append(numToss)     # add number or tosses to new list
        output.append(tuple(trial))  # add ending pos result to list as a tuple

    for endPos in output:            # iterate over tuples in output list
        if endPos in result.keys():  # create a dictionary to capture frequencies
            result[endPos] += 1      # of end positions 
        else:
            result[endPos] = 1

    print(result)
    print(sum(tossList)/len(tossList))
