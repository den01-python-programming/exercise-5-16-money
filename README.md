# Exercise 5.16 Money

In the Payment card exercise we used an object variable to store the amount of money. A more reasonable way to handle amounts of money is create an own class for that purpose. Here is a layout for the class:

```python
class Money:

    def __init__(self, pounds, pence):
        self.pounds = pounds
        self.pence = pence

    def pounds(self):
        return self.pounds

    def pence(self):
        return self.pence

    def __str__(self):
        zero = ""
        if (self.pence <= 10):
            zero = "0"

        return str(self.pounds) + "." + zero + str(self.pence) + "p"
```

Next we'll create a few operations for processing money.

## Plus

First create the method `def plus(self, addition)` that returns a new money object that is worth the total amount of the object whose method was called and the object that is received as the parameter.

The basis for the method is the following:

```python
def plus(self, addition):
    new_money = Money(...) # create a money object that has the correct worth

    # return the money object
    return new_money
```

Here are some examples of how the method works.

```python
a = Money(10,0)
b = Money(5,0)

c = a.plus(b)

print(a)  # 10.00p
print(b)  # 5.00p
print(c)  # 15.00p

a = a.plus(c)          # NB: a Money object is created, and is placed "at the end of the strand connected to a"
#  the old 10 pounds at the end of the strand disappears and the Java garbage collector takes care of it

print(a)  # 25.00p
print(b)  # 5.00p
print(c)  # 15.00p
```

## Less

Create the method `def less_than(self, other)` that returns true if the money-object on which the method is called on has a lesser value than the money object given as a parameter.


```python
a = Money(10, 0)
b = Money(3, 0)
c = Money(5, 0)

print(a.less_than(b))  # false
print(b.less_than(c))  # true
```

## Minus

Write the method `def minus(self, decreaser)` that returns a new money object worth the difference of the object whose method was called and the object received as the parameter. If the difference would be negative, the worth of the created money object is set to 0.

Here are examples of how the method works.

```python
a = Money(10, 0)
b = Money(3, 50)

c = a.minus(b)

print(a)  # 10.00p
print(b)  # 3.50p
print(c)  # 6.50p

c = c.minus(a)       # NB: a Money object is created, and is placed "at the end of the strand connected to c"
#  the old 6.5 pounds at the end of the strand disappears and the Java garbage collector takes care of it


print(a)  # 10.00p
print(b)  # 3.50p
print(c)  # 0.00p
```
