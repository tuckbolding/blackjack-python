import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def create_deck():
    deck = [(rank, suit) for suit in SUITS for rank in RANK_VALUES]
    random.shuffle(deck)
    return deck


def draw_card(deck):
    if not deck:
        raise ValueError("Cannot draw from an empty deck")
    return deck.pop()


def hand_value(hand):
    total = sum(RANK_VALUES[rank] for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == "A")

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def format_hand(hand, hide_first=False):
    if hide_first and hand:
        cards = ["[Hidden]"] + [f"{rank} of {suit}" for rank, suit in hand[1:]]
    else:
        cards = [f"{rank} of {suit}" for rank, suit in hand]
    return ", ".join(cards)


def determine_outcome(player_score, dealer_score):
    if player_score > 21:
        return "You bust. Dealer wins."
    if dealer_score > 21:
        return "Dealer busts. You win!"
    if player_score > dealer_score:
        return "You win!"
    if player_score < dealer_score:
        return "Dealer wins."
    return "It's a tie."


def dealer_play(deck, dealer_hand):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    return dealer_hand


def player_turn(deck, player_hand, input_func=input, print_func=print):
    while hand_value(player_hand) < 21:
        choice = input_func("Hit or stand? (h/s): ").strip().lower()
        if choice in {"h", "hit"}:
            player_hand.append(draw_card(deck))
            print_func(
                f"You drew: {player_hand[-1][0]} of {player_hand[-1][1]}"
            )
            print_func(f"Your hand: {format_hand(player_hand)}")
            print_func(f"Your score: {hand_value(player_hand)}")
        elif choice in {"s", "stand"}:
            break
        else:
            print_func("Please enter 'h' to hit or 's' to stand.")
    return player_hand


def play_round(input_func=input, print_func=print):
    deck = create_deck()
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    print_func("\n--- New Round ---")
    print_func(f"Dealer hand: {format_hand(dealer_hand, hide_first=True)}")
    print_func(f"Your hand: {format_hand(player_hand)}")
    print_func(f"Your score: {hand_value(player_hand)}")

    if hand_value(player_hand) == 21:
        print_func("Blackjack or 21 on deal!")
    else:
        player_turn(deck, player_hand, input_func=input_func, print_func=print_func)

    player_score = hand_value(player_hand)

    if player_score <= 21:
        dealer_play(deck, dealer_hand)

    dealer_score = hand_value(dealer_hand)
    print_func(f"Dealer final hand: {format_hand(dealer_hand)}")
    print_func(f"Dealer score: {dealer_score}")
    print_func(f"Your final score: {player_score}")
    print_func(determine_outcome(player_score, dealer_score))


def play_game(input_func=input, print_func=print):
    while True:
        play_round(input_func=input_func, print_func=print_func)
        again = input_func("Play another round? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print_func("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
