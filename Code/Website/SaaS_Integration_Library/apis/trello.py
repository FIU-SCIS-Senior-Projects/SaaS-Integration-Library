import requests
import json
import calendar
import datetime
import simplejson
import pprint
import sys
sys.path.append("/home/adam/")
from senior import secret

#from SaaS_Integration_Library import settings

class Trello(object):
    """Trello API class"""

    def __init__(self, token):
        self.credentials = {'key': secret.TRELLO_KEY, 'token': token}
        self.record = None
        self.boards = None
        self.cards = None
        self.lists = None
        self.members = None
        self.labels = None
        self.username = None
        self.mycards = None
        self.total_cards = 0
        self.due_in_seven = None
        self.cards_past_due = None

    def make_call(self, address):
        return requests.get(address, params=self.credentials)


    def get_records(self):
        resp = self.make_call("https://trello.com/1/members/me")
        self.record = resp.json()
        return self.record


    def set_username(self, username):
        self.username = username


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
        self.mycards = []
        self.due_in_seven = []
        self.cards_past_due = []

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
            self.total_cards += 1
            del card['labels']
            del card['pos']
            del card['manualCoverAttachment']
            del card['idShort']
            del card['checkItemStates']
            del card['descData']
            del card['idAttachmentCover']
            del card['badges']
            del card['id']
            del card['idBoard']
            del card['email']
            del card['shortLink']
            del card['idMembersVoted']

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

            # search through member names, if have mine then store in separate list
            if self.username is None:
                self.set_username(self.get_records()['username'])

            for member_name in card['memberNames']:
                if member_name == self.username:
                    self.mycards.append(card)

            # add to due in seven list or add to past due list
            if self.get_due_in_seven(card):
                self.due_in_seven.append(card)


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


    def get_cards_assigned_to_me(self):
        if self.mycards is None:
            self.get_all_cards()

        return self.mycards


    def get_total_cards(self):
        if self.cards is None:
            self.get_all_cards()

        return self.total_cards


    #TODO get due in 7 days, date on card example: 2015-04-20T16:00:00.000Z
    def get_due_in_seven(self, card):
        if card['due'] is not None:
            cur_date = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
            due = card['due'][:10].split('-')
            due_year = int(due[0])
            due_month = int(due[1])
            due_day = int(due[2])
            due_date = datetime.date(due_year, due_month, due_day)
            date_diff = due_date-cur_date

            if date_diff.days <= 7:
                if date_diff.days < 0:
                    self.cards_past_due.append(card)
                    return False
                return True

        return False


    #TODO get past due