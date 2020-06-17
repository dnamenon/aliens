from main import AlienInvasion
from settings import Settings
import unittest



class TestsforAliens(unittest.TestCase):

    def test_bgcolor(self):
        self.ai = AlienInvasion()
        self.set = Settings()
        self.result = self.ai.screen.get_at((0,0))
        self.ogcolor = self.set.bg_color
        self.assertEqual(self.result,self.ogcolor)
        print(self.ogcolor)
        print(self.result)


if __name__ == '__main__':
    unittest.main()


