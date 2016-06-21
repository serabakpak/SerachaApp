


# This program takes a body of text and replaces swear words with more palatable words.

#Ask user for body of text
user_text = "damn fucking bitch. shut the fuck up!"
print ("original text: " + user_text)


# dictionary of bad words and their replacements

bad_word_dict = {'shut the fuck up': 'shut the front door', 'fuck': 'eff', 'bitch': 'biznatch', 'shit': 'shiznit', 'asshole': 'a-hole', 'damn': 'darn', 'fucking': 'flunking'}

# Iterate through dictionary and replace all bad words in text.

def replace_bad_words(text, dict):
	for key in dict:
		text = text.replace(key, dict[key])
	return text		

# Call replace_bad_words function

new_text = replace_bad_words(user_text, bad_word_dict)
print ("new text: " + new_text.capitalize())





