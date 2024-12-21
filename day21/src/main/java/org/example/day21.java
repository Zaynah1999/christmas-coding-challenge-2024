package org.example;

public class day21 {
    public int lengthOfLastWord(String s) {
        String[] words = s.trim().split("\\s+");
        if (words.length > 0) {
            return words[words.length - 1].length();
        }
        return 0;
    }
}