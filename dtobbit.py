def decToBinary(n):
  
    # String to store the binary representation
    bin = ""

    while n > 0:
        # Finding (n % 2) using bitwise AND operator
        # (n & 1) gives the least significant bit (LSB)
        bit = n & 1
        bin += str(bit)

        # Right shift n by 1 (equivalent to n = n // 2)
        # This removes the least significant bit (LSB)
        n = n >> 1

    return bin[::-1]

if __name__ == "__main__":
    n = 12
    print(decToBinary(n))
