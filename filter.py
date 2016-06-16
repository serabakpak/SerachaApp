


# This program takes a body of text and filters swear words and replaces with more palatable words.

#Ask user for body of text
text = "fuck you bitch you little shit"
print ("original text:", text)


# dictionary of bad words and their replacements

bad_word_dict = {'fuck': 'eff', 'bitch': 'biatch', 'shit': 'shiznit'}

# Loop over dictionary and look for certain words. If bad word exists, replace with another word.

for key in bad_word_dict:
	text = text.replace(key, bad_word_dict[key])
	

print ("new text:", text)





