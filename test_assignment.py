import unittest
from io import StringIO
import sys

class TestControlStructures(unittest.TestCase):

    def test_while_loop(self):
        # Test if the while loop prints even numbers up to 20 and stops at 16
         # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # While loop prints even numbers up to 20 but stops at 16
        num = 2
        while num <= 20:
            print(num)
            if num == 16:
                pass
            num += 2
        

    def test_for_loop_continue(self):
        # Test if the for loop skips numbers divisible by 3
         # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # For loop skips numbers divisible by 3
        for num in range(1, 11):
            if num % 3 == 0:
                continue
            print(num)

        # Restore stdout
        sys.stdout = sys.__stdout__
        pass

    def test_if_else(self):
        # Test if the if-else statement categorizes numbers correctly
        # Function to categorize numbers
        def categorize_number(n):
            if n > 0:
                return "Positive"
            elif n < 0:
                return "Negative"
            else:
                return "Zero"

        self.assertEqual(categorize_number(10), "Positive")
        self.assertEqual(categorize_number(-5), "Negative")
        self.assertEqual(categorize_number(0), "Zero"
        pass

    def test_nested_loops(self):
        # Test if the nested loops generate the correct multiplication table
         # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Generate multiplication table (1 to 3)
        for i in range(1, 4):
            for j in range(1, 4):
                print(i * j, end=" ")
            print()

        # Restore stdout
        sys.stdout = sys.__stdout__

        pass

if __name__ == "__main__":
    unittest.main()