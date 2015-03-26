#from trello import TrelloApi
import requests
import json
import simplejson
import pprint
#from SaaS_Integration_Library import settings

class Trello(object):
    """Trello API class"""
    TRELLO_KEY = "36fb61b8a99b93c4cbf0b63a5f440503"

    def __init__(self, token):
        self.credentials = {'key': Trello.TRELLO_KEY, 'token': token}
        self.record = None
        self.boards = None
        self.cards = None
        self.lists = None
        self.members = None
        self.labels = None

    def make_call(self, address):
        return requests.get(address, params=self.credentials)

    def get_records(self):
        resp = self.make_call("https://trello.com/1/members/me")
        self.record = resp.json()
        return self.record

    def get_all_boards(self):
        resp = requests.get("https://trello.com/1/members/my/boards", params=self.credentials)
        self.boards = resp.json()
        return self.boards

    def get_board(self, id):
        resp = requests.get("https://trello.com/1/boards/{board_id}".format(board_id=id), params=self.credentials)
        return resp.json()

    def get_card(self, id):
        resp = requests.get("https://trello.com/1/cards/{card_id}".format(card_id=id), params=self.credentials)
        return resp.json()

    def get_all_cards(self):
        self.cards = []

        #check if boards contains any boards to get board ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            cardinfo = {}
            resp = requests.get("https://trello.com/1/boards/{board_id}/cards".format(board_id=board['id']),
                                params=self.credentials)
            cardinfo['boardId'] = board['id']
            cardinfo['cards'] = resp.json()
            self.cards.append(cardinfo)

        return self.cards

    def get_lists(self):
        self.lists = []

        #check if have boards to get list ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            listinfo = {}
            resp = requests.get("https://trello.com/1/boards/{board_id}/lists".format(board_id=board['id']), params=self.credentials)
            listinfo['boardId'] = board['id']
            listinfo['lists'] = resp.json()
            self.lists.append(listinfo)

        return self.lists

    #members for all boards
    def get_members(self):
        self.members = []

        #check if have boards to get ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            memberinfo = {}
            resp = requests.get("https://trello.com/1/boards/{board_id}/members".format(board_id=board['id']), params=self.credentials)
            memberinfo['boardId'] = board['id']
            memberinfo['members'] = resp.json()
            self.members.append(memberinfo)

        return self.members


    def get_labels(self):
        self.labels = []

        #check if have boards to get ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            labelinfo = {}
            resp = requests.get("https://trello.com/1/boards/{board_id}/labels".format(board_id=board['id']), params=self.credentials)
            labelinfo['boardId'] = board['id']
            labelinfo['labels'] = resp.json()
            self.labels.append(labelinfo)

        return self.labels

