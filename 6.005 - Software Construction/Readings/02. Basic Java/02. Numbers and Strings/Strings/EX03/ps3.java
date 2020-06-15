import java.util.Arrays;

public class ps3 {
    public static void main (String args[]){
        String string1 = "Cosmo and Laine:";
        String string2 = "Maid, clean soon!";

        string1 = string1.replaceAll("[^a-zA-Z]", "").toLowerCase();
        string2 = string2.replaceAll("[^a-zA-Z]", "").toLowerCase();

        string1 = sortString(string1);
        string2 = sortString(string2);

        if (string1.matches(string2)) {
            System.out.println("These strings match");
        }
        else {
            System.out.println("These do not match");
        }

    }

    public static String sortString(String string) {
        char tempArray[] = string.toCharArray();

        Arrays.sort(tempArray);

        return new String(tempArray);
    }
    
}