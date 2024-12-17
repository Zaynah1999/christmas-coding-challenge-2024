package org.example;

import java.util.List;

public class day17 {
        public int searchInsert(List<Integer> nums, int target) {
            if (nums.contains(target)) {
                return nums.indexOf(target);
            } else {
                for (int i = 0; i < nums.size(); i++) {
                    if (target < nums.get(i)) {
                        return i;
                    }
                }
                return nums.size();
            }
        }
    }
