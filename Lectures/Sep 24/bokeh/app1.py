
from bokeh.plotting import figure
from bokeh.io import curdoc
### Generate our simple "stock" trends

T = range(0,100)
S1 = [t for t in T] #going up
S2 = [-t for t in T] #going down

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)),title="Simple Stock Trends")

curdoc().add_root(p) #add the plot to the current document
# should see an empty plot
# in order to run this app, all you need to do is run `bokeh serve app.py`

