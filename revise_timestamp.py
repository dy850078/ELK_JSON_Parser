# -*- coding: utf-8 -*-
import os
import settings
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3].split(':')
# plus 5 min
min = int(timestamp[1])+5
if min < 10:
    timestamp[1] = '0'+str(min)
else:
    timestamp[1] = str(min)
timestamp = ':'.join(timestamp) 

log = '{ "@timestamp" : "%sZ", "host" : { "name" : "NTWEBE119.edahdmz.org.tw" }, "agent" : { "version" : "7.9.0", "hostname" : "NTWEBE119", "ephemeral_id" : "7da05ef6-6fb2-4dca-9b26-c13010d8190f", "id" : "d1af3220-fc73-47bd-a73f-bbe0cd964756", "name" : "NTWEBE119", "type" : "winlogbeat" }, "ecs" : { "version" : "1.5.0" }, "log" : { "level" : "資訊" }, "message" : "__", "winlog" : { "keywords" : [ "稽核失敗" ], "computer_name" : "NTWEBE119.edahdmz.org.tw", "event_id" : 4625, "task" : "登入", "api" : "wineventlog", "provider_guid" : "{54849625-5478-4994-A5BA-3E3B0328C30D}", "channel" : "Security", "opcode" : "資訊", "process" : { "pid" : 648, "thread" : { "id" : 4876 } }, "record_id" : 1317691, "event_data" : { "TargetUserName" : "ed110871", "LogonType" : "3", "LogonProcessName" : "NtLmSsp ", "Status" : "0xc000006d", "ProcessId" : "0x0", "IpPort" : "55143", "TargetUserSid" : "S-1-0-0", "AuthenticationPackageName" : "NTLM", "KeyLength" : "0", "WorkstationName" : "SQLBI", "SubjectUserSid" : "S-1-0-0", "SubjectUserName" : "-", "SubjectDomainName" : "-", "IpAddress" : "10.7.2.231", "ProcessName" : "-", "LmPackageName" : "-", "SubjectLogonId" : "0x0", "SubStatus" : "0xc0000064", "TransmittedServices" : "-", "TargetDomainName" : "EDAH", "FailureReason" : "%%2313" }, "provider_name" : "Microsoft-Windows-Security-Auditing" }, "event" : { "created" : "%sZ", "kind" : "event", "code" : 4625, "timezone" : "+08:00", "provider" : "Microsoft-Windows-Security-Auditing", "action" : "登入" } }' % (timestamp, timestamp)

input_command = 'curl -k -u elastic:settings.pwd -XPOST https://localhost:9200/winlogbeat-test/_doc -H "Content-Type: application/json" -d ' + "'" + log + "'"
for i in range(3):
    os.system(input_command)
    print(timestamp)





