public class Card {
    private char rank;
    private char suit;

    // suits = H D C S
    // ranks = 1234556792345678

    // Card(K, H)
    public Card(char rank, char suit) {
        this.rank = rank;
        this.suit = suit;
    }

    public string toString() {
        return rank + " of " + suit;
    }

    public Boolean isSameRank(card cardOne, card cardTwo) {
        if (cardOne.getSuite().equals(cardTwo.getSuit())) {
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public Boolean isSameSuit(card cardOne, card cardTwo) {
        if (cardOne.getRank().equals(cardTwo.getRank())) {
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public char getRank() {
        return rank;
    }

    public char getSuit() {
        return suit;
    }
}