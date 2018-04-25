import pytextrank
import sys
import json
import re
from importlib import reload

reload(sys)
#sys.setdefaultencoding('utf-8')

path_stage1 = 'o1.json'
path_stage2 = 'o2.json'

def text_rank(json_request):
	pattern = re.compile("TI  - (.*?)\\r|AB  - (.*?)\\r")
	matches = re.findall(pattern, json_request['ris'])
	all_inputs = []
	for section in matches:
	       all_inputs.append((''.join([word + ' ' for word in section])).strip())

	input_json = {}
	input_json['id'] = "0"
	input_json['text'] = '.'.join(all_inputs)

	with open('ris_extracted.json', 'w') as output:
	    json.dump(input_json, output)

	with open(path_stage1, 'w') as f:
	    for graf in pytextrank.parse_doc(pytextrank.json_iter('ris_extracted.json')):
	        f.write("%s\n" % pytextrank.pretty_print(graf._asdict()))

	graph, ranks = pytextrank.text_rank(path_stage1)

	with open(path_stage2, 'w') as f:
	    for rl in pytextrank.normalize_key_phrases(path_stage1, ranks):
	        f.write("%s\n" % pytextrank.pretty_print(rl._asdict()))

	phrases = list([p for p in pytextrank.limit_keyphrases(path_stage2, phrase_limit=20)])

	return phrases
