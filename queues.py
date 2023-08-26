############# Queue ############
#adding an element #retrieving an element # search and retrieve an element

queueList = []

def queueAddElement(queueName, element):
    queueName.append(element)


def queueRetrieveElement(queueName):
    # sourcery skip: inline-immediately-returned-variable, move-assign-in-block
    items = queueName[0]
    queueName.pop(0)
    return items

queueAddElement(queueList, 14)
queueAddElement(queueList, 24)
queueAddElement(queueList, 34)
queueAddElement(queueList, 44)
queueAddElement(queueList, 54)
queueAddElement(queueList, 64)
queueAddElement(queueList, 74)

print(queueList)
items = queueRetrieveElement(queueList)
print(items)
print(queueList)

def searchandRetrieve(queueName, element):
    # sourcery skip: merge-else-if-into-elif
    newQueue = []
    flag = 0
    for index in range(len(queueName) -1):
        if (queueName[0] == element):
            flag = 1
            queueRetrieveElement(queueList)
            return_index = index

        else:
            if (flag == 0):
                queueAddElement(newQueue, queueName[index])
                print("newQueue", newQueue)
                queueRetrieveElement(queueList)
    queueName = newQueue + queueName
    print(queueName)
    return return_index

index = searchandRetrieve(queueList, 34)
print(queueList)
print(index)