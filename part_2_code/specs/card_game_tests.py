import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        
        self.card1 = Card("hearts", 1)
        self.card2 = Card("hearts", 2)
        self.card3 = Card("clubs", 3)
        self.card4 = Card("hearts", 3)
        
        self.cards1 = [self.card1, self.card2]
        self.cards2 = [self.card3, self.card4]
        
        self.card_game1 = CardGame()
    
    def test_check_for_ace_true(self):
        result = self.card_game1.check_for_ace(self.card1)
        self.assertEqual(True, result)
    def test_check_for_ace_false(self):
        result = self.card_game1.check_for_ace(self.card2)
        self.assertEqual(False, result)
    def test_highest_card_card1(self):
        result = self.card_game1.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)
    def test_highest_card_card2(self):
        result = self.card_game1.highest_card(self.card3, self.card1)
        self.assertEqual(self.card3, result)
    def test_highest_card_card3(self):
        result = self.card_game1.highest_card(self.card3, self.card4)
        self.assertEqual("Value is the same", result)
    def test_cards_total(self):
        result = self.card_game1.cards_total(self.cards1)
        self.assertEqual('You have a total of 3', result)
