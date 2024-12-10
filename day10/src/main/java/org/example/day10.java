package org.example;

public class day10 {
    public boolean isValid(String s) {
        boolean valid = true;
        while (valid) {
            if (s.isEmpty()) {
                return true;
            }
            if (s.contains("()")) {
                s = s.replace("()", "");
                continue;
            }
            if (s.contains("{}")) {
                s = s.replace("{}", "");
                continue;
            }
            if (s.contains("[]")) {
                s = s.replace("[]", "");
                continue;
            }
            return false;
        }
        return false;
    }
}
