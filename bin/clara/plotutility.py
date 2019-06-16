import matplotlib.pyplot as plt
import logging as log
log.basicConfig(level=log.DEBUG)
log.debug('this is a demo massage')


def zoom_factory(ax, base_scale=1.5):
    prex = 0
    prey = 0
    prexdata = 0
    preydata = 0

    def zoom_fun(event):
        nonlocal prex, prey, prexdata, preydata
        curx = event.x
        cury = event.y

        # if not changed mouse position(or changed so little)
        # remain the pre scale center
        if abs(curx - prex) < 10 and abs(cury - prey) < 10:
            # remain same
            xdata = prexdata
            ydata = preydata
        # if changed mouse position ,also change the cur scale center
        else:
            # change
            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location

            # update previous location data
            prex = event.x
            prey = event.y
            prexdata = xdata
            preydata = ydata

        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()

        cur_xrange = (cur_xlim[1] - cur_xlim[0]) * .5
        cur_yrange = (cur_ylim[1] - cur_ylim[0]) * .5

        # log.debug((xdata, ydata))
        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        ax.set_xlim([
            xdata - cur_xrange * scale_factor,
            xdata + cur_xrange * scale_factor
        ])
        ax.set_ylim([
            ydata - cur_yrange * scale_factor,
            ydata + cur_yrange * scale_factor
        ])
        plt.draw()  # force re-draw

    fig = ax.get_figure()  # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event', zoom_fun)

    # return the function
    return zoom_fun


fig, ax = plt.subplots(1, 1)

ax.plot(range(10))
scale = 1.1
f = zoom_factory(ax, base_scale=scale)

fig.show()
