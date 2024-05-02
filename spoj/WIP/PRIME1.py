while True:
  tests = int(input())
  test_cases = []
  for single_test in range(0, tests):
    test_cases.append(input())
  for single_case in range(0, len(test_cases)):
    prime_range = test_cases[single_case].split(' ')
    numbers = range(int(prime_range[0]), int(prime_range[1])+1)
    prime_numbers = []
    for single_number in numbers:
      # 1,2,3,5,7
      # 1,2,3,5,7,11,13,17,19
      # 4,6,8,9,10,12,14,15,16,18
      if single_number == 1:
        pass
      elif single_number in [2,3,5,7]:
        prime_numbers.append(str(single_number))
      elif single_number % 2 == 0 or single_number % 3 == 0 or single_number % 5 == 0 or single_number % 7 == 0:
        pass
      elif single_number % 2 == 1 or single_number % 3 == 1:
        prime_numbers.append(str(single_number))
    print('\n'.join(prime_numbers))
    if single_case != len(test_cases)-1:
      print()
  break