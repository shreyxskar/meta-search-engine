import cgi

print("Content-type: text/html\r\n\r\n")

print('''

<html>
<head>
<title>Hotel Rankings Page</title>
<style>
a{text-decoration:none;transition:0.5s;}
a:hover
{color:white;}
body
{
font-family:lucida console;
    background-color:#F0F0F0;
}
h1
{
    -webkit-text-stroke:1px #00A680;
    
    font-size:30px;
    color:#00A680;
}
h3
{
    color:white;
}
</style>
</head>
<body>
<center>
<div>
<h1><a href="homepage.py">Hotels in Goa</a></h1>
<h3 style="width:90%"><marquee>Plan your Goa stay in a smarter way</marquee></h3>
</div>
</center><iframe src="rankings.py" name="leftone" border=0 width="35%" height="82%"></iframe>
<iframe src="see.py" name="rightone" border="0" width="60%" height="82%"></iframe>

</body>
</html>

''')
