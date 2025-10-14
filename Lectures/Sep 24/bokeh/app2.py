
from bokeh.plotting import figure
from bokeh.io import curdoc
### Generate our simple "stock" trends

T = [t for t in range(0,100)]
S1 = [t for t in T] #going up
S2 = [-t for t in T] #going down

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)),title="Simple Stock Trends")

curdoc().add_root(p) #add the plot to the current document
p.line(T,S1) #plot the line for S1

