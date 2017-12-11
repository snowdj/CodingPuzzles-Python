# Method: running check
def encode_string(input_str):
  if input_str is None:
    return None

  if len(input_str) <= 2:
    return input_str

  input = list(input_str)
  output = []
  rep_cnt = 1
  for i in range(1, len(input)):
    if input[i] == input[i-1]:
      rep_cnt += 1
    else:
      output.append((input[i-1], rep_cnt))
      rep_cnt = 1
  if rep_cnt > 1:
    output.append((input[-1], rep_cnt))

  output_str = ""
  for item in output:
    if item[1] == 1:
      output_str += item[0]
    elif item[1] == 2:
      output_str += "{0}{0}".format(item[0])
    else:
      output_str += "{0}{1}".format(item[0], item[1])

  return output_str

if __name__ == "__main__":
  test_str = "abaaabbdeaaaaxdd"
  expected_result = "aba3bbdea4xdd"
  print("expected result: {0}".format(expected_result))
  your_result = encode_string(test_str)
  print("Your result: {0}".format(your_result))
  assert(expected_result == your_result)
