class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length()-1;

        while (l < r) {
            char cl = s.toLowerCase().charAt(l);
            char cr = s.toLowerCase().charAt(r);
            if (!Character.isLetterOrDigit(cl)) {
                l++;
                continue;
            }
            if (!Character.isLetterOrDigit(cr)) {
                r--;
                continue;
            }
            if (cl != cr) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
