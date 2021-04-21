class Solution:
	def palindromePermutation(self, s1: str) -> bool:
		a = [0] * 128
		for e in s1:
			if e == ' ':
				continue
			a[ord(e)] += 1
		middle = False
		for e in a:
			if e % 2 == 1:
				if middle:
					return False
				middle = True
		return True

S = Solution()
print(S.palindromePermutation("kek"))
print(S.palindromePermutation("kekk"))
print(S.palindromePermutation("aaabbb"))
print(S.palindromePermutation("aabbb"))
print(S.palindromePermutation("taco cat"))
print(S.palindromePermutation("lmao"))