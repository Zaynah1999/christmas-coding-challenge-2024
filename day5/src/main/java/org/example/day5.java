package org.example;

public class day5 {
        public int removeDuplicates(int[] nums) {
            if (nums == null || nums.length == 0) {
                return 0;
            }

            int itemPosition = 0;

            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != nums[itemPosition]) {
                    itemPosition++;
                    nums[itemPosition] = nums[i];
                }
            }

            return itemPosition + 1;
        }
    }