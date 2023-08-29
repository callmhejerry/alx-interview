#!/usr/bin/python3

'''LOCK BOXES'''


def canUnlockAll(boxes):
    """A function that checks of all the boxes
    in boxes can be opened. returns true if it can
    otherwise return false
    """
    all_keys = []
    closed_boxes = []

    for i in range(len(boxes)):
        box = i

        if box != 0:
            if box in all_keys:
                # open the box and retrieve all the keys
                all_keys.extend(boxes[box])
                if len(closed_boxes) > 0:
                    check_closed_boxes(closed_boxes, all_keys, boxes)
            else:
                closed_boxes.append(box)
        else:
            # Add all keys gotten to all keys array
            all_keys.extend(boxes[i])

    return len(closed_boxes) == 0


def check_closed_boxes(closed_boxes, keys, boxes):
    """Check closed boxes and add the keys of
    the closed box if it can be opened
    """
    for key in keys:
        for box in closed_boxes:
            if key == box:
                keys.extend(boxes[box])
                closed_boxes.remove(box)
