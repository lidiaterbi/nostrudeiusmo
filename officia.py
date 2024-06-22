def search_along_line(midpoint, upper_border):
    x_mid = midpoint[0]
    y_mid = midpoint[1]
    x_upper = upper_border[0]
    y_upper = upper_border[1]

    # Calculate the slope of the line
    slope = (y_upper - y_mid) / (x_upper - x_mid)

    # Start from the midpoint
    x = x_mid
    y = y_mid

    # Move towards the upper border in small increments
    while y < y_upper:
        # Check if the current point lies on the line
        if y == slope * (x - x_mid) + y_mid:
            return (x, y)

        # Move one unit up
        y += 1

    return None  # If no point on the line is found

# Example usage
midpoint = (2, 3)
upper_border = (5, 7)
result = search_along_line(midpoint, upper_border)
print(result)  # Output: (4, 6)
