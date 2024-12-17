# Health Monitoring Data Processing

Now that you've completed the "minimal" CLI App, your next task is to continue this development effort and perform analysis on real heart-rate data. The company you work for, Seng-Links, aims to identify periods when a user sleeps or exercises using their varying recorded heart rates. 

Your company has provided you a data folder (*data/*) of 5 files that contain heart-rate samples from a participant. The participant's device records heart rate data every 5 minutes. This is the sampling rate, the interval at which heart rate data is recorded. Based on their personal data, you are tasked with writing code to determine when this participant is sleeping or exercising.

Like before, your co-worker has managed to complete the framework of this project but now relies on you to complete the rest.

## Instructions

First, to install the `matplotlib` library to your environment, run the following command in your VSCode terminal:

```
pip install matplotlib
```

There are three Python files which you will modify in this repository to complete this project:
* cleaner.py
* metrics.py
* main.py
* writeup.md

The files with the prefix `test_` (i.e. `test_clean.py`, `test_metrics.py`, and `test_run.py`) are intended for you to test your code to ensure that all project requirements are complete. **Do not modify the code in these files. Otherwise, you will not be able to check that your code is functioning correctly.**. 

Once you've completed the coding portion of this project and ensured that all output is correct, you will then provide a writeup in the file ` writeup.md`, where you will answer analytical questions that gauge your statistical thinking.

Further details and usage of each file are listed below: 

**cleaner.py**

This module contains two functions you will implement to clean your list of data. Both functions take in a list. `filter_nondigits` will take in a list of strings and filter out all strings that include non-digit characters. Remove the new-line character (`\n`) before performing digit checks! After validating that a string is a valid digit, you will convert this element into an integer and append it into a new list, which will be returned when your function ends.

The `filter_outliers` function will function similarly, except this time, your function will take in a list of integers. You will filter out all heart rate samples that are less than 30 and greater than 250. 

To test this module on all possible inputs open a terminal in VSCode. Go to the Terminal tab in the top menu and select New Terminal. Then type the following command:

```
python test_cleaner.py
```

We recommend working on this module **first**.

**metrics.py**

This module contains three functions that you will implement to calculate various descriptive statistics on a window of data. For example, in the `window_average` function, you will calculate your data's [moving average](https://en.wikipedia.org/wiki/Moving_average) based on some window size parameter `n`.

You will apply this concept to calculate the rolling maximum and standard deviation. As these functions will only be called **after** you've cleaned and removed outliers, you can expect your list of data to be integers.

To test this module on all possible inputs, you will run the following command in your terminal:

```
python test_metrics.py
```

**main.py**

This module executes when you hit the green **Run** button above. You can also execute the following command in your terminal to run this file:

```
python main.py
```

By default, we include the path to the `data1` text file if you want to test one file at a time. After running this module, view the figures created in your `images/` directory. This filepath is found underneath the conditional `if __name__ == "__main__":` and can be modified.

However, to test this module on all your data paths, you will run the following command in your terminal:

```
python test_run.py
```

This file will combine all previously implemented modules to clean, process, and visualize your data. Be sure to abide by the file-naming conventions listed in this file, or your tests will fail! This module will also utilize file I/O to read and save your data into a list. We recommend working on this file **last**.

**writeup.md**

This file contains 4 analytical questions you will answer based on the metrics and visualizations your code generates. Remember that you can manually develop the specified data visualizations by running your `main.py` file.

## Submission 

The due date for this project is `12/16`.

To begin work on this project, you will create a repository in your GitHub and copy all these template files into your repo.

Be sure to test as you code in order to verify that your functions are working correctly. If you see that all of your tests are evaluating to a green check-mark (✅) for a specific module, that means your code is ready to go, and you can move on to the next challenge.

You can also verify that your code is working as expected by comparing the images you create in your `images/` folder to the images in the `results/` folder.

To submit this project, you will submit a link to your completed GitHub repository to Canvas.

