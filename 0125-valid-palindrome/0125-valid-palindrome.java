class Solution {
    public boolean isPalindrome(String s) {
        String clean=s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        StringBuilder rev=new StringBuilder(clean).reverse();
        String reverse=rev.toString();
        if(reverse.equals(clean)){
            return true;
        }
        return false;
    }
}