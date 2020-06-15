class Card {
    private int rank;
    private int suit;

    // suits = H D C S
    // ranks = 1234556792345678

    // Card(K, H)
    public Card(int suit, int rank) {
        this.rank = rank;
        this.suit = suit;
    }

    public String toString() {
        return rank + " of " + suit;
    }

    public Boolean isSameRank(Card cardOne, Card cardTwo) {
        if (cardOne.getSuit().equals(cardTwo.getSuit())) {
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public Boolean isSameSuit(Card cardOne, Card cardTwo) {
        if (cardOne.getRank().equals(cardTwo.getRank())) {
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public int getRank() {
        return rank;
    }

    public char getSuit() {
        return suit;
    }
}