public class ps2 {
    public static void main(String args[]) {
        
        int len = args.length;

        char[] initials = new char[len];

        for (int i = 0; i < len; i++) {
            initials[i] = args[i].charAt(0);
        }


        System.out.println(initials);
    }
}