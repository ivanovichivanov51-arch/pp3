bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  x = 200
print(isinstance(x, int))