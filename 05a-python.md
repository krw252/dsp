# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

 >> Python lists and tuples are both compound data types which are used to group together values. However, lists are mutable and typically contain homogeneous data structures while tuples are immutable and typically contain heterogeneous data structures. Their syntax also varies with lists being enclosed by square brackets while tuples are enclosed by standard parentheses.  Since dictionaries keys require immutable elements, only tuples will work as keys so long as its objects are immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are both mutable compound data types used to group together values.  Lists are ordered whereas sets are unordered.  Moreover, sets do not have duplicate values. In terms of syntax, lists use square brackets while sets use curly braces or the set() function.

>>List Example: 
```python
domesticated_animals = ['cat', 'dog', 'hamster', 'lizard']
Set Example: zoo_animals = set(['elephant', 'giraffe', 'gazelle', 'gorilla'])
```
>>It is faster to find an element within a set as sets use hashtables as their underlying data structure.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' expressions create small anonymous functions using the lambda keyword.  They are generally used as arguments within other, named functions but can be used whenever we require a temporary, nameless function. The syntax for a lambda expressions is lambda x,y: func(x,y)

>>Example using a 'lambda' with the 'sorted' function:
```python
zoo_inventory = [('zebra', 5), ('giraffe', 2), ('gorilla', 3), ('humans', 800)]
sorted(zoo_inventory, key=lambda age:age[1]) #sort by number of animals
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to define and create a list in Python in which a method iterates over another list to output a new list as defined by the applied method.  For example, the list comprehension list(x for x in range(0,51) if x % 2 == 0) will iterate over the range(0,51) and return a list of numbers which satisfy the 'if' criteria (divisible by 2).  List comprehensions and 'map' and 'filter' functions can do very similar things but vary in terms of readability and sometimes speed.

>> Example of LC v. 'map'
```python
#sqr each number in a defined list
numbers = [1,2,3,4,5,6,7,8,9,10]
lc_sqr = [x ** 2 for x in numbers]
map_sqr = list (map(lambda x: x**2, numbers))
```

>> Example of LC v. 'filter'
```python
#filter for only even numbers in a defined list
numbers = [1,2,3,4,5,6,7,8,9,10]
lc_evens = [x for x in numbers if x % 2 == 0]
filter_evens = list(lambda x: x % 2 == 0, numbers)
```
>> Example of set comprehension
```python
#dedupe and sort a list
numbers = [1,1,1,5,2,1,15,2,22,32]
set_comp = {n for n in numbers}
```
>> Example of dictionary comprehension
```python
#return dictionary with key of abc and value of 0-4
abc = ['a','b','c','d','e']
dict_comp = {k: v for (k,v) in zip(abc, range(4))}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





