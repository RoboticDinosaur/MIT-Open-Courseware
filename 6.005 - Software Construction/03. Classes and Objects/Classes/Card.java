public class Card {

    private char value;
    private char suit;

    public Card(char cardValue, char cardSuit) {
        value = cardValue;
        suit = cardSuit;
    }


    public int getValue() {
        return value;
    }

    public int getSuit() {
        return suit;
    }

    public boolean compareValue(char compareValue) {
        return true;
    }

    public boolean compareSuit(char compareSuit) {
        return true;
    }

    public boolean compare(String card) {
        return true;
    }
}