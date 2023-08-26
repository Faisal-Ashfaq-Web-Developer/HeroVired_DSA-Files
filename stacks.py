################## Stack #############################
#points: add an element, retrieve an elements, search an elements, delete an elements.

# sourcery skip: merge-list-append
stackList = []

def stackAddElement(Listname, element):
    Listname.append(element)

def stackRetrieveElement(Listname):
    items = Listname[len(Listname) - 1]
    Listname.pop()
    return items

stackAddElement(stackList, 13)
stackAddElement(stackList, 23)
stackAddElement(stackList, 33)
stackAddElement(stackList, 43)
stackAddElement(stackList, 53)
stackAddElement(stackList, 63)
stackAddElement(stackList, 73)

print(stackList)
items = stackRetrieveElement(stackList)
print(items)
print(stackList)

def searchandRetrieve(stackName, element):
    newStack = []
    flag = 0
    for index in range(len(stackName)-1, -1, -1):
        if (stackName[index] == element):
            flag = 1
            stackRetrieveElement(stackList)
            return index

        else:
            if (flag == 0):
                stackAddElement(newStack, stackName[index])
                print("newstack", newStack)
                stackRetrieveElement(stackList)


index = searchandRetrieve(stackList, 53)
print(stackList)
print(index)
