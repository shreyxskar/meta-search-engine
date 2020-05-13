import cgi
print('''

<html>
<head>
<title>Search hotels in Goa</title>
<style>a{text-decoration:none;}
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
div.iframes
{
    overflow:hidden;
}
iframe
{
    overflow:hidden;
}
input.inp_bar
{
    border: 2px solid #00A680;
    height:35px;
    transition:0.4s;
    width:40%;
    color:#00A680;
    padding-left:10px;
}
input.inp_bar:hover
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
</style>
</head>
<body>
<center>
<div class="header">
<h1><a href="homepage.py">Hotels in Goa</a></h1>
<h3 style="width:90%"><marquee>Plan your Goa stay in a smarter way</marquee></h3>
</div>

<div class="search_bar">
<form action="customer.py" name="search_form" method="post" target="hotel_frame">
<input type="text" class="inp_bar" name="inp_bar" placeholder="Enter here...">
<input type="submit" class="btn" value="Search">
</div>
Helpful tags:
<input type="submit" class="btn" value="good food">
<input type="submit" class="btn" value="excellent">
<input type="submit" class="btn" value="location">
<input type="submit" class="btn" value="room service">
<input type="submit" class="btn" value="value for money">
<br>
</center>
<br>

<div name="iframes"> 
<iframe name="hotel_frame" width="27%" height="68%" style="overflow:hidden;">
</iframe>
<iframe name="browser1" width="69%" height="68%"></iframe>
</div>

</body>
</html>

''')
