import unittest
import pprint
import json

from trello import Trello
from mock import Mock
from mock import patch
from mock import PropertyMock

class TrelloTestCase(unittest.TestCase):
    """Trello Api tester"""

    TEST_TOKEN = "36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe"
    TEST_BOARD_ID = "54d10ee46bd364a1e6f063ea"
    TEST_CARD_ID = "54d10f4c8777eefd6328ad43"

    def setUp(self):
        self.trello = Trello(TrelloTestCase.TEST_TOKEN)

    def test01_getRecords_unit(self):
        self.trello.make_call = Mock()
        self.trello.make_call.return_value.json.return_value = {'record':'some record'}
        print("User Records:")
        pprint.pprint(self.trello.get_records())
        assert self.trello.record == {'record' : 'some record'}


    # def test02_getAllBoards_unit(self):
    #     print("User Boards:")
    #     mock = Mock()
    #     #self.trello.get_all_boards = Mock(return_value={"boards":"Got boards!"})
    #     pprint.pprint(self.trello.get_all_boards(mock))
    #     mock.requests.get.assert_called_with()
    #     #assert self.trello.boards == {"boards":"Got boards!"}
    #
    #
    # def test03_getAllBoards_integrate(self):
    #     print("User Boards:")
    #     pprint.pprint(self.trello.get_all_boards())

    # def test03_getBoard(self):
    #     print("User Test Board:")
    #     pprint.pprint(self.trello.get_board(TrelloTestCase.TEST_BOARD_ID))
    #
    # def test04_getAllCards(self):
    #     print ("Cards:")
    #     pprint.pprint(self.trello.get_all_cards())
    #
    # def test05_getCard(self):
    #     print("User Test Card:")
    #     pprint.pprint(self.trello.get_card(TrelloTestCase.TEST_CARD_ID))
    #
    # def test06_getLists(self):
    #     print("User Lists:")
    #     pprint.pprint(self.trello.get_lists())
    #
    # def test07_getMembers(self):
    #     print("User Members:")
    #     pprint.pprint(self.trello.get_members())
    #
    # def test08_getLabels(self):
    #     print("User Labels:")
    #     pprint.pprint(self.trello.get_labels())

if __name__ == "__main__":
    unittest.main()