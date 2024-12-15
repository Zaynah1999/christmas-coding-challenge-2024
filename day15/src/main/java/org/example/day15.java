package org.example;

public class day15 {
    public boolean isPalindrome(int x) {
            // Check if the number is negative, in which case it's not a palindrome
            if (x < 0) {
                return false;
            }

            // Convert the integer to a string and check if it's equal to its reverse
            String str = Integer.toString(x);
            StringBuilder sb = new StringBuilder(str);
            return str.equals(sb.reverse().toString());
        }
    }

