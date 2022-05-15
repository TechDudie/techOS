import sys
from tokens import Tokenizer

try:
  file = open(sys.argv[1]).read()
except:
  print("File not found.")
  exit()

