fruits= ["apple", "banana", "cherry", "blueberry"]
longest_fruit= fruits [0]
for fruit in fruits: 
 if len(fruit) > len(longest_fruit):
     longest_fruit=fruit 
     
print("the longest word is ",  longest_fruit)
 