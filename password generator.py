import itertools

def generate_passwords(numbers):
  """Generates all possible 6 digit passwords for the given numbers."""
  for password in itertools.product(numbers, repeat=6):
    yield "".join(password)

def main():
  """Prints all the possible 6 digit passwords for the given numbers."""
  numbers = input("Enter the numbers: ")
  for password in generate_passwords(numbers):
    print(password)

if __name__ == "__main__":
  main()
