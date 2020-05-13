print("Content-type: text/html\r\n\r\n")

print('''
<html>
<title>Welcome Hoteliers, your reviews are here</title>
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
input.inph_bar
{
    border: 2px solid #00A680;
    height:35px;
    transition:0.4s;
    width:40%;
    color:#00A680;
    padding-left:10px;
}
input.inph_bar:hover
{
    box-shadow: 2px 2px 2px 1px grey;
}
input.btn
{
   border: 2px solid #00A680;
   transition:0.4s;
   width:10%;
   background-color:#00A680;
   height:35px;
   color:white;
   font-size:15px;
   cell-padding:5px 5px 5px 5px;
}
input.btn:hover
{
    box-shadow: 2px 2px 2px 1px grey;
}
iframe
{
    border:0;
}
</style>
<head>
</head>
<body>
<center>
<div class="header">
<h1><a href="homepage.py">Hotels in Goa</a></h1>
<h3 style="width:90%"><marquee>Plan your Goa stay in a smarter way</marquee></h3>
</div>

<div class="search_bar">
<form action="hotelier.py" name="search_form" method="post" target="hotel_frame">
<input type="text" class="inph_bar" name="inph_bar" placeholder="Enter here...">
<input type="submit" class="btn" value="Search">
</div>

<div name="iframes"> 
<iframe name="hotel_frame" width="90%" height="68%" style="overflow:hidden;">

</div>
</center>
</body>
</html>
''')

