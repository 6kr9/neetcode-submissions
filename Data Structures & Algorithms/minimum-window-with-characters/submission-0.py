class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        left = 0
        freq = defaultdict(int)

        for c in t:
            freq[c] += 1

        need = len(freq)
        have = 0    
        window_cnt = defaultdict(int)
        ans = ""
        min_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window_cnt[ch] += 1

            if ch in freq and window_cnt[ch] == freq[ch]:
                have += 1

            while have == need:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    ans = s[left:right+1]

                left_ch = s[left]   

                if left_ch in freq:
                    if window_cnt[left_ch] == freq[left_ch]:
                        have -= 1

                    window_cnt[left_ch] -= 1

                left += 1

        return ans                      