import re
import sys
sys.set_int_max_str_digits(1000000000)
while True:
  tests = int(input())
  test_cases = []
  for single_test in range(0, tests):
    test_cases.append(input())
  for single_case in range(0, len(test_cases)):
    test_number = int(test_cases[single_case])
    binary = bin(test_number)[2:].zfill(8)
    binary = re.sub("^0+", "", str(binary))
    zeroes_in_binary = len(re.findall("0", binary))
    if test_number > 10:
      tens = int(test_number / 10)
    else:
      tens = 0
    print(tens)
    print(zeroes_in_binary)
    factorial_result = (2 * tens) + zeroes_in_binary
    print(factorial_result)
    print()
  break