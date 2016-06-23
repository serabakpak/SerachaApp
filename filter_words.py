# This program takes a body of text and replaces swear words with "nicer" alternatives.

# Dictionary of bad words and their replacements

bad_word_dict = {'FUCK': 'EFF', 'BITCH': 'BIZNATCH', 'SHIT': 'SHIZNIT', 'ASSHOLE': 'A-HOLE', 'DAMN': 'DAGNABBIT', 'FUCKING': 'FLUNKING', 'WHORE': 'WOMAN', 'BULLSHIT': 'BS', 'SHUT THE FUCK UP': 'SHUT THE FRONT DOOR', 'FUCKIN': 'FUDGIN', 'FUCK!': 'FUDGE NUGGET!', 'HATE': 'LOVE'}

# Iterate through dictionary and replace all bad words in text.

def replace_bad_words(text, dict):
	text = text.upper()
	for key in dict:
		text = text.replace(key, dict[key])
	return text		


# later on, going to rewrite own filter method to account for capilizations and punctuations
# split the string into a series of words
# determine if the original word is an capitalized or upcase
# to see if the word is in the dictionary, we need to downcase the word
# if the word is a match we will replace the word with the value in the dictionary, but maintain the original word's capitalization or upcase value that we store before the check
# append the word to a new list
# join the words in the new list with a space.

# def replace_bad_words(text, dict):
# 	list_text = text.split()
# 	new_list = []
# 	for word in list_text:	
# 		if word.lower() in dict.keys():
# 			word = dict[word]			
# 			print word
# 		new_list.append(word)
# 	print new_list
# 	print " ".join(new_list)		

# replace_bad_words(test_text, bad_word_dict)

