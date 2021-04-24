i = 7
k = i
while i >= 1:
    print(" " * (k - i) + "*" * i)
    i -= 1 

"""
0
1
2
3
4
5 
"""
baseLayer = 5
i = 0

while i <= baseLayer - 1:
    print(i)
    i += 1
    print(i * "" + (baseLayer - i) * "*" )
    i += 1

    """
***** => 0 space, 5 stars
 **** => 1 space, 4 stars
  *** => 2 spaces, 3 stars
   ** => 3 spaces, 2 stars
    * => 4 spaces, 1 star
"""