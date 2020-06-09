class Deck {

    // suits = H D C S
    // ranks = 1234556792345678
    // For each Card.Suit > add Card.Rank
    public final int[] suits = { 1, 2, 3, 4 };
    public final int[] ranks = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 };

    public Card[][] cards;

    public Deck() {
        for (int suit = 0; suit <= suits.length; suit++) {
            for (int rank = 0; rank <= ranks.length; rank++) {
                cards[suit][rank] = new Card(suit, rank);
            }
        }
    }
}