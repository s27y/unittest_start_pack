import unittest
import os

class TestSample(unittest.TestCase):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # Something you only want to init once
    CLASS_LEVEL_OBJECT = None

    def setUp(self):
        if self.__class__.CLASS_LEVEL_OBJECT is None:
        configs = config_loader.load_test_config(
            os.path.join(__location__, 'test_config'))
        username = configs['username']
        password = configs['password']
#        self.__class__.CLASS_LEVEL_OBJECT = None
#        self.__class__.CLASS_LEVEL_OBJECT.do_something()

# Test sample data
#        with open(os.path.join(self.__class__.__location__, 'injectors/sample.xml'), 'r') as f:
#            site_xml = f.read()


    @unittest.skipUnless(os.path.isfile(os.path.join(__location__, 'test_config')),
            "For local testing only - requires test_config file")
    def test_run_locally(self):
        pass


if __name__ == '__main__':
    unittest.main()
