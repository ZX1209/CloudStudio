Add Labels and Text to Matplotlib Plots: Annotation Examples

```py
Add text to plotPermalink
See all options you can pass to plt.text here: valid keyword args for plt.txt

import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=2.0, scale=0.8, size=10)

plt.plot(xs,ys)

# text is left-aligned
plt.text(2,4,'This text starts at point (2,4)')

# text is right-aligned
plt.text(8,3,'This text ends at point (8,3)',horizontalalignment='right')

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()

```

```py
Add labels to line plotsPermalink
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=3, scale=0.4, size=10)

# 'bo-' means blue color, round points, solid lines
plt.plot(xs,ys,'bo-')

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,7,0.5))

plt.show()
```

```py
Add labels to bar plotsPermalink
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = np.arange(0,10,1)
ys = np.random.normal(loc=3, scale=0.4, size=10)

plt.bar(xs,ys)

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()
```

```py
Add labels to scatter plot pointsPermalink
Loop over the arrays with points (x and y) and call plt.annotate() using the value itself as label:

import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# using some dummy data for this example
xs = np.random.normal(loc=4, scale=2.0, size=10)
ys = np.random.normal(loc=2.0, scale=0.8, size=10)

# plot the chart
plt.scatter(xs,ys)

# zip joins x and y coordinates in pairs
for x,y in zip(xs,ys):

    label = "{:.2f}".format(y)

    # this method is called for each point
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,5,0.5))

plt.show()
```