import pandas as pd     # import pandas as pd
import matplotlib.pyplot as plt     # import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show      # from matplotlib.pyplot import plot, draw, show
import termcolor       # import termcolor
import cprint       # import cprint

pd.set_option('display.max_rows',None)  # display all rows when asked to

# Read csv file of oil prices from https://datahub.io/core/oil-prices
data = pd.read_csv("brent-daily_csv.csv")
# Get the data from 2015 to 2020
data = data[7008:]
# Get only the prices from data
us_prices = list(data['Price'])
# Initialize cad_prices list
cad_prices = []
# Get the dates from the data list
dates = list(data['Date'])
# Initialize the total dictionary, which will 
# contain prices and dates
total = {}

# for every price and every date in us_prices,dates
for price, date in zip(us_prices,dates):
    total[date] = price # date : price

for value in us_prices: # for every value in us_prices
    # append int(value) * 1.43 to the cad_prices list
    cad_prices.append(int(value)*1.43)

# Initialize plot figure
fig = plt.figure()

# add an axes called ax
ax = fig.add_axes([0, 0, 1, 1])

# Plot the US dollar oil price in red
plot(us_prices, label="USD",color='red')
# Plot the CAD dollar oil price in green
plot(cad_prices, label="CAD", color='green')

# set a y label "Price"
plt.ylabel("Price")
# set an x label "Years"
plt.xlabel("Years")
# set the title "Price of Oil over the years"
plt.title('Price of Oil over the years')
# Show the Legend
ax.legend()
# Save the figure into variable name fig1
fig1 = plt.gcf()
# Show the plot
plt.show()
# ask user if they want to save it
saveIt = input("Would you like to save this plot? ")

# If they do
if saveIt.lower() == 'yes':
    # ask for the name of the file
    name = input("What will be the name of the file?\n")
    # print "Plot saved as {name}.png"
    print(f"Plot saved as {name}.png")
    # add .png to name
    name += '.png'
    # save the plot
    fig1.savefig(name,dpi=100)
    # print out in green "Figure Saved"
    termcolor.cprint(f"Saved Figure as {name}", 'green')

# elif they don't
elif saveIt.lower() == 'no':
    # print out in red "Figure not saved"
    termcolor.cprint("Figure not saved", 'red')

# Otherwise
else:
    # print out in red "Figure not saved"
    termcolor.cprint("Figure not saved", 'red')

