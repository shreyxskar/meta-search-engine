import cgi

def generateKey(inp):
    return inp.replace(' ','%20').lower()


inp=input("Enter search string -> ")
part1="https://www.flipkart.com/search?q="
part2=generateKey(inp)
part3="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="


resultant=part1+part2+part3+'1';

print(resultant);


i=99
r2=resultant[:resultant.rindex('=')+1]+'2'+str(2+i)
print(r2)
