import cgi
print('''
<html>
<head>
<title>Welcome!</title>
<style>a{text-decoration:none;font:black;}
body
{
font-family:lucida console;
    background:#C0C0C0;
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
div.links
{
    text-align:center;
    width:40%;
    height:20%;
    background-color:#00A680;
    border: 1px solid #00A680;
    border-radius:2px;
    padding:10px 10px 10px 10px;
    margin:20px 20px 20px 20px;
    transition:0.5s;
}
div.links:hover
{
    font-size:20px;
    box-shadow: 5px 5px 5px 5px black;
}
</style>
</head>
<body>
<center>
<div class="header">
<h1><a href="homepage.py">Hotels in Goa</a></h1>
<h3 style="width:90%"><marquee>Plan your Goa stay in a smarter way</marquee></h3>
</div>


<div class="links"><a href="load1.py"><h3> For customers </h3><p>Search hotels based on your preferences<br> like location, food or room service etc.</p></a></div>
<div class="links"><a href="eleven.py"><h3> For hoteliers </h3><p>Keep track of all your hotels here!<br>Come to know about about your<br>services based on user reviews.</p></a></div>
<div class="links"><a href="rankpage.py"><h3>View our top-rated hotels in Goa</h3><p>We go through all the reviews<br>of the customers<br>and rank the hotels accordingly.<br>Try it! </p></a> </div></center>
</html>
''')
