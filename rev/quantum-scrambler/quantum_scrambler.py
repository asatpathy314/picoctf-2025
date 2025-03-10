import sys

def exit():
  sys.exit(0)


def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
  return L



def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return [[i] for i in range (35)]
def main():
  flag = [[i] for i in range (40)]
  cypher = scramble(flag)
  flag = []
  for i in range(len(cypher)-2):
    flag.append(((cypher[i][0])))
    flag.append(((cypher[i][-1])))
    print(flag)
  flag.append(((cypher[-2][0])))
  flag.append(((cypher[-1][0])))
  print(flag)

if __name__ == '__main__':
  main()
