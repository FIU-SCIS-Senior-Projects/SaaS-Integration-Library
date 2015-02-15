#from trello import TrelloApi
import requests

#Developer API Key = 36fb61b8a99b93c4cbf0b63a5f440503
#Test Token = 36b68eef1b52420e5731962cdb0bef1e8f152874b10f6036ed30bd9f117dc2fe

class Trello(object):
    """Trello API class"""
    TRELLO_KEY = "36fb61b8a99b93c4cbf0b63a5f440503"

    #TODO: Card, List, Label, Member

    def __init__(self, token):
        self.credentials = {'key': Trello.TRELLO_KEY, 'token': token}
        self.record = None
        self.boards = None
        self.cards = None

    def get_records(self):
        resp = requests.get("https://trello.com/1/members/me", params=self.credentials)
        self.record = resp.json()
        return self.record

    def get_all_boards(self):
        resp = requests.get("https://trello.com/1/members/my/boards", params=self.credentials)
        self.boards = resp.json()
        return self.boards

    def get_board(self, id):
        resp = requests.get("https://trello.com/1/boards/{board_id}".format(board_id=id), params=self.credentials)
        return resp.json()

    def get_all_cards(self):
        self.cards = {}

        #check if boards contains any boards to get board ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            resp = requests.get("https://trello.com/1/boards/{board_id}/cards".format(board_id=board['id']), params=self.credentials)
            self.cards[board['id']] = resp.json()

        return self.cards