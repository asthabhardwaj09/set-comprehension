#set comprehension

s={k**2 for k in range(1,11)}
print(s)

names=['astha','ravita','mukul']
first={name[0] for name in names}
print(first)