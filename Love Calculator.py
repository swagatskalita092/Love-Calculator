print("WELCOME TO LOVE CALCULATOR <3 ")
name1=input("Please enter your name : ")
name2=input("Please enter his/her name : ")
together=name1+name2
lower_case=together.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
true=t+r+u+e
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
love=l+o+v+e
love_score=int(true)+int(love)
print("Your love score is : " , love_score)
if love_score>50:
    print("Perfecto")
elif love_score>20 and love_score<50:
    print("you two are alright")
else:
    print("forget the love score , love is blind anyway ")