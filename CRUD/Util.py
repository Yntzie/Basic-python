import random
import string

def randomString(panjang:int) -> str:
  hasil_random = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
  
  return hasil_random