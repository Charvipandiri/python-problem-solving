string = input()
reverse_str =""
for i in string:
  reverse_str = i + reverse_str
if string == reverse_str:
    print("Palindrome")
else:
  print("NOT Palindrome")  
