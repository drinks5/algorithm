#!/usr/bin/env python3
class Solution:
    def checkInclusion(self, t: str, s: str) -> bool:

        needs: dict[str, int] = {}
        windows: dict[str, int] = {}
        match = 0
        start = end = -1
        min_len = len(s) + 1
        i = j = 0
        for x in t:
            if x not in needs:
                needs[x] = 1
            else:
                needs[x] += 1
        for x in s:
            if x not in windows:
                windows[x] = 0

        while j < len(s):
            right = s[j]
            if right in needs:
                windows[right] += 1
                if windows[right] == needs[right]:
                    match += 1
            j += 1
            if match == len(needs):
                return True
            # while match == len(needs):
            #     left = s[i]
            #     if (j - i) < min_len:
            #         min_len = j - i
            #         start = i
            #         end = j
            #     if left in needs:
            #         windows[left] -= 1
            #         if windows[left] < needs[left]:
            #             match -= 1
            #     i += 1

        return False


def main():
    s = "ab"
    t = "eidboaoo"
    data = Solution().checkInclusion(t, s)
    print(data == True)


if __name__ == "__main__":
    main()