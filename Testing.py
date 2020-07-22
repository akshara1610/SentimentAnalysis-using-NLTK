nltk.download('punkt')
from nltk.tokenize import word_tokenize
custom_tweet = 'I hate you, you made me cry.'
custom_tokens = remove_noise(word_tokenize(custom_tweet))

print(classifier.classify(dict([token, True] for token in custom_tokens)))

#You can change the custom_tweet input and check for various inputs
