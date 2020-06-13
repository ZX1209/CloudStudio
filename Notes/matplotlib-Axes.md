# texts
ax.texts


Plotting
Basic
Axes.plot	Plot y versus x as lines and/or markers.
Axes.errorbar	Plot y versus x as lines and/or markers with attached errorbars.
Axes.scatter	A scatter plot of y vs x with varying marker size and/or color.
Axes.plot_date	Plot data that contains dates.
Axes.step	Make a step plot.
Axes.loglog	Make a plot with log scaling on both the x and y axis.
Axes.semilogx	Make a plot with log scaling on the x axis.
Axes.semilogy	Make a plot with log scaling on the y axis.
Axes.fill_between	Fill the area between two horizontal curves.
Axes.fill_betweenx	Fill the area between two vertical curves.
Axes.bar	Make a bar plot.
Axes.barh	Make a horizontal bar plot.
Axes.stem	Create a stem plot.
Axes.eventplot	Plot identical parallel lines at the given positions.
Axes.pie	Plot a pie chart.
Axes.stackplot	Draw a stacked area plot.
Axes.broken_barh	Plot a horizontal sequence of rectangles.
Axes.vlines	Plot vertical lines.
Axes.hlines	Plot horizontal lines at each y from xmin to xmax.
Axes.fill	Plot filled polygons.
Spans
Axes.axhline	Add a horizontal line across the axis.
Axes.axhspan	Add a horizontal span (rectangle) across the axis.
Axes.axvline	Add a vertical line across the axes.
Axes.axvspan	Add a vertical span (rectangle) across the axes.
Spectral
Axes.acorr	Plot the autocorrelation of x.
Axes.angle_spectrum	Plot the angle spectrum.
Axes.cohere	Plot the coherence between x and y.
Axes.csd	Plot the cross-spectral density.
Axes.magnitude_spectrum	Plot the magnitude spectrum.
Axes.phase_spectrum	Plot the phase spectrum.
Axes.psd	Plot the power spectral density.
Axes.specgram	Plot a spectrogram.
Axes.xcorr	Plot the cross correlation between x and y.
Statistics
Axes.boxplot	Make a box and whisker plot.
Axes.violinplot	Make a violin plot.
Axes.violin	Drawing function for violin plots.
Axes.bxp	Drawing function for box and whisker plots.
Binned
Axes.hexbin	Make a 2D hexagonal binning plot of points x, y.
Axes.hist	Plot a histogram.
Axes.hist2d	Make a 2D histogram plot.
Contours
Axes.clabel	Label a contour plot.
Axes.contour	Plot contours.
Axes.contourf	Plot contours.
Array
Axes.imshow	Display an image, i.e.
Axes.matshow	Plot the values of a 2D matrix or array as color-coded image.
Axes.pcolor	Create a pseudocolor plot with a non-regular rectangular grid.
Axes.pcolorfast	Create a pseudocolor plot with a non-regular rectangular grid.
Axes.pcolormesh	Create a pseudocolor plot with a non-regular rectangular grid.
Axes.spy	Plot the sparsity pattern of a 2D array.
Unstructured Triangles
Axes.tripcolor	Create a pseudocolor plot of an unstructured triangular grid.
Axes.triplot	Draw a unstructured triangular grid as lines and/or markers.
Axes.tricontour	Draw contours on an unstructured triangular grid.
Axes.tricontourf	Draw contours on an unstructured triangular grid.
Text and Annotations
Axes.annotate	Annotate the point xy with text text.
Axes.text	Add text to the axes.
Axes.table	Add a table to an Axes.
Axes.arrow	Add an arrow to the axes.
Axes.inset_axes	Add a child inset axes to this existing axes.
Axes.indicate_inset	Add an inset indicator to the axes.
Axes.indicate_inset_zoom	Add an inset indicator rectangle to the axes based on the axis limits for an inset_ax and draw connectors between inset_ax and the rectangle.
Axes.secondary_xaxis	Add a second x-axis to this axes.
Axes.secondary_yaxis	Add a second y-axis to this axes.
Fields
Axes.barbs	Plot a 2D field of barbs.
Axes.quiver	Plot a 2D field of arrows.
Axes.quiverkey	Add a key to a quiver plot.
Axes.streamplot	Draw streamlines of a vector flow.
Clearing
Axes.cla	Clear the current axes.
Axes.clear	Clear the axes.
Appearance
Axes.axis	Convenience method to get or set some axis properties.
Axes.set_axis_off	Turn the x- and y-axis off.
Axes.set_axis_on	Turn the x- and y-axis on.
Axes.set_frame_on	Set whether the axes rectangle patch is drawn.
Axes.get_frame_on	Get whether the axes rectangle patch is drawn.
Axes.set_axisbelow	Set whether axis ticks and gridlines are above or below most artists.
Axes.get_axisbelow	Get whether axis ticks and gridlines are above or below most artists.
Axes.grid	Configure the grid lines.
Axes.get_facecolor	Get the facecolor of the Axes.
Axes.get_fc	Get the facecolor of the Axes.
Axes.set_facecolor	Set the facecolor of the Axes.
Axes.set_fc	Set the facecolor of the Axes.
Property cycle
Axes.set_prop_cycle	Set the property cycle of the Axes.
Axis / limits
Axes.get_xaxis	Return the XAxis instance.
Axes.get_yaxis	Return the YAxis instance.
Axis Limits and direction
Axes.invert_xaxis	Invert the x-axis.
Axes.xaxis_inverted	Return whether the x-axis is inverted.
Axes.invert_yaxis	Invert the y-axis.
Axes.yaxis_inverted	Return whether the y-axis is inverted.
Axes.set_xlim	Set the x-axis view limits.
Axes.get_xlim	Return the x-axis view limits.
Axes.set_ylim	Set the y-axis view limits.
Axes.get_ylim	Return the y-axis view limits.
Axes.update_datalim	Extend the dataLim BBox to include the given points.
Axes.update_datalim_bounds	Extend the datalim BBox to include the given Bbox.
Axes.set_xbound	Set the lower and upper numerical bounds of the x-axis.
Axes.get_xbound	Return the lower and upper x-axis bounds, in increasing order.
Axes.set_ybound	Set the lower and upper numerical bounds of the y-axis.
Axes.get_ybound	Return the lower and upper y-axis bounds, in increasing order.
Axis Labels, title, and legend
Axes.set_xlabel	Set the label for the x-axis.
Axes.get_xlabel	Get the xlabel text string.
Axes.set_ylabel	Set the label for the y-axis.
Axes.get_ylabel	Get the ylabel text string.
Axes.set_title	Set a title for the axes.
Axes.get_title	Get an axes title.
Axes.legend	Place a legend on the axes.
Axes.get_legend	Return the Legend instance, or None if no legend is defined.
Axes.get_legend_handles_labels	Return handles and labels for legend
Axis scales
Axes.set_xscale	Set the x-axis scale.
Axes.get_xscale	Return the x-axis scale as string.
Axes.set_yscale	Set the y-axis scale.
Axes.get_yscale	Return the y-axis scale as string.
Autoscaling and margins
Axes.use_sticky_edges	When autoscaling, whether to obey all Artist.sticky_edges.
Axes.margins	Set or retrieve autoscaling margins.
Axes.set_xmargin	Set padding of X data limits prior to autoscaling.
Axes.set_ymargin	Set padding of Y data limits prior to autoscaling.
Axes.relim	Recompute the data limits based on current artists.
Axes.autoscale	Autoscale the axis view to the data (toggle).
Axes.autoscale_view	Autoscale the view limits using the data limits.
Axes.set_autoscale_on	Set whether autoscaling is applied on plot commands
Axes.get_autoscale_on	Get whether autoscaling is applied for both axes on plot commands
Axes.set_autoscalex_on	Set whether autoscaling for the x-axis is applied on plot commands
Axes.get_autoscalex_on	Get whether autoscaling for the x-axis is applied on plot commands
Axes.set_autoscaley_on	Set whether autoscaling for the y-axis is applied on plot commands
Axes.get_autoscaley_on	Get whether autoscaling for the y-axis is applied on plot commands
Aspect ratio
Axes.apply_aspect	Adjust the Axes for a specified data aspect ratio.
Axes.set_aspect	Set the aspect of the axis scaling, i.e.
Axes.get_aspect	
Axes.set_adjustable	Define which parameter the Axes will change to achieve a given aspect.
Axes.get_adjustable	
Ticks and tick labels
Axes.set_xticks	Set the x ticks with list of ticks
Axes.get_xticks	Return the x ticks as a list of locations
Axes.set_xticklabels	Set the x-tick labels with list of string labels.
Axes.get_xticklabels	Get the x tick labels as a list of Text instances.
Axes.get_xmajorticklabels	Get the major x tick labels.
Axes.get_xminorticklabels	Get the minor x tick labels.
Axes.get_xgridlines	Get the x grid lines as a list of Line2D instances.
Axes.get_xticklines	Get the x tick lines as a list of Line2D instances.
Axes.xaxis_date	Sets up x-axis ticks and labels that treat the x data as dates.
Axes.set_yticks	Set the y ticks with list of ticks
Axes.get_yticks	Return the y ticks as a list of locations
Axes.set_yticklabels	Set the y-tick labels with list of strings labels.
Axes.get_yticklabels	Get the y tick labels as a list of Text instances.
Axes.get_ymajorticklabels	Get the major y tick labels.
Axes.get_yminorticklabels	Get the minor y tick labels.
Axes.get_ygridlines	Get the y grid lines as a list of Line2D instances.
Axes.get_yticklines	Get the y tick lines as a list of Line2D instances.
Axes.yaxis_date	Sets up y-axis ticks and labels that treat the y data as dates.
Axes.minorticks_off	Remove minor ticks from the axes.
Axes.minorticks_on	Display minor ticks on the axes.
Axes.ticklabel_format	Change the ScalarFormatter used by default for linear axes.
Axes.tick_params	Change the appearance of ticks, tick labels, and gridlines.
Axes.locator_params	Control behavior of major tick locators.
Units
Axes.convert_xunits	Convert x using the unit type of the xaxis.
Axes.convert_yunits	Convert y using the unit type of the yaxis.
Axes.have_units	Return True if units are set on the x or y axes.
Adding Artists
Axes.add_artist	Add an Artist to the axes, and return the artist.
Axes.add_child_axes	Add an AxesBase to the axes' children; return the child axes.
Axes.add_collection	Add a Collection to the axes' collections; return the collection.
Axes.add_container	Add a Container to the axes' containers; return the container.
Axes.add_image	Add an AxesImage to the axes' images; return the image.
Axes.add_line	Add a Line2D to the axes' lines; return the line.
Axes.add_patch	Add a Patch to the axes' patches; return the patch.
Axes.add_table	Add a Table to the axes' tables; return the table.
Twinning
Axes.twinx	Create a twin Axes sharing the xaxis
Axes.twiny	Create a twin Axes sharing the yaxis
Axes.get_shared_x_axes	Return a reference to the shared axes Grouper object for x axes.
Axes.get_shared_y_axes	Return a reference to the shared axes Grouper object for y axes.
Axes Position
Axes.get_anchor	Get the anchor location.
Axes.set_anchor	Define the anchor location.
Axes.get_axes_locator	Return the axes_locator.
Axes.set_axes_locator	Set the axes locator.
Axes.reset_position	Reset the active position to the original position.
Axes.get_position	Get a copy of the axes rectangle as a Bbox.
Axes.set_position	Set the axes position.
Async/Event based
Axes.stale	Whether the artist is 'stale' and needs to be re-drawn for the output to match the internal state of the artist.
Axes.pchanged	Call all of the registered callbacks.
Axes.add_callback	Add a callback function that will be called whenever one of the Artist's properties changes.
Axes.remove_callback	Remove a callback based on its observer id.
Interactive
Axes.can_pan	Return True if this axes supports any pan/zoom button functionality.
Axes.can_zoom	Return True if this axes supports the zoom box button functionality.
Axes.get_navigate	Get whether the axes responds to navigation commands
Axes.set_navigate	Set whether the axes responds to navigation toolbar commands
Axes.get_navigate_mode	Get the navigation toolbar button status: 'PAN', 'ZOOM', or None
Axes.set_navigate_mode	Set the navigation toolbar button status;
Axes.start_pan	Called when a pan operation has started.
Axes.drag_pan	Called when the mouse moves during a pan operation.
Axes.end_pan	Called when a pan operation completes (when the mouse button is up.)
Axes.format_coord	Return a format string formatting the x, y coordinates.
Axes.format_cursor_data	Return a string representation of data.
Axes.format_xdata	Return x formatted as an x-value.
Axes.format_ydata	Return y formatted as an y-value.
Axes.mouseover	
Axes.in_axes	Return True if the given mouseevent (in display coords) is in the Axes
Axes.pick	Process a pick event.
Axes.pickable	Return whether the artist is pickable.
Axes.get_picker	Return the picking behavior of the artist.
Axes.set_picker	Define the picking behavior of the artist.
Axes.set_contains	Define a custom contains test for the artist.
Axes.get_contains	Return the custom contains function of the artist if set, or None.
Axes.contains	Test whether the artist contains the mouse event.
Axes.contains_point	Return whether point (pair of pixel coordinates) is inside the axes patch.
Axes.get_cursor_data	Return the cursor data for a given event.
Children
Axes.get_children	Return a list of the child Artists of this Artist.
Axes.get_images	return a list of Axes images contained by the Axes
Axes.get_lines	Return a list of lines contained by the Axes
Axes.findobj	Find artist objects.
Drawing
Axes.draw	Draw everything (plot lines, axes, labels)
Axes.draw_artist	This method can only be used after an initial draw which caches the renderer.
Axes.redraw_in_frame	This method can only be used after an initial draw which caches the renderer.
Axes.get_renderer_cache	
Axes.get_rasterization_zorder	Return the zorder value below which artists will be rasterized.
Axes.set_rasterization_zorder	
Parameters:	
Axes.get_window_extent	Return the axes bounding box in display space; args and kwargs are empty.
Axes.get_tightbbox	Return the tight bounding box of the axes, including axis and their decorators (xlabel, title, etc).
Bulk property manipulation
Axes.set	A property batch setter.
Axes.update	Update this artist's properties from the dictionary props.
Axes.properties	Return a dictionary of all the properties of the artist.
Axes.update_from	Copy properties from other to self.
General Artist Properties
Axes.set_agg_filter	Set the agg filter.
Axes.set_alpha	Set the alpha value used for blending - not supported on all backends.
Axes.set_animated	Set the artist's animation state.
Axes.set_clip_box	Set the artist's clip Bbox.
Axes.set_clip_on	Set whether the artist uses clipping.
Axes.set_clip_path	Set the artist's clip path, which may be:
Axes.set_gid	Set the (group) id for the artist.
Axes.set_label	Set a label that will be displayed in the legend.
Axes.set_path_effects	Set the path effects.
Axes.set_rasterized	Force rasterized (bitmap) drawing in vector backend output.
Axes.set_sketch_params	Sets the sketch parameters.
Axes.set_snap	Set the snapping behavior.
Axes.set_transform	Set the artist transform.
Axes.set_url	Set the url for the artist.
Axes.set_visible	Set the artist's visibility.
Axes.set_zorder	Set the zorder for the artist.
Axes.get_agg_filter	Return filter function to be used for agg filter.
Axes.get_alpha	Return the alpha value used for blending - not supported on all backends
Axes.get_animated	Return the animated state.
Axes.get_clip_box	Return the clipbox.
Axes.get_clip_on	Return whether the artist uses clipping.
Axes.get_clip_path	Return the clip path.
Axes.get_gid	Return the group id.
Axes.get_label	Return the label used for this artist in the legend.
Axes.get_path_effects	
Axes.get_rasterized	Return whether the artist is to be rasterized.
Axes.get_sketch_params	Returns the sketch parameters for the artist.
Axes.get_snap	Returns the snap setting.
Axes.get_transform	Return the Transform instance used by this artist.
Axes.get_url	Return the url.
Axes.get_visible	Return the visibility.
Axes.get_zorder	Return the artist's zorder.
Axes.axes	The Axes instance the artist resides in, or None.
Axes.set_figure	Set the Figure for this Axes.
Axes.get_figure	Return the Figure instance the artist belongs to.
Artist Methods
Axes.remove	Remove the artist from the figure if possible.
Axes.is_transform_set	Return whether the Artist has an explicitly set transform.
Projection
Methods used by Axis that must be overridden for non-rectilinear Axes.

Axes.name	
Axes.get_xaxis_transform	Get the transformation used for drawing x-axis labels, ticks and gridlines.
Axes.get_yaxis_transform	Get the transformation used for drawing y-axis labels, ticks and gridlines.
Axes.get_data_ratio	Return the aspect ratio of the raw data.
Axes.get_data_ratio_log	Return the aspect ratio of the raw data in log scale.
Axes.get_xaxis_text1_transform	
Returns:	
Axes.get_xaxis_text2_transform	
Returns:	
Axes.get_yaxis_text1_transform	
Returns:	
Axes.get_yaxis_text2_transform	
Returns:	
Other
Axes.zorder	
Axes.get_default_bbox_extra_artists	Return a default list of artists that are used for the bounding box calculation.
Axes.get_transformed_clip_path_and_affine	Return the clip path with the non-affine part of its transformation applied, and the remaining affine part of its transformation.
Axes.has_data	Return True if any artists have been added to axes.