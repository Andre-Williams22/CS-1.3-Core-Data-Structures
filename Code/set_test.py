from sets import Treeset 
import unnitest



class TestTreeset(unnittest.TestCase):

    def test_init(self):
        data = 123
        tree = Treeset(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None
    

    def test_add(self, element):
        # Create node with no children
        pass












if __name__ == 'main':
    unnitest.main()