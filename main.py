import csv

from Deck import Deck

card_rank = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

players_deck = []


def read_file():
    item_count = {}
    with open("deck.csv", "r") as file:
        cvs_reader = csv.reader(file)
        count_card = 0
        for i, row in enumerate(cvs_reader):
            players_deck.append(row)
            count_card += len(row)
            for item in row:
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
        if count_card != 52:
            print("cards are not 52")
            exit()
        # Print the item counts
        for item, count in item_count.items():
            if count != 4:
                print(f"error with {item}")
                exit()


# def war2(curr_deck1, curr_deck2):
#     capture1 = []
#     capture2 = []
#     all_cards1 = len(curr_deck1)
#     all_cards2 = len(curr_deck2)
#
#     while all_cards1 and all_cards2:
#         if len(curr_deck1) == 0:
#             curr_deck1.extend(capture1)
#             capture1.clear()
#
#         if len(curr_deck2) == 0:
#             curr_deck2.extend(capture2)
#             capture1.clear()
#
#
#         card1 = curr_deck1.pop(0)
#         card2 = curr_deck2.pop(0)
#
#         rank1 = card_rank[card1]
#         rank2 = card_rank[card2]
#
#         if rank1 > rank2:
#             print("1")
#             capture1.append(card2)
#             capture1.append(card1)
#         elif rank1 < rank2:
#             print("2")
#             capture2.append(card1)
#             capture1.append(card2)
#         else:
#             print("war")
#             war_card1 = []
#             war_card2 = []
#             for i in range(3):
#                 war_card1.append(curr_deck1.pop(0))
#                 war_card2.append(curr_deck2.pop(0))
#
#         all_cards1 = len(curr_deck1) + len(curr_deck1)
#         all_cards2 = len(curr_deck2) + len(curr_deck2)


def game_engine(p1, p2):
    moves = 0
    while True:
        if not p1.can_draw_card():
            return
        if not p2.can_draw_card():
            return
        moves +=1
        card1 = p1.draw_card()
        card2 = p2.draw_card()
        print(moves)
        # p1.show()
        # p2.show()
        print("------")
        rank1 = card_rank[card1]
        rank2 = card_rank[card2]

        result = check(rank1, rank2)

        if result == -1:
            p1.capture_card.append(card2)
            p1.capture_card.append(card1)
        if result == 1:
            p2.capture_card.append(card1)
            p2.capture_card.append(card2)
        if result == 0:
            war(p1, p2, card1, card2)


def war(p1, p2, card1, card2):
    war_card1 = []
    war_card2 = []
    p1.show()
    p2.show()
    if not p1.can_draw_card(3):
        print("player 2 win")
        return
    if not p2.can_draw_card(3):
        print("player 1 win")
        return

    for i in range(3):
        drown_card1 = p1.draw_card()
        drown_card2 = p2.draw_card()
        war_card1.append(drown_card1)
        war_card2.append(drown_card2)
    result = check(card_rank[war_card1[-1]], card_rank[war_card2[-1]])
    print(card1,war_card1)
    print(card2,war_card2)
    if result == -1:
        p1.capture_card.extend(war_card2[::-1])
        p1.capture_card.extend(card2[::-1])
        p1.capture_card.extend(war_card1[::-1])
        p1.capture_card.extend(card1[::-1])

    if result == 1:
        p2.capture_card.extend(war_card1[::-1])
        p2.capture_card.extend(card1[::-1])
        p2.capture_card.extend(war_card2[::-1])
        p2.capture_card.extend(card2[::-1])

    if result == 0:
        war_card1.insert(0, card1)
        war_card2.insert(0, card2)
        war(p1, p2, war_card1, war_card2)
    p1.show()
    p2.show()


def check(card1, card2):
    if card1 > card2:
        return -1
    if card1 < card2:
        return 1
    if card1 == card2:
        return 0


if __name__ == "__main__":
    read_file()
    player1 = Deck(players_deck[0])
    player2 = Deck(players_deck[1])

    game_engine(player1, player2)
