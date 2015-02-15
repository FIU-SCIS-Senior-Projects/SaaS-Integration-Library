from trello import Trello
import unittest
import pprint

class TrelloTestCase(unittest.TestCase):
    """Trello Api tester"""

    TEST_TOKEN = "36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe"
    TEST_BOARD_ID = "54d10ee46bd364a1e6f063ea"

    def setUp(self):
        self.trello = Trello(TrelloTestCase.TEST_TOKEN)

    def test01_getRecords(self):

        print("User Records:")
        pprint.pprint(self.trello.get_records())

    def test02_getAllBoards(self):
        print("User Boards:")
        pprint.pprint(self.trello.get_all_boards())

    def test03_getBoard(self):
        print("User Test Board:")
        pprint.pprint(self.trello.get_board(TrelloTestCase.TEST_BOARD_ID))

    def test04_getAllCards(self):
        print ("Cards:")
        pprint.pprint(self.trello.get_all_cards())


if __name__ == "__main__":
    unittest.main()