# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

Given an array of strings `strs`, group the <div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:r1d:">anagrams<div style="position: fixed; z-index: 40; inset: 0px auto auto 0px; transform: translate(328px, 214px);"> together. You can return the answer in **any order** .

**Example 1:** 

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

Explanation:

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:** 

```
Input: strs = [""]

Output: [[""]]
```

**Example 3:** 

```
Input: strs = ["a"]

Output: [["a"]]
```

**Constraints:** 

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.