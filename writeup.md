## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

- There may be missing values or “NO SIGNAL” entries in this dataset because of a user error or connection interference while running the device. By filtering these values risks can include  the loss of important information needed to piece clues together.
  

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

- In this context, the standard deviation in heart rate data measures change. With this information, we can determine whether or not an individual's heart rate is healthy and consistent.


## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

- The x-axis in this context represents time and it provides the changes over time in the heart rate. The heart rate either increases or decreases depending on the activity of the subject. An increasing heart rate can indicate exercise while a decrease can indicate rest.

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

- Yes, the average heart rate line graph measures the different time intervals while standard deviation measures the variability of the heart rate. Together the graph measures the stability of the heart rate over a period of time.

