# Method: hash table - not yet working
# Use hash table is not a good solution for this problem, this method is complicated

def encode_string(input_str):
  if input_str is None:
    return None

  if len(input_str) <= 2:
    return input_str

  input = list(input_str)

  record = {}
  for p in range(0, len(input)):
    if input[p] not in record:
      record[input[p]] = []
      record[input[p]].append(1)
    else:
      if input[p] == input[p-1]:
        record[input[p]][-1] += 1
      else:
        record[input[p]].append(1)

  output_str = ""
  for i in input_str:
    if len(record[i]) > 0:
      rec = record[i].pop(0)
    else:
      rec = 0

    if rec == 0:
      continue
    elif rec == 1:
      output_str += "{0}".format(i)
    elif rec == 2:
      output_str += "{0}{0}".format(i, i)
    else:
      output_str += "{0}{1}".format(i, rec)
     
  return output_str
  

if __name__ == "__main__":
  test_str = "abaaabbdeaaaaxdd"
  expected_result = "aba3bbdea4xdd"
  print("expected result: {0}".format(expected_result))
  your_result = encode_string(test_str)
  print("Your result: {0}".format(your_result))
  assert(expected_result == your_result)
