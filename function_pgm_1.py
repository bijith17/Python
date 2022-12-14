length=int(input("Enter the length:-"))
breadth=int(input("Enter the breadth:-"))
choice=input("enter the choice")
 

def area_rect(length,breadth):
     area_rectangle=length*breadth
     print(area_rectangle)
     

def peri_rect(length,breadth):
     peri_rectangle=2*(length+breadth)
     print(peri_rectangle)
     

if choice=="area":
     print("The area of rectangle of given number is ")
     area_rect(length,breadth)

else:
     print("The perimeter of rectangle of given number is ")
     peri_rect(length,breadth)





