class card():
  """this creates a card object"""

  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] 
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
  
  def __init__(self,rank=0,suite=2):
  
    self.rank = rank
    self.suite =  suite
  
  def __str__(self):
    return "the rank is {rank_names[self.rank]} and the suit is {suit_name[self.suit]}"

ace_of_spade = card(1,3)

print(ace_of_spade)