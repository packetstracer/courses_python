import pdb


def digits(x):
  """ Return de number of digits of an integer

  Args:
    x: the integer to check

  Returns: a list of the digits (12367 -> [1,2,3,6,7])
  """
  digs = []

  # this sentence stops de debugger
  pdb.set_trace()

  while x != 0:
    div, mod = divmod(x, 10)
    digs.append(mod)
    x = div

  return digs


def is_palyndrome(x):
  """Determine if an integer is a palyndrome.

  Args:
    x: the integer to check

  Returns: if integer is palyndrome
  """
  digs = digits(x)

  for f, r in zip(digs, reversed(digs)):
    if f != r:
      return False

  return True


# invoke the script with pdb option -> python3 -m pdb palyndrome.py
print(is_palyndrome(1001))
print(is_palyndrome(14671))