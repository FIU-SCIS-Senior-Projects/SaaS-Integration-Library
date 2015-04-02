#from trello import TrelloApi
import requests
from itertools import izip
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
            resp = requests.get("https://trello.com/1/boards/{board_id}/cards".format(board_id=board['id']),
                                params=self.credentials)

            #for each card in board, add board id and then append to cards list
            for element in resp.json():
                element['boardName'] = board['name']
                self.cards.append(element)

        # Clean up fields: remove Labels, pos, Manualcoverattachment, idshort,
        # checkitemstates, descdata, idattachmentcover
        # join in other API Calls
        for card in self.cards:
            del card['labels']
            del card['pos']
            del card['manualCoverAttachment']
            del card['idShort']
            del card['checkItemStates']
            del card['descData']
            del card['idAttachmentCover']

            # replace idlist with list name
            list_id = card['idList']
            del card['idList']
            card['listName'] = self.get_list_name(list_id)

            # replace idmembers with member names
            member_ids = card['idMembers']
            del card['idMembers']
            card['memberNames'] = self.get_member_names(member_ids)

            # replace idlabels with label names
            label_ids = card['idLabels']
            del card['idLabels']
            card['labelNames'] = self.get_label_names(label_ids)

        return self.cards

    def get_lists(self):
        self.lists = []

        #check if have boards to get list ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            resp = requests.get("https://trello.com/1/boards/{board_id}/lists".format(board_id=board['id']), params=self.credentials)

            for element in resp.json():
                self.lists.append(element)

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

            #for each member in board, add board id and then append to members list
            for element in resp.json():
                element['boardId'] = board['id']
                self.members.append(element)

        return self.members


    def get_labels(self):
        self.labels = []

        #check if have boards to get ids from
        if self.boards == None:
            self.get_all_boards()

        for board in self.boards:
            resp = requests.get("https://trello.com/1/boards/{board_id}/labels".format(board_id=board['id']), params=self.credentials)
            for element in resp.json():
                self.labels.append(element)

        return self.labels

    def get_list_name(self, list_id):
        listName = ""

        # Need update procedure?
        if self.lists == None:
            self.get_lists()

        for list in self.lists:
            if list['id'] == list_id:
                listName = list['name']

        return listName

    def get_member_names(self, member_ids):
        member_names = []

        # Need update procedure?
        if self.members == None:
            self.get_members()

        for member in self.members:
            for member_id in member_ids:
                # make sure no duplicates
                if member['id'] == member_id and member['username'] not in member_names:
                    username = str(member['username'])
                    member_names.append(username)

        return member_names

    def get_label_names(self, label_ids):
        label_names = []

        # Need update procedure?
        if self.labels == None:
            self.get_labels()

        for label in self.labels:
            for label_id in label_ids:
                # if found id and the name is not blank string
                if label['id'] == label_id and label['name'] != "":
                    label_names.append(json.dumps(label['name']))

        return label_names