
#Write a python program to count the frequency of any specific word (in your domain) in the paragraph.
def count_word_frequency(paragraph,target_word):
    words = paragraph.split()
    word_count = 0
    for word in words:
        cleaned_word=word.strip(".,!?").lower()
        if cleaned_word==target_word.lower():
           word_count+=1
    return word_count
paragraph="Online game rental store is a website where the customers can rent games for a specific period of time. The users will be unable to acces the games after a limited period of time"
word=input("Enter the word to be searched : ")           
target_word=word
frequency=count_word_frequency(paragraph,target_word)
print(f"The word '{target_word}' appears {frequency} times in the paragraph.")

#Write a python program to display all the datatypes of selected specific elements in the paragraph
def identify_datatypes(paragraph,selected_elements):
    for element in selected_elements:
        if element in paragraph:
            value=paragraph[element]
            data_types=type(value).__name__
            print(f"Element:{element} | Value:{value}|Data Type:{data_types}")
paragraph={
    "name":"Rojal Treesa Joy",
    "Register_no":"2347249",
    "Domain_Name":"Online Game Rental Store",
    "Year":"2023"
           }
selected_elements=["name","Register_no","Domain_Name","Year"]
identify_datatypes(paragraph,selected_elements)

#Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.
def count_symbols(paragraph):
    alphabets=0
    digits=0
    special_symbols=0
    for char in paragraph:
        if char.isalpha():
            alphabets+=1
        elif char.isdigit():
            digits+=1
        else:
            special_symbols+=1
    return alphabets,digits,special_symbols
paragraph="Online game rental store is a website where the customers can rent games for a specific period of time. The users will be unable to acces the games after a limited period of time"
           
alphabets_counts,digital_count,special_symbols_count=count_symbols(paragraph)
print(f"Number of Alpha={alphabets_counts}")
print(f"Number of numbers/Nummeric digits:{digital_count}")
print(f"Number of Special Charcters:{special_symbols_count}")

#Create a Set with elements that consists of various data types (int, float, string, Boolean, etc. from your domain) and perform the functions pop(), clear(), discard() and del. Write the insights as docstring.
setss={1,'ram','A27',2015}
print(setss)
pop=setss.pop()
print(pop)
print(setss)
dis=setss.discard('A27')
print(dis)
print(setss)
setss.clear()
print(setss)
del setss

setss={1,'ram','A27',2015}
print(setss)

#Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.
setss_update={'C1','C2','C3','C4','C5','C6'}
 
setss.update(setss_update)
print(setss)

value={'C6', 'C2', 'C5', 'C4', 'ram', 'A27', 'C3', 'C1'}
set_desenting=sorted(value,reverse=True)
print("The set 'value' in set in decending order: ",set_desenting)

#Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.
id=input("Enter the customer ID : ")
name=input("Enter the customer name : ")
rating=input("Enter the rating out of 5 : ")

tuple=(id,name,rating)
print(tuple)

intval,strval,floatval=tuple
print("The interger value in tuple= ",intval)
print("The string value in the tuple= ",strval)
print("The float value in the tuple= ",floatval)

#Enter your domain name as characters and count any number of characters and print the count
domain=('o','n','l','i','n','e', 'g','a','m','e', 'r','e','n','t','a','l', 's','t','o','r','e')
count=0
n=input("The character to be counted : ")
for i in domain:
    if i==n:
        count+=1
print("Number of '",n,"' in the string is : ", count)

#Enter your domain name, execute all the slicing possibilities and also negative indexing.
domain='online game rental store'
print(domain)
print("The 'Domain' string after negative slicing : ",domain[-7:-2])
print("The 'Domain' string after slicing : ",domain[slice(8)])

