import re
while True:
  tests = int(input())
  test_cases = []
  for single_test in range(0, tests):
    test_cases.append(input())
  for single_case in range(0, len(test_cases)):
    pair = test_cases[single_case].split(' ')
    single_reversed = int(str(pair[0])[::-1])
    double_reversed = int(str(pair[1])[::-1])
    single_reversed = str(single_reversed + double_reversed)[::-1]
    print(re.sub("^0+", "", single_reversed))
  break