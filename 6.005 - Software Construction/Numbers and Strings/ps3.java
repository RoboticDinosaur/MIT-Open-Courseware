public class ps3 {
    public static void main(String[] args) {

        int numArgs = args.length;

        double total = 0;

        if (numArgs < 2) {
            System.out.println("Not enough numbers");
            return;
        } else {
            for (int i = 0; i < numArgs; i++) {
                total += Float.valueOf(args[i]).floatValue();
            }
            System.out.format("%.2f%n", total);

        }
    }

}