<h1>Films map</h1>
This module allows to look at the closet (up to 10) locations where movies were filmed
<h1>How the program works</h1>
The module uses locations.list from imdb.com, filters all movies that were filmed in the given year and country (it is calculated based on
the coordinates given). Then it calculates 10 closest locations and creates a map with markers on these locations
<h1>Notes</h1>
The map has three layers:

1. Main layer

2. Films layers - shows all nearest film locations. Blue markers are film locations, red marker is your written location

3. Distance layer - shows distance to these locations. If you want to see them, click on the marker.

<h1>Requirements</h1>
Write coordinates in a tuple e.g (50.4500336, 30.5241361) and year as an int from 1896 to 2019
<h1>HTML tags</h1>
<!DOCTYPE html> - an instruction to the web browser about what version of HTML the page is written in.

&lt;head&gt; - a container for metadata.
  
&lt;body&gt; - defines the document's body
  
&lt;meta&gt; - provides metadata about the HTML document

&lt;script&gt; - used to define a client-side script (JavaScript)
  
&lt;link&gt; - allow users to click their way from page to page.

&lt;style&gt; - used to define style information for an HTML document.
  
&lt;div&gt; - defines a division or a section in an HTML document.
  
<h1>Conclusion</h1>
The program shows the closest film locations in the desired year and can be useful if you are wondering where to go.
<h1>Example</h1>
For example look at the Map_example.jpg file. The input was: create_map((50.4500336, 30.5241361), 2006)
