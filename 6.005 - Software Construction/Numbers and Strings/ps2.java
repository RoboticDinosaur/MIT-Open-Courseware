public class ps2 {
    public static void main(String[] args) {

        int numArgs = args.length;

        int total = 0;

        if (numArgs < 2) {
            System.out.println("Not enough numbers");
            return;
        } else {
            for (int i = 0; i < numArgs; i++) {
                total += Integer.valueOf(args[i]).intValue();
            }
            System.out.println(total);

        }
    }

}