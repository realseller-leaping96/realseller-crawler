import re

text = "I like apble And abple"
text_mod = re.sub('apble|abple',"apple",text)
print (text_mod)