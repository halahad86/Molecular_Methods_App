import re

"""
 To solve:
 
 1) Generate all of the possible permutation for every enzyme slices
 
 2) Iterate over all of the combinations of permutations
 
 3) If answer found update the currently held slices and exit the loop
"""


def solve(slices, names, assigments):
    permsA = []
    permsB = []
    permsC = []

    permGen(len(slices[0]), slices[0], permsA)
    permGen(len(slices[1]), slices[1], permsB)
    permGen(len(slices[2]), slices[2], permsC)

    for currA in permsA:
        for currB in permsB:
            for currC in permsC:
                temp = [currA, currB, currC]
                if posFinder(temp, names, assigments):
                    del slices[:]
                    slices.append(temp[0])
                    slices.append(temp[1])
                    slices.append(temp[2])
                    return True
    return False

###############################################################################

"""
 Determine if a there is a possible solution with the current permutations
 by trying to find positions for the slices to occupy and if there is an
 possible arxrangement then update the assignments
"""


def posFinder(slices, names, assigments):
    isPoss = False
    noSec = len(slices[2])

    takenA = []
    takenB = []

    if posGen(0, 0, noSec, slices, takenB, takenA):
        isPoss = posGen(1, 1, noSec, slices, takenA, takenB)

    if isPoss:
        assigments[2] = []
    for i in xrange(0, len(takenA)):
        assigments[2].insert(takenA[i], names[0])

    for i in xrange(0, len(takenB)):
        assigments[2].insert(takenB[i], names[1])

    return isPoss


###############################################################################

def posGen(start, enzymeType, noSec, slices, takenPrev, takenCurr):
    posSol = True
    point = 0
    offset = 0
    currDis = 0
    curr = start

    while offset <= noSec and posSol and point < len(slices[enzymeType]):
        currDis += slices[2][(offset + start) % noSec]
        if currDis > slices[enzymeType][point]:
            posSol = False
        elif currDis == slices[enzymeType][point] and takenPrev.count(curr) == 0:
            currDis = 0
            takenCurr.append(curr)
            curr = (offset + 1 + start) % noSec
            point += 1
        offset += 1
    return posSol

###############################################################################

"""
 Generate all of the permutations for a list by using Heap's Algorithm.
"""


def permGen(N, objects, permList):
    if (N == 0):
        permList.append(list(objects))
        return

    for c in xrange(0, N):
        permGen(N - 1, objects, permList)
        if (N % 2 == 0):
            temp = objects[c]
            objects[c] = objects[N - 1]
            objects[N - 1] = temp
        else:
            temp = objects[0]
            objects[0] = objects[N - 1]
            objects[N - 1] = temp


###############################################################################



def findAns(size, Enzyme1, Enzyme2, Enzyme3):
    # Holds the sizes of each segment and the owner of the segment
    slices = [[], [], []]
    assigment = [[], [], []]
    currSizes = [0, 0, 0]
    names = []



    # Set up the lists to be read to receive the data.


    """
      This is where the current size of each map is held to help to speed
      up checking for missing values due to duplicates
     """

    """

      get the values from the arguments

    """

    data = [Enzyme1.split(":"), Enzyme2.split(":"), Enzyme3.split(":")]

    names = [data[0][0][0], data[1][0][0], data[0][0][0] + " + " + data[1][0][0]]

    for i in xrange(3):
        for k in xrange(1, len(data[i])):
            temp = int(data[i][k])
            slices[i].append(temp)
            currSizes[i] += temp
            assigment[i].append(names[i])

    passed = False
    possibleMovesLeft = True

    """
    Track the location of additions add location to each base for
    backtracking
    """

    dupAdded = [[], [], []]

    pos = [0, 0, 0]

    """
     Keep looping till all potential moves have been exhausted or till a
     solution has been found
    """

    while possibleMovesLeft:
        """
	     Try to find duplicates by adding in any sections that fit into
	     the spare space when these section are removed then the process
	     to find a new section to fit into the gap starts from position
	     n+1 where n is piece removed. The process is repeated for every
	     map
	    """
        for i in xrange(0, 3):
            for t in xrange(pos[i], len(slices[i])):
                if size >= currSizes[i] + slices[i][t]:
                    slices[i].insert(t, slices[i][t])
                    currSizes.insert(i, currSizes.pop(i) + slices[i][t])
                    dupAdded[i].append(t)
                if size == currSizes[i]:
                    break;

        """

	    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	    CAN THIS BE MADE NICER??????????????????????

	    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	    Test to ensure that every base is completely full and that the
	    number of segments add up then try to solve else remove the last
	    added segment and reset the start position of any preceding base.
	    """
        if (size == curSize for curSize in currSizes) and (len(slices[2]) == len(slices[0]) + len(slices[1])) and solve(
                slices, names, assigment):
            passed = True
            possibleMovesLeft = False
        else:
            if not len(dupAdded[0]):
                if not len(dupAdded[1]):
                    if not len(dupAdded[2]):
                        possibleMovesLeft = False
                    else:
                        newpos = dupAdded[2].pop()
                        currSizes.insert(2, currSizes.pop(2) - slices[2].pop(newpos))
                        pos[2] = newpos + 1
                        pos[0] = pos[1] = 0
                else:
                    newpos = dupAdded[1].pop()
                    currSizes.insert(1, currSizes.pop(1) - slices[1].pop(newpos))
                    pos[1] = newpos + 1
                    pos[0] = 0
            else:
                newpos = dupAdded[0].pop()
                currSizes.insert(0, currSizes.pop(0) - slices[0].pop(newpos))
                pos[0] = newpos + 1

    """
      Check to see if a solution is found and display appropriate message.
     """
    if not passed:
        return ("NoSol")
    else:
        ans = ""
        for i in xrange(3):
            for k in xrange(len(slices[i])):
                ans = ans + assigment[i][k] + "," + str(slices[i][k]) + ","
            ans = ans[:-1] + ":"
        ans = ans[:-1]
        return ans 

