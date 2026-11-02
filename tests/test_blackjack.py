import unittest

from blackjack import dealer_play, determine_outcome, hand_value


class TestBlackjackLogic(unittest.TestCase):
    def test_hand_value_ace_as_eleven(self):
        hand = [("A", "Spades"), ("9", "Hearts")]
        self.assertEqual(hand_value(hand), 20)

    def test_hand_value_ace_adjusts_to_one(self):
        hand = [("A", "Spades"), ("9", "Hearts"), ("K", "Clubs")]
        self.assertEqual(hand_value(hand), 20)

    def test_hand_value_multiple_aces_adjust(self):
        hand = [("A", "Spades"), ("A", "Hearts"), ("9", "Clubs")]
        self.assertEqual(hand_value(hand), 21)

    def test_dealer_draws_until_at_least_17(self):
        dealer_hand = [("10", "Hearts"), ("2", "Spades")]
        deck = [("9", "Diamonds"), ("5", "Clubs")]
        final_hand = dealer_play(deck, dealer_hand)
        self.assertEqual(hand_value(final_hand), 17)

    def test_outcome_player_busts(self):
        self.assertEqual(determine_outcome(22, 18), "You bust. Dealer wins.")

    def test_outcome_dealer_busts(self):
        self.assertEqual(determine_outcome(20, 22), "Dealer busts. You win!")

    def test_outcome_tie(self):
        self.assertEqual(determine_outcome(19, 19), "It's a tie.")


if __name__ == "__main__":
    unittest.main()
