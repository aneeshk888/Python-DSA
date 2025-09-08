import math

def floorceildiv(a,b):

  floor_val=math.floor(a/b)
  ceil_val=math.ceil(a/b)
  return [floor_val,ceil_val]

if  __name__ == "__main__":
 a,b=5,3
 res=floorceildiv(a,b)
 print(res[0],res[1])
