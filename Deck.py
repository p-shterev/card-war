class Deck:

    def __init__(self, current_card):
        self.current_card = current_card
        self.capture_card = []

    def size(self):
        return len(self.current_card) + len(self.capture_card)

    def can_draw_card(self, num=0):
        if self.size() == 0:
            return False

        if self.size() < num:
            return False

        if len(self.current_card) == 0:
            self.current_card.extend(self.capture_card[::-1])
            self.capture_card.clear()

        return True

    def draw_card(self):
        if self.can_draw_card():
            return self.current_card.pop(0)
        return False

    def show(self):
        print(self.current_card)
        print(self.capture_card)
