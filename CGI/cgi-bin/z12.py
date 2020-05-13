import cgi

print("""print "Content-type: text/html; charset=utf-8""")
print("""
<!DOCTYPE html>
<html>
<body>
<script>
function changeImage()
{
    alert("Hello");
}
</script>

<img id="myimage" onclick="changeImage()"
src="pic.jpg" >

<p>Click the light bulb to turn on/off the light</p>

</body>
</html>

""")
