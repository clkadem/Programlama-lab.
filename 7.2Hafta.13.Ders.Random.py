import random

def rollDie():
    r=random.choice([1,2,3,4,5,6])
    return r

def rollN(n):
    result=''
    for i in range(n):
        result=result+str(rollDie())+" "
print(rollN(10))

def flip(numFlipps):
    heads=0
    for i in range(numFlipps):
        if(random.choice(('H','T'))=='H'):
            heads+=1

    return heads/numFlipps
print(flip(5))

def flipsim(numFlipPerTrial,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipPerTrial))
        mean=sum(fracHeads)/len(fracHeads)
    return mean

print(flipsim(10,1))

def flipPlot(minExp,maxExp):
    ratios,diffs,xAxis=[],[],[]
    for exp in range(minExp,maxExp+1):#
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads=0
        for i in range(numFlips):
            if(random.choice(('H','T'))=='H'):
                numHeads+=1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads / numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
       # pylab.title('Difference Between Heads and Tails')
       # pylab.xlabel('Number of Flips')
       # pylab.ylabel('Abs(#Heads - #Tails)')
       # pylab.plot(xAxis, diffs, 'k')
       # pylab.figure()
       # pylab.title('Heads/Tails Ratios')
       # pylab.xlabel('Number of Flips')
       # pylab.ylabel('#Heads/#Tails')
       # pylab.plot(xAxis, ratios, 'k')

random.seed(0)
flipPlot(4, 20)