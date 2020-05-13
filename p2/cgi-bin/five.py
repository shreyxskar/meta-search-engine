

str1="https://www.tripadvisor.in/Hotel_Review-g306995-d645554-Reviews-So_My_Resort-Calangute_North_Goa_District_Goa.html#REVIEWS"
#str1="Shreyaskar"
link=str1[:str1.rindex('-Reviews-')+len('-Reviews-')]+"or"+str(i*5)+str1[str1.rindex('-Reviews-')+len('-Reviews'):]
print("",str1,"\n",link)
