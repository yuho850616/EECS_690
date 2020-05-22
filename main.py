from __future__ import division
from itertools import chain


def isfloat(value): # to check the data is number or not
  try:
    float(value)
    return True
  except ValueError:
    return False

def Diff(li1, li2): # to get the difference of the two lists
    return (list(set(li1) - set(li2)))

def intersection(lst1, lst2): # to get the intersection of two lists
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def Remove(duplicate): # remove the duplicate value
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def Cutpoint(removearray): # to find the cutpoint of the two values
    cutpointlist = []
    removearray = sorted(removearray)
    for i in range(len(removearray)-1):
        cutpointlist.append((removearray[i]+removearray[i+1])/2)
    cutpointlist.append(removearray[0])
    cutpointlist.append(removearray[len(removearray)-1])
    cutpointlist = sorted(cutpointlist)
    return(cutpointlist)

def intersect(*d):
    sets = iter(map(set, d))
    result = sets.next()
    for s in sets:
        result = result.intersection(s)
    return result

def main():
    #use 2D LIST TO read the file
    array2D = []
    attributename = []
    print("Please input the input data file name")
    filename = input()
    with open(filename, 'r') as f:
        list1 = [str(word) for word in f.readline().split()]
        list2 = [str(word) for word in f.readline().split()] # attributename
        for line in f.readlines():
            line = line.strip()
            array2D.append(line.split())
    numrow = len(array2D)
    numcol = len(array2D[0])
    list2.pop(0) #remove [
    list2.pop()  #remove ]
    list2.pop()  #remove decisionname

    # use 2d list to read the attribute value we want(flip the array2D)
    # test.txt example[['0.8', '0.8', '0.8', '1.2', '1.2', '2.0', '2.0'], ['0.3', '1.1', '1.1', '0.3', '2.3', '2.3', '2.3'], ['7.2', '7.2', '10.2', '10.2', '10.2', '10.2', '15.2'], ['very-small', 'small', 'medium', 'medium', 'medium', 'high', 'very-high']]
    lists = []
    for i in range (numcol):
        lists.append([])
    for i in range(numcol):
        for j in range(numrow):
         lists[i].append(array2D[j][i])
    cutpointornot1 = isfloat(lists[0][0])
    cutpointornot2 = isfloat(lists[1][0])
    cutpointornot3 = cutpointornot1 and cutpointornot2




    if(cutpointornot3 == True): #if the data is number do mlem2 cutpoint first

        # newlists are the float type of lists
        newlists = []
        for i in range (numcol-1):
            newlists.append([])
        for i in range(numcol-1):
            for j in range(numrow):
                newlists[i].append(float(lists[i][j]))

        floatlists = []
        for i in range (numcol-1):
            floatlists.append([])
        for i in range(numcol-1):
            for j in range(numrow):
                floatlists[i].append(float(lists[i][j]))

        for i in range(numcol-1):
            #remove duplicate value in the lists
            #test.txt example[0.8, 1.2, 2.0]
            #                [0.3, 1.1, 2.3]
            #                [7.2, 10.2, 15.2]
            newlists[i] = Remove(newlists[i])
            #find the cutpoint in the lists
            #test.txt example
            # [0.8, 1.0, 1.6, 2.0]
            # [0.3, 0.7000000000000001, 1.7, 2.3]
            # [7.2, 8.7, 12.7, 15.2]
            newlists[i] = Cutpoint(newlists[i])

        totalavnum = 0;
        for i in range(numcol-1):
            totalavnum = totalavnum + (2*(len(newlists[i])-2))

        #to store the attribue list
        avlist = []# for attribute cutpoint sets
        for i in range (totalavnum):
            avlist.append([])

        #example in test.txt [[1, 2, 3], [4, 5, 6, 7], [1, 2, 3, 4, 5], [6, 7], [1, 4], [2, 3, 5, 6, 7], [1, 2, 3, 4], [5, 6, 7], [1, 2], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6], [7]]

        avequaltlist = []
        #exmaple in test.txt ['A,0.8..1.0', 'A,1.0..2.0', 'A,0.8..1.6', 'A,1.6..2.0', 'B,0.3..0.7000000000000001', 'B,0.7000000000000001..2.3', '0.3..1.7', '1.7..2.3', '7.2..8.7', '8.7..15.2', '7.2..12.7', '12.7..15.2']
        x=0
        for i in range(numcol-1):
            max = (len(newlists[i])-1)
            for j in range(len(newlists[i])-2):
                str0 = list2[i]
                stra = ","
                str1 = (str(newlists[i][0]))
                str2 = ".."
                str3 = str(newlists[i][j+1])
                str4 = str0 + stra + str1 + str2 +str3
                avequaltlist.append(str4)
                for a in range(numrow):
                    if(newlists[i][j+1]>floatlists[i][a]):
                        avlist[x].append(a+1)
                x+=1
                str9 = list2[i]
                str10 = ","
                str5 = str(newlists[i][j+1])
                str6 = ".."
                str7 = (str(newlists[i][max]))
                str8 = str9 + str10 + str5 + str6 + str7
                avequaltlist.append(str8)
                for a in range(numrow):
                    if(newlists[i][j+1]<floatlists[i][a]):
                        avlist[x].append(a+1)
                x+=1

        originalavlist = []
        for i in range (totalavnum):
            originalavlist.append(avlist[i])


        decisionlists = []
        for i in range (len(lists[numcol-1])):
             decisionlists.append(lists[numcol-1][i])
        originaldecisionlists = [] # have all the decision variable
        for i in range (len(lists[numcol-1])):
            originaldecisionlists.append(lists[numcol-1][i])
        decisionlists = Remove(decisionlists)
        B = [] #decision sets
        for i in range (len(decisionlists)):
            B.append([])
            B[i].append(decisionlists[i])
        for i in range (numrow):
            for j in range (len(B)):
                if lists[numcol-1][i]==B[j][0] :
                    B[j].append(i+1)
        #decisionlists test.txt example ['very-small', 'small', 'medium', 'high', 'very-high']

        originalB = []
        for i in range (len(decisionlists)):
            originalB.append(B[i])


        #lem2 following the pseudo code on handout
        decisionrule = []
        [j.pop(0) for j in B]
        intersectionlist = []
        intersectionindexlist = []
        for i in range (len(B)): #[[1,2,3],[4,5][6,7,8]] 0-2
            update = []
            G = B[i]
            while(len(G)!=0):#[[1,2,3],[4,5][6,7,8]]
                T = []
                intersectionlist = []
                for j in range(len(avlist)):#[[1,3][2,4][5,8][6][7][1,2,5][3,4][6,7,8][1,3,5][2,6][4,7,8]]
                    intersectionlist.append(intersection(avlist[j],G))
                count = 0
                cardinalityintersection = []
                while((len(T)==0 or all(x in B[i] for x in cardinalityintersection)==False)):
                    maxindex = 0
                    maxintersection = intersectionlist[0]
                    for k in range(len(avlist)):
                        if(len(maxintersection)<len(intersectionlist[k])):
                            maxintersection = intersectionlist[k]
                            maxindex = k
                        elif(len(maxintersection)==len(intersectionlist[k])):
                            if(len(avlist[maxindex])<=len(avlist[k])):
                                maxintersection = intersectionlist[k]
                                maxindex = maxindex
                            else:
                                maxintersection = intersectionlist[k]
                                maxindex = k
                    if(count==0):
                        cardinalityintersection = avlist[maxindex]
                        T.append(maxindex)
                    else:
                        cardinalityintersection = intersection(cardinalityintersection,avlist[maxindex])
                        T.append(maxindex)
                    count += 1
                    G = maxintersection
                    for j in range(len(avlist)):#[[1,3][2,4][5,8][6][7][1,2,5][3,4][6,7,8][1,3,5][2,6][4,7,8]]
                        intersectionlist[j]= intersection(avlist[j],G)

                    for y in T:
                        intersectionlist[y].clear()
                car = []
                s = 0
                if(len(T)>1):
                    while(s != len(T)):
                        temp = s
                        tempvalue = T[s]
                        T.pop(s)
                        for j in range(len(T)):
                            if(j==0):
                                car = avlist[T[j]]
                            else:
                                car = intersection(car,avlist[T[j]])
                        if(all(x in B[i] for x in car)== False):
                            T.insert(temp,tempvalue)
                            s+=1
                        else:
                            s=0
                decisionrule.append(decisionlists[i])
                intersectionindexlist.append(T)
                for x in range (len(cardinalityintersection)):
                    update.append(cardinalityintersection[x])
                G = Diff(B[i],update)

        print("Please input the output data file name")#output the file
        filename = input()
        outFile = open(filename, 'w')
        k = 0
        for i in range (len(intersectionindexlist)):
            outFile.write("\n")
            for j in range (len(intersectionindexlist[i])):
                outFile.write("(")
                outFile.write(str(avequaltlist[intersectionindexlist[i][j]]))
                outFile.write(")")
                if(j<len(intersectionindexlist[i])-1):
                    outFile.write("&")
                else:
                    outFile.write("->")
                    outFile.write("(Decision, ")
                    outFile.write(decisionrule[k])
                    outFile.write(")")
                    k += 1

    else:
        totalelements = 0
        newlists = []
        for i in range (numcol-1):
            newlists.append(lists[i])
        for i in range(numcol-1):
            newlists[i]= Remove(newlists[i])#remove duplicate attribute values
            totalelements = totalelements + len(newlists[i])
        flatten_list = list(chain.from_iterable(newlists))
        avlist = []# for attribute cutpoint sets
        for i in range (totalelements):
            avlist.append([])

        a = 0
        for i in range (len(lists)-1):
            for j in range(len(newlists[i])):
                for k in range(len(lists[i])):
                    if(newlists[i][j]==lists[i][k]):
                        avlist[a].append(k+1)
                a+=1

        originalavlist = []
        for i in range (totalelements):
            originalavlist.append(avlist[i])

        decisionlists = []
        for i in range (len(lists[numcol-1])):
             decisionlists.append(lists[numcol-1][i])
        originaldecisionlists = [] # have all the decision variable
        for i in range (len(lists[numcol-1])):
            originaldecisionlists.append(lists[numcol-1][i])
        decisionlists = Remove(decisionlists)
        B = [] #decision sets
        for i in range (len(decisionlists)):
            B.append([])
            B[i].append(decisionlists[i])
        for i in range (numrow):
            for j in range (len(B)):
                if lists[numcol-1][i]==B[j][0] :
                    B[j].append(i+1)
        originalB = []
        for i in range (len(decisionlists)):
            originalB.append(B[i])

        outputlist = []
        for i in range(len(newlists)):
            for j in range(len(newlists[i])):
                str1 = list2[i]
                str2 = ','
                str3 = newlists[i][j]
                str4 = str1 + str2 + str3
                outputlist.append(str4)

        decisionrule = []
        [j.pop(0) for j in B]
        intersectionlist = []
        intersectionindexlist = []
        for i in range (len(B)): #[[1,2,3],[4,5][6,7,8]] 0-2
            update = []
            G = B[i]
            while(len(G)!=0):#[[1,2,3],[4,5][6,7,8]]
                T = []
                intersectionlist = []
                for j in range(len(avlist)):#[[1,3][2,4][5,8][6][7][1,2,5][3,4][6,7,8][1,3,5][2,6][4,7,8]]
                    intersectionlist.append(intersection(avlist[j],G))
                count = 0
                cardinalityintersection = []
                while((len(T)==0 or all(x in B[i] for x in cardinalityintersection)==False)):
                    maxindex = 0
                    maxintersection = intersectionlist[0]
                    for k in range(len(avlist)):
                        if(len(maxintersection)<len(intersectionlist[k])):
                            maxintersection = intersectionlist[k]
                            maxindex = k
                        elif(len(maxintersection)==len(intersectionlist[k])):
                            if(len(avlist[maxindex])<=len(avlist[k])):
                                maxintersection = intersectionlist[k]
                                maxindex = maxindex
                            else:
                                maxintersection = intersectionlist[k]
                                maxindex = k
                    if(count==0):
                        cardinalityintersection = avlist[maxindex]
                        T.append(maxindex)
                    else:
                        cardinalityintersection = intersection(cardinalityintersection,avlist[maxindex])
                        T.append(maxindex)
                    count += 1
                    G = maxintersection
                    for j in range(len(avlist)):#[[1,3][2,4][5,8][6][7][1,2,5][3,4][6,7,8][1,3,5][2,6][4,7,8]]
                        intersectionlist[j]= intersection(avlist[j],G)

                    for y in T:
                        intersectionlist[y].clear()
                car = []
                s = 0
                if(len(T)>1):
                    while(s != len(T)):
                        temp = s
                        tempvalue = T[s]
                        T.pop(s)
                        for j in range(len(T)):
                            if(j==0):
                                car = avlist[T[j]]
                            else:
                                car = intersection(car,avlist[T[j]])
                        if(all(x in B[i] for x in car)== False):
                            T.insert(temp,tempvalue)
                            s+=1
                        else:
                            s=0

                decisionrule.append(decisionlists[i])
                intersectionindexlist.append(T)
                for x in range (len(cardinalityintersection)):
                    update.append(cardinalityintersection[x])
                G = Diff(B[i],update)

        k = 0
        print("Please input the output data file name")
        filename = input()
        outFile = open(filename, 'w')
        for i in range (len(intersectionindexlist)):
            outFile.write("\n")
            for j in range (len(intersectionindexlist[i])):
                outFile.write("(")
                outFile.write(str(outputlist[intersectionindexlist[i][j]]))
                outFile.write(")")
                if(j<len(intersectionindexlist[i])-1):
                    outFile.write("&")
                else:
                    outFile.write("->")
                    outFile.write("(Decision, ")
                    outFile.write(decisionrule[k])
                    outFile.write(")")
                    k += 1


if __name__ == "__main__":
    main()
