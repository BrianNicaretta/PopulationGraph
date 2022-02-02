# Brian Nicaretta
# Data inputs are provided by instructor's heights list. 

# The purpose of this cells program is to make a program that makes a bar chart for
# the population of the United States in 1995, 2000, 2005, 2010 and 2015 using pyplot.

import matplotlib.pyplot as plt

def main():
    """the main function stores data for years, populations in millions and constructs a bar chart
    via the matplotlib API"""
    # Create a list with the X coordinates of each bar's left edge
    left_edges = [0, 10, 20, 30, 40]
    
    # Create a list with the heights of each bar
    heights = [266.6,282.2,295.5,309.3,320.7]
    
    # Create a variable for the bar width
    bar_width = 5
    
    # Add a title
    plt.title('United States Population')
    
    # Add labels to the axes
    plt.xlabel('Year')
    plt.ylabel('Population in millions')
    
    # Customize the tick marks
    plt.xticks([0, 10, 20, 30, 40],
               ['1995', '2000', '2005', '2010', '2015'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['250', '270', '290', '310', '330', '350'])
    
    # Build the bar chart
    plt.bar(left_edges, heights, bar_width, 
            color=('m', 'k', 'r', 'b', 'y'))
    
    # Display the bar chart
    plt.show()
    
if __name__ == "__main__":
    main()