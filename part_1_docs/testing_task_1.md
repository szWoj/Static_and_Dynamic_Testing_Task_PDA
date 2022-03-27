### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# __init__() missing

  def check_for_ace(self, card):
    if card.value = 1: #it should be comparison not assignment
      return True
    else # ":" missing after "else"
      return False
   

  dif highest_card(self, card1 card2): #1.def misspelled, 2. "," missing
  if card1.value > card2.value:
    return card #card1 instead of card
  else:
    return card2
  #elif missing for condition when card1 == card2


def cards_total(self, cards):
  total #total variable must be assigned to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total #return indented "too far"
  
```
