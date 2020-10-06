import unittest
from C11_name_function import get_formatted_name

class NamesTestCase ( unittest.TestCase):
    """Test Cases for name function """

    def test_first_last_name(self):
        """Do names like Janis Joplin Work """
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middel_last_name(self):
        formatted_name = get_formatted_name('Amit','Arora', 'Kumar')
        self.assertEqual(
            formatted_name, 'Amit Kumar Arora'
        )
if __name__ == '__main__':
    unittest.main()