template = '''<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
</head>

<body>
  <!-- <script src="js/scripts.js"></script> -->
  <div>
  	%s
  </div>
  <div>
  	%s
  </div>
</body>
</html>'''

mp3_rel_link = '../mp3_tracks/'
song_links = [('What does the fox say?','Ylvis','fox.mp3'),
			  ('Fuck','Bo Burnham','fuck.mp3')]

button_ul_str = 'This is where the available songs are listed...<br><hr>'
for (title,artist,filename) in song_links:
	elem_template = '"%s" by %s <a href="%s"><button type="button">Add to Queue</button></a><br><hr>'
	button_ul_str += elem_template%(title,artist,mp3_rel_link+filename)
q_ul_str = '<hr>This is where the queued songs will go...'

f = open('queue.html','w')
f.write(template%(button_ul_str,q_ul_str))
f.close()

