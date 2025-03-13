class Solution {
    public int reverse(int x) {
        // Convert the integer to a string
        String num = Integer.toString(x);

        // Handle negative numbers
        boolean isNegative = false;
        if (num.charAt(0) == '-') {
            isNegative = true;
            num = num.substring(1); // Remove the negative sign
        }

        // Reverse the string
        StringBuilder rev = new StringBuilder(num).reverse();
        String reverse = rev.toString();

        // Add the negative sign back if necessary
        if (isNegative) {
            reverse = "-" + reverse;
        }

        // Convert the reversed string back to an integer
        try {
            int reversedNum = Integer.parseInt(reverse);
            return reversedNum;
        } catch (NumberFormatException e) {
            // Handle integer overflow
            return 0;
        }
    }
}