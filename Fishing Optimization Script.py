import csv
import itertools

#Create the empty data structure to store values in later
#Will follow the pattern [Combination, Fish Caught per Hour, Value per Hour, Time Spent Recasting per Hour, Time Spent Cooking per Hour]
data = [[0] * 5 for _ in range(59049)]


# Generate a list of ternary tuples with length z
z = 10
digits = list(itertools.product(range(3), repeat=z))


#Define function to convert tuples into strings
def str_tuple(tup):
    return ''.join([str(i) for i in tup])


#Assign the 59,049 combinations to the corresponding 'Combination' slot in our data structure
for i in range (59049):
    data[i][0] = str_tuple(digits[i])


#Assign Odds Variables
oddsSplashtail = 0.5
oddsBaseNormal = 0.16
oddsBaseTrophy = 0.04
oddsCommonNormal = 0.1
oddsCommonTrophy = 0.025
oddsUncommonNormal = 0.06666
oddsUncommonTrophy = 0.01666
oddsRareNormal = 0.00666
oddsRareTrophy = 0.00166
oddsNightNormal = 0.06666
oddsNightTrophy = 0.01666

#Assign Time Variables
timeRecast = 23.5
timeCatchNormal = 94.5
timeCatchTrophy = 142.8
timeCookNormal = 40
timeCookTrophy = 90

#Assign Value Variables (Currently filled out for Ancientscales, Plentifins, Wildsplashes, and Devilfish)
goldBaseNormalRaw = 225
goldBaseNormalCooked = 340
goldBaseTrophyRaw = 565
goldBaseTrophyCooked = 850

goldCommonNormalRaw = 300
goldCommonNormalCooked = 450
goldCommonTrophyRaw = 750
goldCommonTrophyCooked = 1125

goldUncommonNormalRaw = 375
goldUncommonNormalCooked = 565
goldUncommonTrophyRaw = 940
goldUncommonTrophyCooked = 1410

goldRareNormalRaw = 3000
goldRareNormalCooked = 4500
goldRareTrophyRaw = 7500
goldRareTrophyCooked = 11250

goldNightNormalRaw = 300
goldNightNormalCooked = 450
goldNightTrophyRaw = 750
goldNightTrophyCooked = 1125


#Simulate every possible combination of ignoring, catching, and cooking
for i in range (59049):

    #Based on the current combination, discover which fish are going to be ignored, caught, or caught and cooked and assign relevant time/gold values
    
    #Base Normal
    if data[i][0][0] == "0":
        timeBaseNormal = timeRecast
        goldBaseNormal = 0
    elif data[i][0][0] == "1":
        timeBaseNormal = timeCatchNormal
        goldBaseNormal = goldBaseNormalRaw
    elif data[i][0][0] == "2":
        timeBaseNormal = (timeCatchNormal + timeCookNormal)
        goldBaseNormal = goldBaseNormalCooked

    #Base Trophy
    if data[i][0][1] == "0":
        timeBaseTrophy = timeRecast
        goldBaseTrophy = 0
    elif data[i][0][1] == "1":
        timeBaseTrophy = timeCatchTrophy
        goldBaseTrophy = goldBaseTrophyRaw
    elif data[i][0][1] == "2":
        timeBaseTrophy = (timeCatchTrophy + timeCookTrophy)
        goldBaseTrophy = goldBaseTrophyCooked

    #Common Normal
    if data[i][0][2] == "0":
        timeCommonNormal = timeRecast
        goldCommonNormal = 0
    elif data[i][0][2] == "1":
        timeCommonNormal = timeCatchNormal
        goldCommonNormal = goldCommonNormalRaw
    elif data[i][0][2] == "2":
        timeCommonNormal = (timeCatchNormal + timeCookNormal)
        goldCommonNormal = goldCommonNormalCooked

    #Common Trophy
    if data[i][0][3] == "0":
        timeCommonTrophy = timeRecast
        goldCommonTrophy = 0
    elif data[i][0][3] == "1":
        timeCommonTrophy = timeCatchTrophy
        goldCommonTrophy = goldCommonTrophyRaw
    elif data[i][0][3] == "2":
        timeCommonTrophy = (timeCatchTrophy + timeCookTrophy)
        goldCommonTrophy = goldCommonTrophyCooked

    #Uncommon Normal
    if data[i][0][4] == "0":
        timeUncommonNormal = timeRecast
        goldUncommonNormal = 0
    elif data[i][0][4] == "1":
        timeUncommonNormal = timeCatchNormal
        goldUncommonNormal = goldUncommonNormalRaw
    elif data[i][0][4] == "2":
        timeUncommonNormal = (timeCatchNormal + timeCookNormal)
        goldUncommonNormal = goldUncommonNormalCooked

    #Uncommon Trophy
    if data[i][0][5] == "0":
        timeUncommonTrophy = timeRecast
        goldUncommonTrophy = 0
    elif data[i][0][5] == "1":
        timeUncommonTrophy = timeCatchTrophy
        goldUncommonTrophy = goldUncommonTrophyRaw
    elif data[i][0][5] == "2":
        timeUncommonTrophy = (timeCatchTrophy + timeCookTrophy)
        goldUncommonTrophy = goldUncommonTrophyCooked

    #Rare Normal
    if data[i][0][6] == "0":
        timeRareNormal = timeRecast
        goldRareNormal = 0
    elif data[i][0][6] == "1":
        timeRareNormal = timeCatchNormal
        goldRareNormal = goldRareNormalRaw
    elif data[i][0][6] == "2":
        timeRareNormal = (timeCatchNormal + timeCookNormal)
        goldRareNormal = goldRareNormalCooked

    #Rare Trophy
    if data[i][0][7] == "0":
        timeRareTrophy = timeRecast
        goldRareTrophy = 0
    elif data[i][0][7] == "1":
        timeRareTrophy = timeCatchTrophy
        goldRareTrophy = goldRareTrophyRaw
    elif data[i][0][7] == "2":
        timeRareTrophy = (timeCatchTrophy + timeCookTrophy)
        goldRareTrophy = goldRareTrophyCooked

    #Night Normal
    if data[i][0][8] == "0":
        timeNightNormal = timeRecast
        goldNightNormal = 0
    elif data[i][0][8] == "1":
        timeNightNormal = timeCatchNormal
        goldNightNormal = goldNightNormalRaw
    elif data[i][0][8] == "2":
        timeNightNormal = (timeCatchNormal + timeCookNormal)
        goldNightNormal = goldNightNormalCooked

    #Night Trophy
    if data[i][0][9] == "0":
        timeNightTrophy = timeRecast
        goldNightTrophy = 0
    elif data[i][0][9] == "1":
        timeNightTrophy = timeCatchTrophy
        goldNightTrophy = goldNightTrophyRaw
    elif data[i][0][9] == "2":
        timeNightTrophy = (timeCatchTrophy + timeCookTrophy)
        goldNightTrophy = goldNightTrophyCooked


    #Calculate the average cast time for the current combination using a weighted average of relevant times
    avgCastTime = (oddsSplashtail * timeRecast) + (oddsBaseNormal * timeBaseNormal) + (oddsBaseTrophy * timeBaseTrophy) + (oddsCommonNormal * timeCommonNormal) + (oddsCommonTrophy * timeCommonTrophy) + (oddsUncommonNormal * timeUncommonNormal) + (oddsUncommonTrophy * timeUncommonTrophy) + (oddsRareNormal * timeRareNormal) + (oddsRareTrophy * timeRareTrophy) + (oddsNightNormal * timeNightNormal) + (oddsNightTrophy * timeNightTrophy)


    #Calculate the amount of casts per hour by dividing 3600 (seconds per hour) by average cast time
    castsPerHour = 3600 / avgCastTime


    #Calculate how many times each possible outcome will occur in an hour
    numSplashtail = castsPerHour * oddsSplashtail
    numBaseNormal = castsPerHour * oddsBaseNormal
    numBaseTrophy = castsPerHour * oddsBaseTrophy
    numCommonNormal = castsPerHour * oddsCommonNormal
    numCommonTrophy = castsPerHour * oddsCommonTrophy
    numUncommonNormal = castsPerHour * oddsUncommonNormal
    numUncommonTrophy = castsPerHour * oddsUncommonTrophy
    numRareNormal = castsPerHour * oddsRareNormal
    numRareTrophy = castsPerHour * oddsRareTrophy
    numNightNormal = castsPerHour * oddsNightNormal
    numNightTrophy = castsPerHour * oddsNightTrophy


    #Calculate total time spent recasting and cooking in an hour
    #Also set values for ignored fish to 0
    totalRecastTime = 0
    totalCookTime = 0

    #Base Normal
    if data[i][0][0] == "0":
        totalRecastTime += (numBaseNormal * timeRecast)
        numBaseNormal = 0
    elif data[i][0][0] == "2":
        totalCookTime += (numBaseNormal * timeCookNormal)

    #Base Trophy
    if data[i][0][1] == "0":
        totalRecastTime += (numBaseTrophy * timeRecast)
        numBaseTrophy = 0
    elif data[i][0][1] == "2":
        totalCookTime += (numBaseTrophy * timeCookTrophy)
        
    #Common Normal
    if data[i][0][2] == "0":
        totalRecastTime += (numCommonNormal * timeRecast)
        numCommonNormal = 0
    elif data[i][0][2] == "2":
        totalCookTime += (numCommonNormal * timeCookNormal)

    #Common Trophy
    if data[i][0][3] == "0":
        totalRecastTime += (numCommonTrophy * timeRecast)
        numCommonTrophy = 0
    elif data[i][0][3] == "2":
        totalCookTime += (numCommonTrophy * timeCookTrophy)

    #Unommon Normal
    if data[i][0][4] == "0":
        totalRecastTime += (numUncommonNormal * timeRecast)
        numUncommonNormal = 0
    elif data[i][0][4] == "2":
        totalCookTime += (numUncommonNormal * timeCookNormal)

    #Uncommon Trophy
    if data[i][0][5] == "0":
        totalRecastTime += (numUncommonTrophy * timeRecast)
        numUncommonTrophy = 0
    elif data[i][0][5] == "2":
        totalCookTime += (numUncommonTrophy * timeCookTrophy)

    #Rare Normal
    if data[i][0][6] == "0":
        totalRecastTime += (numRareNormal * timeRecast)
        numRareNormal = 0
    elif data[i][0][6] == "2":
        totalCookTime += (numRareNormal * timeCookNormal)

    #Rare Trophy
    if data[i][0][7] == "0":
        totalRecastTime += (numRareTrophy * timeRecast)
        numRareTrophy = 0
    elif data[i][0][7] == "2":
        totalCookTime += (numRareTrophy * timeCookTrophy)

    #Night Normal
    if data[i][0][8] == "0":
        totalRecastTime += (numNightNormal * timeRecast)
        numNightNormal = 0
    elif data[i][0][8] == "2":
        totalCookTime += (numNightNormal * timeCookNormal)

    #Night Trophy
    if data[i][0][9] == "0":
        totalRecastTime += (numNightTrophy * timeRecast)
        numNightTrophy = 0
    elif data[i][0][9] == "2":
        totalCookTime += (numNightTrophy * timeCookTrophy)

    data[i][3] = totalRecastTime + (numSplashtail * timeRecast)
    data[i][4] = totalCookTime

    #Calculate how many fish will be caught in an hour
    totalFish = numBaseNormal + numBaseTrophy + numCommonNormal + numCommonTrophy + numUncommonNormal + numUncommonTrophy + numRareNormal + numRareTrophy + numNightNormal + numNightTrophy
    data[i][1] = totalFish

    #Calculate how much gold will be earned in an hour
    totalGold = (numBaseNormal * goldBaseNormal) + (numBaseTrophy * goldBaseTrophy) + (numCommonNormal * goldCommonNormal) + (numCommonTrophy * goldCommonTrophy) + (numUncommonNormal * goldUncommonNormal) + (numUncommonTrophy * goldUncommonTrophy) + (numRareNormal * goldRareNormal) + (numRareTrophy * goldRareTrophy) + (numNightNormal * goldNightNormal) + (numNightTrophy * goldNightTrophy)
    data[i][2] = totalGold


#Write the compiled data to a csv file
file = open('data.csv', 'w+', newline = '')

with file:
    write = csv.writer(file)
    write.writerows(data)

