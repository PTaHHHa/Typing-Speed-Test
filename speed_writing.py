import random
import datetime
import difflib


print('Typing Speed Test')
with open('file.txt', 'r') as file:
    text = file.read()
    sentences = text.split('.')

    refactored_sentences = [x.strip() for x in sentences]

random_sentence = random.choice(refactored_sentences)

print('Try to write the same sentence\n')
print(random_sentence)

time_start = datetime.datetime.now()
user_input = input()
time_stop = datetime.datetime.now()

if user_input != random_sentence:
    print("Your sentence doesn't match with given sentence")
diff = difflib.SequenceMatcher(None, user_input, random_sentence).ratio()

total_time = abs(time_stop - time_start).seconds
print(f'\nTime: {total_time} sec.')
print(f'Similarity: {diff*100}%')
