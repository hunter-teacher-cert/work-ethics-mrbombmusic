import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists.

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
Input: a dicitonary containing the number of regular economy seats sold.
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plane
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win"
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing.
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])
    # print("Economy Sold = " + str(economy_sold))

    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat


    if random.randrange(100) > 30: # looking for window seat
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]
        # randomzie it
        random.shuffle(order)
        # print("Looking in row " + str(order[0]))

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win": # left side window seat
                plane[row][0] = name
                # print("here is win seat for " + str(name) + "at left side row " + str(row))
                return plane
            elif plane[row][len(plane[0])-1] == "win": # right side window seat
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    # couldn't find window seat or didnt specifically want a window seat
    r = 0
    c = 1

    #Modified this seating loop to put non-window seat economy-plus in first rows
    while not(found_seat):
        # print("c = " + str(c))
        if plane[r][0] == "win":
            plane[r][c] = name
            found_seat = True
        if plane[r][c] == "avail":
            plane[r][c] = name
            found_seat = True
        if c < len(plane[r]) - 1:
            c += 1
        else:
            r += 1
            c = 1
    return plane


# finds number of empty seats in plane
# used in assign_rows function
def find_empty_seats(plane):
    remaining_seats = {}
    rows = len(plane)
    n = 0
    for row in plane:
        avail_seats = row.count("avail")
        if row[len(row) - 1] == "win":
            avail_seats += 1
        if row[0] == "win":
            avail_seats += 1
        remaining_seats.setdefault(n, avail_seats)
        n += 1
    return remaining_seats

# This function assigns all seats to regular economy passengers after economy plus passengers have been seated
# This function will also utilize swapping and reseating functions below to assure that all blocks of
# regular economy passengers are seated together
def assign_rows(plane, remaining_seats, economy_sold):
    avail_seats_in_row = list(remaining_seats.values())
    num_purchased_seats = list(economy_sold.values())
    num_purchased_seats.sort()
    num_purchased_seats.reverse()
    total_avail = sum(avail_seats_in_row)
    total_needed = sum(num_purchased_seats)
    rc = 0 # remaining_seats counter
    remaining_seats_row = list(remaining_seats.keys())
    sold_seat_name = list(economy_sold.keys())
    sold_seat_name.sort()
    sold_seat_name.reverse()
    while total_needed > 0:
        if avail_seats_in_row[rc] >= num_purchased_seats[0]:
            row = int(remaining_seats_row[rc])
            start = find_first_empty_seat_in_row(plane[row], num_purchased_seats[0])
            for i in range(num_purchased_seats[0]):
                if plane[row][i + start] == "avail" or plane[row][i + start] == "win":
                    plane[row][i + start] = sold_seat_name[0]
            total_avail -= num_purchased_seats[0]
            total_needed -= num_purchased_seats[0]
            avail_seats_in_row[rc] -= num_purchased_seats[0]
            sold_seat_name.pop(0)
            num_purchased_seats.pop(0)
            rc = 0
        elif avail_seats_in_row[rc] < num_purchased_seats[0] and rc == len(plane) - 1:
            eWRows = locate_avail_win_seat(plane)
            eNRows = locate_avail_non_win_seat(plane)
            if len(eWRows) == 0 and len(eNRows) > 0:
                plane = make_avail_block(plane, eNRows, num_purchased_seats[0])
            elif len(eWRows) > 0 and len(eNRows) == 0:
                plane = make_avail_block_win(plane, eWRows, num_purchased_seats[0])
            else:
                plane = win_seat_swap(plane, eWRows, eNRows)
            remaining_seats = find_empty_seats(plane)
            avail_seats_in_row = list(remaining_seats.values())
            remaining_seats_row = list(remaining_seats.keys())
            rc = 0
        else:
            if rc < len(plane) - 1:
                rc += 1
            else:
                rc = 0

# creates a list of all rows with an available window seat
# used in assign_rows function
def locate_avail_win_seat(plane):
    row_with_empty_win_seat = []
    count_row = 0
    for row in plane:
        for i in range(len(row) -1, -1, -1):
            if row[i] == "win":
                row_with_empty_win_seat.append(count_row)
        count_row += 1
    return row_with_empty_win_seat

# creates a list of all rows with an available non-window seat
# used in assign_rows function
def locate_avail_non_win_seat(plane):
    row_with_empty_non_win_seat = []
    count_row = 0
    for row in plane:
        for i in range(len(row) -1, -1, -1):
            if row[i] == "avail":
                row_with_empty_non_win_seat.append(count_row)
        count_row += 1
    return row_with_empty_non_win_seat

#swaps economy plus passenger in window seat to a different window seat
# to make two or more open seats together
def win_seat_swap(plane, empty_win_rows, empty_non_win_rows):
    eWRow = empty_win_rows[0]
    eNRow = empty_non_win_rows[0]
    plane[eWRow][len(plane[eWRow]) -1] = plane[eNRow][len(plane[eNRow]) -1]
    plane[eNRow][len(plane[eNRow]) -1] = "win"
    return plane

# swaps economy plus passenger in non-window seat to a different non-window seat
# to make two or more open seats together
def make_avail_block(plane, empty_nw_row, num_seats):
    full_row = find_full_row(plane)
    for i in range(num_seats):
        avail_seat = plane[empty_nw_row[i]].index("avail")
        plane[empty_nw_row[i]][avail_seat] = plane[full_row][i + 1]
        plane[full_row][i + 1] = "avail"
    return plane

# swaps economy plus passenger in non-window seat to a different window seat
# to make two or more open seats together
def make_avail_block_win(plane, empty_w_row, num_seats):
    full_row = find_full_row(plane)
    for i in range(num_seats):
        avail_seat = plane[empty_w_row[i]].index("win")
        plane[empty_w_row[i]][avail_seat] = plane[full_row][i + 1]
        plane[full_row][i + 1] = "avail"
    return plane

# used in make_avail_block & make_avail_block_win functions
def find_full_row(plane):
    for row in plane:
        for seat in row:
            if not(seat.startswith("e")):
                break
            else:
                return plane.index(row)

#used to locate seat in row to place block of passengers in
# checks to see there are enough seats together to accommodate number of passengers in block
def find_first_empty_seat_in_row(row, num_seats):
    if num_seats == 1:
        for i in range(len(row)):
            if row[i] == "avail" or row[i] == "win":
                    return i
    elif num_seats == 2:
        for i in range(len(row)):
            if row[i] == "avail" or row[i] == "win":
                if row[i + 1] == "avail" or row[i + 1] == "win":
                    return i
    else:
        for i in range(len(row)):
            if row[i] == "avail" or row[i] == "win":
                if row[i + 1] == "avail" or row[i + 1] == "win":
                    if row[i + (num_seats - 1)] == "avail" or row[i + (num_seats - 1)] == "win":
                        return i

def purchase_economy_block(plane,economy_sold,number,name):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    seats_avail = get_total_seats(plane)
    seats_avail = seats_avail - get_number_economy_sold(economy_sold)

    if seats_avail >= number: # if there are more seats available than the number requested
        economy_sold[name]=number
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """
    economy_sold={}
    total_seats = get_total_seats(plane)

    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 30: # Someone wants to buy window seat
            plane = purchase_economy_plus(plane,economy_sold,"ep-%d"%ep_number)
            ep_number = ep_number + 1
            total_seats = get_avail_seats(plane,economy_sold) # reset total_seats to remaining available seats
        else:
            current_block_size = 1+random.randrange(max_family_size)
            if total_seats >= current_block_size: # makes sure flight cannot be oversold
                economy_sold = purchase_economy_block(plane,economy_sold,current_block_size,"u-%d"%u_number)
                u_number = u_number + 1
                total_seats = get_avail_seats(plane,economy_sold)
            else:
                pass

    empty_rows = find_empty_seats(plane)
    assign_rows(plane, empty_rows, economy_sold)
    return plane



def main():
    plane = create_plane(10,5)
    # print(get_plane_string(plane))
    plane = fill_plane(plane)
    print(get_plane_string(plane))
if __name__=="__main__":
    main()
