print('''

<html>
<head>
<title>Electronic Products hub</title>

<style>
select.optns
{
	width:20%;
	height:15px;
	border:7px solid #FDAB9F;
	border-radius:10px;
	padding: 5px 5px 5px 5px;
	margin-bottom:10px;
}
div.header
{
	color:white;		
	padding-top:3px;
	padding-bottom:3px;
	width:70%;
	background-color:#FDAB9F;
	text-align:center;
	margin-bottom:10px;
	border:1px solid black;
}
div.user_bar
{
	width:100%;	
	height:10px;
	background-color:black;
	color:white;
	margin-bottom:25px;
}
input.query_bar
{
	width:26%;
	border:7px solid #FDAB9F;
	border-radius:10px;
	padding: 5px 5px 5px 5px;
	margin-bottom:10px;
}
input.sub_btn
{
	width:50%;
	border:7px solid #FDAB9F;
	border-radius:10px;
	padding: 5px 5px 5px 5px;
	background-color:white;
	margin-top:10px;
}
iframe.load_res
{
		
}
input.sub_btn:hover
{
	background-color:#E0E0E0;
}
input.query_bar:hover
{
	background-color:#E0E0E0;
}
input.fname_bar
{
	width:25%;
	border:7px solid #FDAB9F;
	border-radius:10px;
	padding: 5px 5px 5px 5px;
}
input.fname_bar:hover
{
	
	background-color:#E0E0E0;
}
input:focus
{
	outline:none !important;
}
</style>
</head>
<body>
<center>
<div class="header" >
<h1>Gadget price comparison </h1>
</div>

<form class="user_bar" method="post" name="form1" action="z2.py" target="load_res">

<input type="text" class="query_bar" name="query_bar" placeholder="Enter product name here" required>
<input type="text" class="fname_bar" name="fname_bar" placeholder="Enter database/filename here" required>
<br>
Show results from :
<select name="optns" required>
<option name="1" value="1">Croma</option>
<option name="2" value="2">Flipkart</option>
<option name="3" value="3">Snapdeal</option>
<option name="4" value="4" selected>All</option>
</select>
<p></p>
Sort by :
<select name="sort" value="sort" required>
<option name="asc" value="asc">asc</option>
<option name="desc" value="desc">desc</option>
</select>
<br>
<input type="Submit" class="sub_btn" value="Search" onclick="hlo()">
</center>


<br><p align="center">
<iframe class="load_res" name="load_res" height="400px" width="1300px" frameborder="none">
</p></form></center>
</body>
</html>
''')


'''
'''
