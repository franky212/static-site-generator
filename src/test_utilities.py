import unittest
from utilities import extract_title

class TestUtilities(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# This is a **bolded** title
"""
        markdown2 = """
## This is not a title

# This is a title
"""
        markdown3 = """

"""
        result = extract_title(markdown)
        result2 = extract_title(markdown2)
        self.assertEqual("This is a **bolded** title", result)
        self.assertEqual("This is a title", result2)
        with self.assertRaises(Exception):
            extract_title(markdown3)


if __name__ == "__main__":
    unittest.main()
