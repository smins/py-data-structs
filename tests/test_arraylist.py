""" Practice unit tests for ArrayList implementation """
import pytest
import arraylist

# pylint:disable=redefined-outer-name,no-self-use
@pytest.fixture
def array_list():
    """ Performs initial ArrayList setup for test cases """
    return arraylist.ArrayList()

class TestArrayList:
    """ Test Class for ArrayList """
    def test_default_size(self, array_list):
        """ Tests the default size of an ArrayList """
        assert array_list.size == 2**20

    def test_default_max_size(self, array_list):
        """ Tests the default max size of an ArrayList """
        assert array_list.max_size == 2**40

    def test_append(self, array_list):
        """ Tests appending a value to the list """
        array_list.append('this is a test')
        assert array_list.get(0) == 'this is a test'

    def test_set_val(self, array_list):
        """ Tests setting a value at a specified in-bounds index in the list """
        array_list.set('always look on the bright side of life', 90)
        assert array_list.get(90) == 'always look on the bright side of life'

    def test_set_growth(self):
        """ Tests setting a value at a specified out-of-bounds index, causing growth """
        array_list = arraylist.ArrayList(size=100)
        array_list.set('this is a test', 150)
        assert array_list.get(150) == 'this is a test'
        assert array_list.size > 100

    def test_get_val(self, array_list):
        """ Tests setting and retrieving a value """
        array_list.set('testing is rad', 66)
        assert array_list.get(66) == 'testing is rad'

    def test_delete_val(self, array_list):
        """ Tests setting an deleting a value """
        for val in range(0, 6):
            array_list.set(val, val)

        assert array_list.get(3) == 3
        initial_size = array_list.size

        array_list.delete(3)

        assert array_list.get(3) == 4
        end_size = array_list.size

        assert initial_size > end_size

    def test_auto_growth(self):
        """ Tests that the ArrayList will grow correctly """
        array_list = arraylist.ArrayList(size=10)

        import string
        for char in string.ascii_letters:
            array_list.append(char)

        assert array_list.get(25) == 'z'
        assert array_list.get(51) == 'Z'

    def test_growth_factor(self, array_list):
        """ Tests the growth_factor param of _grow_array() """
        assert array_list.size == 2**20
        # pylint: disable=protected-access
        array_list._grow_array(growth_factor=2**3)
        assert array_list.size == 2**23

    def test_get_oob(self):
        """ Test that oob index access on ArrayList raises an IndexError """
        array_list = arraylist.ArrayList(size=50)
        with pytest.raises(IndexError):
            array_list.get(100)

    def test_for_each(self):
        """ Test that for-each iteration works for ArrayLists """
        array_list = arraylist.ArrayList(size=100)

        import string
        for char in string.ascii_letters:
            array_list.append(char)

        for char in array_list:
            assert char is None or char in string.ascii_letters
