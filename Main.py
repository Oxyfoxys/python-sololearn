print('save me')
print('rise revolution')
print("shattered pices")
print("from all this pain in the world")
print("i dont understand")


a = 1

while a < 5:
   print('условие верно ' + str(a) )
   a = a + 1
else:
   print('условие неверно ' +str(a) )

   print(2 + 2)
   print(5 + 4 - 3)

   print(2 * (3 + 4))
   print(10 / 2)

   print(3 / 4)
   print(0.42)

   print(8 / 2)

   print(6 * 7.0)

   print(4 + 1.65)

   print(1 + 2 + 3 + 4.0 + 5)

   print(2 ** 5)

   print(9 ** (1 / 2))

   print(10//4)

   print(20 % 6)

   print(1.25 % 0.5)

   print(7 % (5 // 2))

   print((3 ** 2) // 2)

   print('Coding in Finance')

   print("An investment in knowledge pays the best interest.")

   print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

   print('One\nTwo\nThree')

   print("""this
   is a
   multiline
   text""")

   print("Spam" + 'eggs')

   print("2" + "2")

print("spam" * 3)

print(4 * '2')

x = 7
print(x)

print(x + 3)

print(x)

x = 123.456
print(x)

x = "This is a string"
print(x + "!")

age = 42
print("His age is " + str(age))

x = '2'
y = '4'
z = int(x) + int(y)
print(z)

x = 2
print(x)

x += 3
print(x)

x = "spam"
print(x)

x += "eggs"
print(x)

print(17 % 3)

my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello")

print(1 != 1)

print("eleven" != "seven")

print(2 != 10)

print(7 > 5)

print(10 < 10)

if 10 > 5:
    print("10 greater than 5")

print("Program ended")

spam = 7
if spam > 5:
   print("five")
if spam > 8:
   print("eight")

x = 4
if x == 5:
    print("Yes")
else:
    print("No")

    num = 3
    if num == 1:
       print("One")
    else:
       if num == 2:
          print("Two")
       else:
          if num == 3:
             print("Three")
          else:
             print("Something else")

          num = 3
          if num == 1:
             print("One")
          elif num == 2:
             print("Two")
          elif num == 3:
             print("Three")
          else:
             print("Something else")

          print(1 == 1 and 2 == 2)

          print(1 == 1 and 2 == 3)

          print(1 != 1 and 2 == 2)

          print(2 < 1 and 3 > 6)

    print(1 == 1 or 2 == 2)

    print(1 == 1 or 2 == 3)

    print(1 != 1 or 2 == 2)

    print(2 < 1 or 3 > 6)

    print(not 1 == 1)

    print(not 1 > 7)


print(False == False or True)

print(False == (False or True))

print((False == False) or True)

grade = 88
if(grade >= 70 and grade <= 100):
    print("Passed!")

    words = ["Hello", "world", "!"]
    print(words[0])
    print(words[1])
    print(words[2])

    empty_list = []
    print(empty_list)

    number = 3
    things = ["string", 0, [1, 2, number], 4.56]
    print(things[1])
    print(things[2])
    print(things[2][2])

    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(m[1][2])

    str = "Hello world!"
    print(str[6])

    nums = [7, 7, 7, 7, 7]
    nums[2] = 5
    print(nums)

    nums = [1, 2, 3]
    print(nums + [4, 5, 6])
    print(nums * 3)

    words = ["spam", "egg", "spam", "sausage"]
    print("spam" in words)
    print("egg" in words)
    print("tomato" in words)

    nums = [10, 9, 8, 7, 6, 5]
    nums[0] = nums[1] - 5
    if 4 in nums:
        print(nums[3])
    else:
        print(nums[4])

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

nums = [1, 2, 3]
nums.append(4)
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))

items = [2, 4, 6, 8, 10, 12, 14]

num = len(items) // 2
print(num)

letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

i = 3
while i>=0:
   print(i)
   i = i - 1


i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)


  words = ["hello", "world", "spam", "eggs"]
  for word in words:
      print(word + "!")

      str = "testing for loops"
      count = 0

      for x in str:
          if (x == 't'):
              count += 1

      print(count)

      list = [2, 3, 4, 5, 6, 7]

      for x in list:
          if (x % 2 == 1 and x > 4):
              print(x)
              break




for i in range(5):
    print("hello!")

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

print("Hello world!")
range(2, 20)

range(10, 20, 3)


def my_func():
    print("spam")
    print("spam")
    print("spam")


my_func()


def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

def print_double(x):
   print(2 * x)

print_double(3)


def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)


def function(variable):
    variable += 1
    print(variable)

function(7)
print("variable")


def max(x, y):
    if x >= y:
        return x
    else:
        return y


print(max(4, 7))
z = max(8, 5)
print(z)


def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")


print(add_numbers(4, 5))

x = 365
y = 7
# this is a comment

print(x % y)  # find the remainder


# print (x // y)
# another comment

def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")


shout("spam")