class Solution:
	def palindromePermutation(self, s1: str) -> bool:
		a = [0] * 128
		odds = 0
		for e in s1:
			if e != ' ':
				a[ord(e)] += 1
				if a[ord(e)] % 2 == 1:
					odds += 1
				else:
					odds -= 1
		if odds > 1:
			return False
		return True

S = Solution()
print(S.palindromePermutation("kek"))
print(S.palindromePermutation("kekk"))
print(S.palindromePermutation("aaabbb"))
print(S.palindromePermutation("aabbb"))
print(S.palindromePermutation("taco cat"))
print(S.palindromePermutation("lmao"))