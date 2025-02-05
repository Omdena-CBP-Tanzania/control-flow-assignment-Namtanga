import unittest
from io import StringIO
import sys

class TestControlStructures(unittest.TestCase):

    def test_while_loop(self):
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # While loop prints even numbers up to 20 but stops at 16
        num = 2
        while num <= 20:
            print(num)
            if num == 16:
                break
            num += 2

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Expected output
        expected_output = "2\n4\n6\n8\n10\n12\n14\n16\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_for_loop_continue(self):
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

        # Expected output
        expected_output = "1\n2\n4\n5\n7\n8\n10\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_if_else(self):
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
        self.assertEqual(categorize_number(0), "Zero")

    def test_nested_loops(self):
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

        # Expected output
        expected_output = "1 2 3 \n2 4 6 \n3 6 9 \n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
