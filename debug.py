def find_max(a, b, c):
  max_number = a
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
   return b
  else:
    return c                    
def main():
  #FREEZE CODE BEGIN
 x = int(input("Enter a number:\n"))
 y = int(input("Enter a number:\n")) 
 z = int(input("Enter a number:\n"))
#FREEZE CODE END
 maximum = find_max(x, y, z)

 print(f"Maximum value: {maximum}")
if __name__ == "__main__":
    main()