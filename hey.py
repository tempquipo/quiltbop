# print('exploring:day 1')
# print("application of scientific knowledge' for practical purposes")
# print('application of scientific k"nowledge for practical purposes')

#nothing makes a difference with a different quotation in between 2 similar quotes

# print('application of scientific knowledge\' for practical purposes')
# print("application of scientific knowledge\" for practical purposes")

#add in a \ before using the similar quote to avoid any errors while using the same quotation thrice

# print('''application of scientific 
# knowledge for practical purposes''')

#no errors will be displayed when using triple quotations when text in two seperat lines

# print('''application of scientif"ic knowledge' for practical purposes''')
# print("""application of scientific knowledge'" for practical purposes""")
# print('''application of scientific knowledge' 
# 
# for practical purposes''')

#can be written within 3 quotations too, statement gets printed, no matter the space nor the lines left empty within the quotations

#4 forms of printing a statement
# print('application of scientific knowledge for practical purposes')
# print("application of scientific knowledge for practical purposes")
# print('''application of scientific knowledge for practical purposes''')
# print("""application of scientific knowledge for practical purposes""")


# print('print(application of scientific knowledge for practical purposes)')
# print("print(application of scientific knowledge' for practical purposes)")
# print('''print(application of scientific knowledge for practical purposes)''')
# print("""print(application of scientific knowledge for practical purposes)""")





"""
Date:- 14th April 2022 Thursday
Name: HD
File Description: Data types in Python
"""
# print(type(56))
# print(type(4))
# print(type(-2))
# print(type(0.233))
# print(type(40/2))
# print(type(3.0))
# print(type(.2*7))
# print(type(-3.7%6))
# print(type(6.0))
# print(type('Hi'))
# print(type("Bye"))
# print(type('''I'm A'''))
# print(type("""Python"""))
# a='heY'
# print(type(a))






'''
Date: 15th April 2022 Friday
Name: HD
File Description: working with int , float and str
'''
#TO KNOW THE CLASS TYPE
# print(type(5))
# print(type(5.8))
# print(type('hi'))

#TO KNOW WHETHER THE VARIABLE NAME IS VALID OR INVALID / varible rules
# print('r'.isidentifier())
# print('A'.isidentifier())
# print('H2'.isidentifier())
# print('_a'.isidentifier())
# print('3B'.isidentifier())
# print('M_3_'.isidentifier())
# print('_O$'.isidentifier())
# print('a b c'.isidentifier())


# a=78 ; b=89 ; c= 21.45 ; d= 67.13 ; e='ohh'
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(e))


# print(a+b) # int + int      
# print(a+c) # int + float    
# print(c+d) # float + float  
# print(d+a) # float + int    

# print(e+a)  # TypeError
# print(e+c)  # TypeError

#STRING WITH ANOTHER STRING CAN BE ADDED N PRINTED BUT NOT WHEN IT'S WITH ANOTHER DATA TYPE

# x='HA'; y='HA'
# print(x+y)  #HAHA
# print(y+x)  #HAHA
# print(x,y)  #HA HA
# print(y,x)  #HA HA



# Concatenation(+) IS TO Join or combine two or multiple strings together.
# (,) is to add space in between characters
# print('how','r ya')  # how r ya
# print('anytime','so'+'on') # anytime soon

# len counts the number of characters within the quotations, includig spaces 
# index starts from 0
# length starts from 1

# print(len('how long'))
# print(len('howlong'))


# b='heyjkbkj'
# print(len(b))

# this provides the length of the characters

# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[4])
# print(b[5])
# print(b[6])  
# print(b[7])
# print(b[8])    # indexerror
# print(b[9])    # indexerror



# display as True, when it has single space or multiple spaces.
# display as False, when it has no space or contains something in it.

# print(' '.isspace()) 
# print('     '.isspace()) 
# print(''.isspace()) 
# print(' .cvcvbc '.isspace()) 


# print(''+'cmcrkerj')
# print(' '+'xfdfhdth')


# print('sf'+'df')
# print('sf'+'df')
# print('sf','df')

# conversion 'int' to 'str' in 2 ways
# print('hi'+'5'+'hi')
# print('hi'+str(5)+'hi')

a=4.75
print (str(a))
print(int(a))    # as int doesn't contain any point values it provides the whole value
# string cannot be converted into int nor float
# valueerror

# string should be first converted into float and then int
















# a={1,2,3}
# b='hello',1,2,3
# a.add(b)
# print(a)

# b={1,5,7}   #imp
# b.clear()
# print(b) 

# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(d))

# a={1,2,3,'hello'}
# b={4,3,5,'hey'}
# print(a.union(b))#order might change
# print(b.union(a))


# a={1,2,3}
# b={4,3,5}#update and union are same
# c={4,3,7}
# a.update(b)
# a.update(c)
# print (a)

# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b))
# print(b.difference(a))

# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)
# z.discard(73)
# print(z)

# v={26,7,11,4,23}
# v.pop()
# print(v)

# #any element can be eliminated/popped out incase of sets

# v=[26,7,11,4,23]
# v.pop()
# print(v)

# #incase of lists the last element gets eliminated



# 5: [1,4], 6:(4,3), 7:{1,2},8:{3,"world"}}
# h.clear()
# print(h)

# a=[101,102,103,104,105]
# b=dict.fromkeys(a)
# print(b,type(b))
# print(dict.fromkeys(a,'PASS'))

# h={1:"",2: "python", 3:7,4:6.2, 5:[1,4],6:(4,3), 7: {1,2}, 8: {3: "world"}}
# # print(h.get(47))
# # print(h[47])
# # h.pop(6)
# # print(h)
# h.popitem()
# print(h)

#in case of dictionary the pop method must have 1 argument
#when using get method we get none but while passing code that's present we get the output else we get it as 'none'
#incase of dictionary we use pop item to remove the last key value from the dictionary for list its pop

# h={1:"",2: "python", 3:7,4:6.2, 5:[1,4],6:(4,3), 7: {1,2}, 8: {3: "world"}}
# # h.update({7:'core python'})
# # print(h)
# h.update({9: 'adv python'})
# print(h)

# h={1:"",2: "python", 3:7,4:6.2, 5:[1,4],6:(4,3), 7: {1,2}, 8: {3: "world"}}
# h.setdefault(8,'devOps')
# print(h)
# h.setdefault(10, 'DevOps')
# print(h)





































































