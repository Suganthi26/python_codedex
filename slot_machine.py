# Slot MAchine

import random
symbols = ['🍒',' 🍇', '🍉', '7️⃣']
results = random.choices(symbols, k = 3)

print ('|' .join(results) )

if all(item == '7️⃣' for item in results):
  print ('Jackpot!')
else:
  print('Thanks for playing!')
