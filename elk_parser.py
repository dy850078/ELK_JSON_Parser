import time
import json
import os
import argparse
import logging
import settings

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--logfile', dest='log', help='input log file')
args = parser.parse_args()

if args.log == '':
	logging.error('File Path Empty')

else:
	start_time = time.time()

	file = str(args.log)
	with open(file, "r", encoding='utf-8') as f:
		data = json.load(f)

	file_date = file.split('/')[4][0:8]

	for i in range(len(data["hits"]["hits"])):
		orig_log = data["hits"]["hits"][i]["_source"] 
		revised_timestamp = orig_log['@timestamp'].split('T')
		revised_timestamp[0] = '2021-08-10'
		orig_log['@timestamp'] = 'T'.join(revised_timestamp)
		final_log = "'" + str(orig_log).replace("'", '"') + "'"
		input_command = 'curl -k -u %s:%s -XPOST https://localhost:9200/winlogbeat-%s/_doc -H "Content-Type: ' \
			'application/json" -d %s' % (settings.id, settings.pwd, file_date, final_log)
		os.system(input_command)
			
	end_time = time.time()
	print('\n\n\n  - Process Time: ' + str(round(end_time - start_time, 2)))
