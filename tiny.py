#import tinysegmenter
import fugashi
import sys

if len(sys.argv) < 2:
    filename = input("Enter filename: ")
else:
    filename = sys.argv[1].split("\\")[-1]
outfile = 'PARSED_' + filename

with open(filename, encoding="utf8") as file_object:
    text = file_object.read()

tagger = fugashi.Tagger()
parsed_text = ""

for line in text.splitlines():
    words = [word.surface + " " for word in tagger(line)]
    last_line = ''.join(words)
    parsed_text += last_line + "\n"

with open(outfile, 'w', encoding="utf8") as f:
  f.write(parsed_text)