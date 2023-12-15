startPos = [1, 0]
homePos = [2, 3]
rowCosts = [5, 4, 3]
colCosts = [8, 2, 6, 7]


def minimumCostHomecomingCorrected(startPos, homePos, rowCosts, colCosts):
    startrow, startcol = startPos
    homerow, homecol = homePos

    # Calculate the cost for row movement
    # The robot starts at 'startrow', so we begin summing from the next row
    row_movement_cost = 0
    if startrow < homerow:
        row_movement_cost = sum(rowCosts[startrow + 1:homerow + 1])
    elif startrow > homerow:
        row_movement_cost = sum(rowCosts[homerow:startrow])

    # Calculate the cost for column movement
    # The robot starts at 'startcol', so we begin summing from the next column
    col_movement_cost = 0
    if startcol < homecol:
        col_movement_cost = sum(colCosts[startcol + 1:homecol + 1])
    elif startcol > homecol:
        col_movement_cost = sum(colCosts[homecol:startcol])

    # The total cost is the sum of row movement cost and column movement cost
    total_cost = row_movement_cost + col_movement_cost

    return total_cost

# Re-test with the provided case
minimum_cost_corrected = minimumCostHomecomingCorrected(startPos, homePos, rowCosts, colCosts)
print(minimum_cost_corrected)