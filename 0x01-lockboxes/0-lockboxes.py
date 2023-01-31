#!/usr/bin/python3
'''Lockboxes interview'''


def canUnlockAll(boxes):
    '''Checks if all the boxes can be unlocked

    Args:
        boxes (list): list of boxes

    Returns:
        'true' if all the boxes can be opened and 'false' otherwise
    '''
    keys = set(boxes[0])  # Converted to a set to prevent repeat keys
    keys.add(0)

    loop = 1

    # Loops through list of boxes every time a box is opened
    while loop <= len(boxes):
        newkeys = []  # Contains keys found in this loop
        for i in keys:
            try:
                for j in boxes[i]:
                    newkeys.append(j)
            except IndexError:
                pass
        # Adds new keys to key set
        for i in newkeys:
            keys.add(i)
        loop += 1

    if all(i in list(keys) for i in list(range(len(boxes)))):
        return True
    else:
        return False
