public class Card {

    private int value;
    private int suit;

    public enum value {
        1(1),
        2(2),
        3(3),
        4(4),
        5(5),
        6(6),
        7(7),
        8(8), 
        9(9), 
        10(10), 
        J(11),
        Q(12), 
        K(13)
    }
    public enum suits {
        DIAMONDS, CLUBS, SPADES, HEARTS
    }

    public Card(int value, int suit) {
        this.value = value;
        this.suit = suit;
    }


    public int getValue() {
        return value;
    }

    public int getSuit() {
        return suit;
    }
/*
    public boolean compareValue(char compareValue) {
        return true;
    }

    public boolean compareSuit(char compareSuit) {
        return true;
    }

    public boolean compare(String card) {
        return true;
    }
    */
}