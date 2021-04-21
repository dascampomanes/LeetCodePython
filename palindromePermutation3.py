class Solution:
	def palindromePermutation(self, s1: str) -> bool:
		a = 0
		for e in s1:
			if e != " ":
				b = 1 << ord(e)
				a = a ^ b
		return (a & (a - 1)) == 0

S = Solution()
print(S.palindromePermutation("kek"))
print(S.palindromePermutation("kekk"))
print(S.palindromePermutation("aaabbb"))
print(S.palindromePermutation("aabbb"))
print(S.palindromePermutation("taco cat"))
print(S.palindromePermutation("lmao"))