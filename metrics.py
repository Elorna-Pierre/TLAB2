

import statistics

def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    if  not data or n <= 0: #Check if list is empty or if n is valid
        return []
    return [max(data[x:x + n]) #Create a list of maximum values
            for x in range(0, len(data), n)]


def window_average(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of average values from each window)
    """
    if not data or n < 0: #Check if list is empty or if n is valid
        return []
    return [sum(data[x:x + n]) / len(data[x:x + n]) #calculate the averages of n
            for x in range(0, len(data), n)]



def window_stddev(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of standard deviations from each window (size should be len(data)//6)
    """
    if not data or n <= 1 or n > len(data): #Check if list is empty or if n is valid
        return [] #Create list to store each window size
    if n == 1:
        return []

    result = [] #List to store standard deviations for each window

    for x in range(0,len(data), n):
        window = data[x:x + n]
        if len(window) < n: # Disregard windows with no complete data
            break
        stddev = round(statistics.stdev(window),2) #Calculate and round the standard deviation of the window

        result.append(stddev)
    
        
    return result
    