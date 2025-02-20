# Week 1

##################################
# Grade 100% plus 5% of extra effort
# ##################################

# PART A STRINGS

##################################
# All Correct
##################################

#format string
print('Coding' + ' ' + 'For' + ' ' + 'All')
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize(), ',', company.title(), ',', company.swapcase())
company = 'coding for all'
company = company.title()
italics = '\033[3m' # this has italicized all outputs from now on?
##################
italics_end = '\033[23m' # The italization is not necessary, but this is what you should add at the end
##################
print(italics + company + italics_end)


#slice
print(company[7:]) #Can you use slice methods to mopdify a list's memory?
##################
# Answer: only doing this you can -> company = company[7:]
################## 
company = company[7:]
print(company)

company = 'Coding For All'
print('Coding' in company)
print('Coding' in company[:])
print(company.find('Coding')) # finds first index, returns first index of the string, -1 = not there
company = company.replace('Coding','Python')
print(company)
company = company.strip('All')
company = company + 'Everyone'
print(company)
print(company.replace('All', 'Everyone'))
print(company.replace('Everyone', 'All'))

print(company.split())
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
companies = companies.split(', ')
print(companies)

company = 'Coding For All'
print(company[0])
print(company[-1])
print(company[10])
print(company.index('C')) # .index is a method!
print(company.index('F'))
company = 'Coding For All People'
print(company.rfind('l')) #rfind inherently find the last occurrence

because = 'You cannot end a sentence with because because because is a conjuction'
print(because.replace('because',''))

print(because.find('because'), because.rfind('because')) 
#How can we make ^this^ specify the last letter of the substring'because' instead of the first letter of the last occurence?
    #Keith Answer:
    #text = 'because because because'
    # first_index_last_because = text.rfind('because')
    # len_word = len('because') 
    # last_index_last_because = first_index_last_because+len_word-1 


print(because.find('b'), because.rfind('e')) # only works because there aren't other e's
#because = because.remove('because because because') # remove is a list method not for strings

because = list(because)
because1 = because[:31]
because2 = because[55:]
because = because1+because2
because = ''.join(because)
print(because)
##################
# This is very nice !
##################

because = 'You cannot end a sentence with because because because is a conjuction'
because1 = because[:31]
because2 = because[55:]
because = because1 + because2
print(because)

because = 'You cannot end a sentence with because because because is a conjuction'
print(because.find('because'))

company = '  Coding For All   '
print(company)
print(company.strip())

librs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# librs = librs.join('# ')
librs = '# '.join(librs) # Why does the formatting for this work but not what's above in the comment?
print(librs)

print('I am enjoying this challenge\nI just wonder what is next')
print('Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')

radius = 10
area = 3.14*radius**2
print('the area of a circle with radius', radius, 'is', area, 'meters squared')
print(('the area of a circle with radius {} is {} metres squared').format(radius,area))

##################
# This is very nice !
##################


op1 = 8
op2 = 6
a1 = 8+6
a2 =8-6
a3=8*6
a4=8/6
a5=8%6
a6=8//6
a7=8**6
print(('{} + {} = {} \n{} - {} = {} \n{} * {} = {}\n{} / {} = {:.2f}\n{} % {} = {}\n{} // {} = {}\n{} ** {} = {}').format(op1,op2,a1,op1,op2,a2,op1,op2,a3,op1,op2,a4,op1,op2,a5,op1,op2,a6,op1,op2,a7))

original = " Python strings are COOL! "
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()

print('original = " Python strings are COOL! "\nlower_cased = original.lower()\nstripped = original.strip()\nstripped_lower_cased = original.lower().strip()')

ugly = " tiTle of MY new Book\n\n"
print(ugly)
pretty =ugly.strip().title()
print(pretty) # I guess strip lso take away new lines as 'spaces'?

verb = 'is'
language = 'Python'
punctuation = '!'
adjective = 'fun'
sentence = (('Learning {} {} {}{}').format(language,verb,adjective,punctuation))
print(sentence)



#PARTB LISTS

##################################
# All Correct
##################################

ls = []
print(ls)
ls = [1,2,3,4,5,6,7]
print(ls)
print(len(ls))
print(ls[0],ls[3],ls[-1])
# print((int(len(ls)/2))+1)
# if it was a long list, would the quickest way to find the middle still be to divide the length by 2 then infer the index from that?
##################
# Yes! This is correct.
##################
IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(IT_companies)
print('#companies in list =', len(IT_companies))

print('first =', IT_companies[0],', ','middle =',IT_companies[3],', ','last =',IT_companies[-1])

IT_companies[0] = 'Samsung'
print(IT_companies)

IT_companies.append('Instagram')
print(IT_companies)

IT_companies.insert(4,'Dell')
print(IT_companies)

IT_companies[0] = IT_companies[0].upper()
print(IT_companies)

IT_companies = '#; '.join(IT_companies)
print(IT_companies)

IT_companies = IT_companies.lower()
print('samsung' in IT_companies)

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
IT_companies.sort()
print(IT_companies)
IT_companies.sort(reverse=True)
print(IT_companies)
# IT_companies = IT_companies[2:] # why does starting from index 2 only take 2 out of the list instead of 3 (given it goes 0,1,2)? I thought the only time exclusion of the index mentioned was when it is in the :x position?
##################
# The reason this is the case is because we want this to be True:
# IT_companies == IT_companies[:3] + IT_companies[3:]
##################
IT_companies = IT_companies[3:]
print(IT_companies)

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
IT_companies = IT_companies[0:-3]
print(IT_companies)

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del IT_companies[3:4]
print(IT_companies)

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del IT_companies[0]
print(IT_companies)

IT_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del IT_companies[-1]
print(IT_companies)

IT_companies.clear()
print(IT_companies)

del IT_companies


front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node', 'Express','MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
print('full_stack = ',full_stack)

print(full_stack)
print('index of redux =', full_stack.index('Redux'))
full_stack.insert(5, 'SQL')
full_stack.insert(5, 'Python')
print(full_stack)

# Let's create an empty list
my_list = []
print(my_list)

# Let's add some values
my_list.append("Python")
my_list.append("is ok")
my_list.append("sometimes")
print(my_list)

# Let's remove 'sometimes'
my_list.remove("sometimes")
print(my_list)

# Let's change the second item
my_list.append("sometimes")
my_list[1] = "is neat"
print(my_list)

original = ["I", "am", "learning", "hacking", "in"]
modified = original.copy()
modified.append('python')
print('original = ',original)
print('modified = ',modified)

list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]
# Your implementation here
my_list = list1+list2+list3
my_list.sort()
print(my_list)