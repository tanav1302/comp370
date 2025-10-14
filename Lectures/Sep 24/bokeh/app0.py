from bokeh.plotting import figure
from bokeh.io import curdoc
### Generate our simple "stock" trends

T = [t for t in range(0,100)]
S1 = [t for t in T]
S2 = [-t for t in T]

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)),title="Simple Stock Trends")

p.line(T,S1)
curdoc().add_root(p)







# we need to do is we need to install bouquet.
# 0:18:38
# So my system is already installed, but you do pip
# 0:18:41
# 3, install bouquet 


# what you'll see is it's launching
# 0:22:49
# and now it says the bokeh app is running at
# 0:22:53
# localhost 5006 app.
# 0:22:55
# So I'm going to copy that.
# 0:23:01
# We will need to forward a port because again, it's
# 0:23:04
# running on our EC2, it's not running on my local
# 0:23:06
# laptop.
# 0:23:08
# So I'm forwarding port 5006.
# 0:23:12
# The way that I did that is I just hit
# 0:23:14
# add port 5006.
# 0:23:16
# So now that port is being shared and now I
# 0:23:22
# can come into my web browser and go to.
# 0:23:33
# So now I have.
# 0:23:34
# It is a.
# 0:23:36
# Holy fledged web page that is running.
# 0:23:38
# It's got nothing showing.
# 0:23:41
# All right, let's go ahead and plot our stuff on
# 0:23:45
# it.
# 0:23:46
# So P dot line XY just to see how this.
# 0:23:55
# Works.