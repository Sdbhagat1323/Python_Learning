# Regular Expression
'''
Indentifier (hy we looking for a number)

\d any number
\D any thing but a number
\s space
\S anything but a space
\w any charecter
\W anything but charecter
.  any charater.except new line
\b  the whitespace around word
\. a period

modifier (hy we looking this amount or this type of number ):
{1, 3} we are expecting 1-3  
+ match 1 or more
? match 0 or 1
* match 0 or more
$ match the end of the string
^ matching the beginning of  string
| either or (\d{1-3} | \w{5-6})
[] range or "varience"
{x} expecting  "x" amount
White Space Charecters:

\n new line
\s space
\t tab
\e escape
\form feed
\r return

DON'T Forget!!


. + * ? [ } $ ^ ( ) {} | \  


'''

import re

exampleString = '''
Jesssica is 15 year old,and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
# we try to pool name and age
ages = re 


Ages = re.findall(r'\d{1,3}', exampleString)
Names = re.findall(r'[A-Z][a-z]*', exampleString)


print(Ages)
print(Names)



agedict = {}
X = 0 
for eachname in Names:
         agedict[eachname] = Ages[X]
         
         X += 1 
print(agedict)





























