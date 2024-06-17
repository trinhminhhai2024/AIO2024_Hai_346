#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
with open('/content/P1_data.txt', 'r') as f:
  #sentence = f.readlines()
  document = f.read()
#type(sentence)
#sentence[:2]
#print(document)
def text_preprocessing(sentence):
  sentence = sentence.lower()
  sentence = sentence.replace('.','').replace(',','')
  words = sentence.split()
  return words

word = text_preprocessing(document)
counter = {}
for w in word:
  if w in counter:
    counter[w] +=1
  else:
    counter[w] = 1
print(counter)

