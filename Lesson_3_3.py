def my_func(arg1, arg2, arg3):
   return sum(sorted([arg1, arg2, arg3])[1:])

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')