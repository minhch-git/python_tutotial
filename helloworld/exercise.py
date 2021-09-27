def top(): 
  print('     ----- ')
  print('  /         \\')
  print(' /           \\')

def bottom():
  print(' \\           /')
  print('  \\  _____  / ')

def line(): 
  print(' + ---------- + ')

def egg():
  top()
  bottom()
  print()

def cup(): 
  bottom()
  line()
  print()


def stop(): 
  top()
  print('|     stop    |')
  bottom()
  line()

if __name__ == '__main__':
  # main
  egg()
  cup()
  stop()

