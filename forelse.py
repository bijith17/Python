#for else

for i in range(6):
     print(i)
else:
     print("finally finished!")

#break
for i in range(6):
     print(i)
     if i==5:
          break
else:
     print("finally finished!")


#continue

for i in range(6):
     if i==5:
        continue
     print(i)
else:
     print("finally finished!")
   

#pass statement

for i in [0,1,2]:
     pass
print()
