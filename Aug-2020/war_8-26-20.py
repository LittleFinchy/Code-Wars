def is_isogram(s):
	return len(set(s.lower())) == len(s)


print(is_isogram('fasADfes'))