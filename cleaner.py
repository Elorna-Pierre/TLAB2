
#Filter out non-digit values and return a list of intergers
def filter_nondigits(data: list) -> list: 
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    heart_rate_data=[] #Create empty list to store digits
    for digit in data:
        if digit.strip().isdigit(): #Confirm value is a digit
            heart_rate_data.append(int(digit.strip())) #Convert valye into interger and return to list
    return heart_rate_data #Return a list of digits


#Filter out outlier values within the min_value to max_value range
def filter_outliers(data:list, min_value=30, max_value=250)-> list:
    """
    Filter out outlier of the min_value to max_value range

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all outlier strings removed
    """
    heart_rate_data=[] #Create empty list to store values
    for digit in data: #Loop through each value 
        if min_value < digit < max_value: #Check each value to see if it is within the range
            heart_rate_data.append(digit) #Add new values to the list
    return heart_rate_data #Return a list of values within range

