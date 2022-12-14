s={}
s["color"]="black"
print (s)
print()

d={"name":"python","s":20,"age":30,"dec":45.5}
print (d)
print(len(d))
print(type(d))
print(d["age"])
d["age"]=40
print("age",d["age"])

if "age" in d:
     print("yes, age is one of the key in this dictionary")
else:
          print("not found")

d["color"]="black"
print (d)

del d["age"]
print (d)

d.clear()
print(d)

del d  
#print(d) d is deleted!



          
          
