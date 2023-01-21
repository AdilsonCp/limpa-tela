#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
while True:
    num = int(input("Digite um número: "))
    print(f"O número digitado foi {num}")
    print("Digite 999 para encerrar")
    if num == 999:
        break
    time.sleep(2)
    os.system("cls") or None
print("Fim")


# In[ ]:




