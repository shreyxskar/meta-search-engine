print("Content-type: text/html\r\n\r\n")

htmlc="""

<html>
<head>
<link rel="icon" href=\"\"\pic.jpg\"\" type="image/gif" sizes="16x16">
<title>Data Scraper</title>
<style>
body
{
    background-color:white;
    color:white;
}
input.btn
{
	background-color:black;
    border-width:4px;
    border-color:white;
	color:white;
	border-radius:10px;
}
input.btn:hover
{
	background-color:black;
    border-width:4px;
    border-color:red;
	color:red;
	border-radius:10px;
}

div.outer_c
{
	background-color:black;
	border-radius:20px;
}

</style>
<script>
function f1()
{
	var x=document.forms["form1"]["urldata"].value;
	if(x.length==0)
	{
		alert("URL field cannot be left blank!");
		return false;
	}
}
</script>
</head>
<body>
<center style="padding-top:15px">
<div class="outer_c" name="oc" style="border:2px solid black;width:500px;height:80%">
<h1>Data Scraping</h1><hr><br><br>
<form              action="thirteenth.py"              method="post" name="form1">
<h3>Enter search query :</h3>
<input type="text" name="urldataxxx" class="urldataxxx" style="width:450px;height:40px;border-radius:10px;padding-left:10px" required>
<br><br>
<h3>Choose number of pages to be scraped :</h3>
<input type="number" min=1 max=10 name="totalpg" class="totalpg" style="width:220px;height:40px;border-radius:10px;padding-left:10px" >
<br><br>

<h3>Enter .csv file name to save results :</h3>
<input type="text" name="fname" class="fname" style="width:450px;height:40px;border-radius:10px;padding-left:10px" required>



<br><br>
<input class="btn" type="submit" value="Submit" onclick="return f1()" style="width:110px;height:35px;">
<input class="btn" type="reset" value="Reset" style="width:110px;height:35px;">
</form>
</div>
</center>
</body>
</html>
"""

print(htmlc)
