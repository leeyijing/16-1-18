class allredemption:
    def __init__(self, date, bank_card,card_no, item,qty, redeemed_pt,status):
        self.__date = date
        self.__bank_card = bank_card
        self.__card_no = card_no
        self.__item = item
        self.__qty = qty
        self.__redeemed_pt = redeemed_pt
        self.__status = status

    def get_date(self):
        return self.__date

    def get_bank_card(self):
        return self.__bank_card

    def get_card_no(self):
        return self.__card_no

    def get_item(self):
        return self.__item

    def get_qty(self):
        return self.__qty

    def get_redeemed_pt(self):
        return self.__redeemed_pt

    def get_status(self):
        return self.__status

    def set_date(self, date):
        self.__date = date

    def set_bank_card(self, bank_card):
        self.__bank_card = bank_card

    def set_card_no(self, card_no):
        self.__card_no = card_no

    def set_item(self, item):
        self.__card_no = item

    def set_qty(self,qty):
        self.__qty = qty

    def set_redeemed_pt(self,redeemed_pt):
        self.__redeemed_pt = redeemed_pt

    def set_status(self, status):
        self.__status = status
