package org.example;
import java.util.List;

public class day18 {
    public String longestCommonPrefix(List<String> strs) {
        if (strs == null || strs.isEmpty()) {
            return "";
        }

        StringBuilder stringer = new StringBuilder();
        int shortest = strs.stream().mapToInt(String::length).min().orElse(0);

        for (int j = 0; j < shortest; j++) {
            for (int i = 1; i < strs.size(); i++) {
                if (strs.get(i - 1).charAt(j) != strs.get(i).charAt(j)) {
                    return stringer.toString();
                }
            }
            stringer.append(strs.get(0).charAt(j));
        }

        return stringer.toString();
    }
}
