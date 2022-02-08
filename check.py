import nltk
import numpy as np
import string
def num_digits(text):
	ans=0;
	for c in text:
		if(c.isdigit()):
			ans = ans+1;
	return ans;	
cnt=num_digits("i am good. i am goof")
print(cnt)