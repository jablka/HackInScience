def missing_card(cards):

    cards = set(cards.split(' '))

    color = { "S", "H", "D", "C" }
    rank = { '2','3','4','5','6','7','8','9','10','J','Q','K', 'A'}
    
    deck = set()
    for c in color:
        for r in rank:
            deck.add( c+r )
    
    return ''.join(deck - cards)
