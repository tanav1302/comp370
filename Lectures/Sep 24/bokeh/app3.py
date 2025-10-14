
from bokeh.plotting import figure
from bokeh.models import Dropdown
from bokeh.layouts import column
from bokeh.io import curdoc
### Generate our simple "stock" trends

T = [t for t in range(0,100)]
S1 = [t for t in T] #going up
S2 = [-t for t in T] #going down

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)),title="Simple Stock Trends")

r = p.line(T,S1) 

ds = r.data_source

### create a dropdown menu to select the stock trend
menu = [("Stock 1", "S1"), ("Stock 2", "S2")]
dropdown = Dropdown(label="Select Stock Trend", menu=menu)
# Now it's not going to show up yet because we're going to have to put it into our root.
# So we need to go add a layout from layouts,

curdoc().add_root(column(p, dropdown)) #add the plot and dropdown to the current document


# we now have a dropdown menu, but it doesn't do anything.
# And so we're going to have to add something so
# that when I click stock one, it selects stock.
# One and then puts that line up here and right
# now it's showing stock one, but when I hit.
# Stock 2 it just show my stock 2 all right.
