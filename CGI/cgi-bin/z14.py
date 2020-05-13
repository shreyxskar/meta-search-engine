print("Content-type:text/html\r\n\r\n")

print("""
<head>
<title>Checkout</title>
<script>
function myfun()
{
alert("We wish it'll be delivered :)");
}
</script>
</head>
<body style="color:#black">
<center>
<div class="newH" style="background-color:#FDAB9F;width:25%;border-radius:10px;padding-bottom:10px;-webkit-text-stroke:0.3px black;">
<h1 class="hdr" style="text-align:center;" >Proceed to pay</h2>
<h3> Address:</h3> <input type="text-area" required><br><br>
<h3>Mode of payment : </h3><input type="radio" name="rdo" >Cash on delivery
<br><br>
<input type="Submit" name="clk" class="clk" onclick="return myfun()">

</center>
</body>
""")
