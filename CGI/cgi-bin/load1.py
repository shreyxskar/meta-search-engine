import cgi
print('''

<html>
<head>
<title>Search hotels in Goa</title>
<style>

</style>
</head>
<body>
<center>
<div class="header">
<h1>Hotels in Goa</h1>
<h3 style="width:90%"><marquee>Plan your Goa stay in a smarter way</marquee></h3>
</div>

<div class="search_bar">
<form action="" name="search_form" method="post" target="hotel_frame">
<input type="text" class="inp_bar" placeholder="Enter here...">
<input type="submit" value="Search">
</div>

<div name="iframes"> 
<iframe name="hotel_frame" width="30%" height="70%">
</iframe>
<iframe name="browser1" width="60%" height="70%"></iframe>
</div>

</center>
</body>
</html>

''')