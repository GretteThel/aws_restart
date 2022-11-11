#Store the human preproinsulin sequence in a variable called prepoinsulin
preproinsulin=
"Store the remaining sequence element of human insulin in variables name isInsulin, bInsulin, aInsulin,cInsulin
isInsulin=""
bInsulin=""
aInsulin=""
cInsulin=""
insulin=bInsulin + aInsulin
print(insulin)
pkr = {'y':10.07, 'c':8.18, 'k':10.53, 'h':6.00, 'r':12.48, 'd':3.65, 'e':4.25}
#y,c,k,h,r,d,e are the only amino acids that contribute to the net charge calculation.
#In this exercise, we will use count() method and list comprehension to count the number of y,c,k,h,r,d,e amino acids. These amino acids contribute to the net charge.
x=float(insulin.count('y'))
float(x)
print(type(x))
List=['y','c','k','h','r','d','e']
#for i in List:
#    print(float(insulin.count(i)))
seqCount={i:float(insulin.count(i)) for i in List}
print(seqCount)
#In this exercise we will construct the net charge formula
pH=0
while()