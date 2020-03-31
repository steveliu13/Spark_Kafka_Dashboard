import json
from unittest import TestCase

from util import JsonUtil
from util.DataUtil import generateData, dict2record, consumeRecord
from util.JsonUtil import json_deserialize, json_deserialize2objlist


class Test(TestCase):
    def test_generate_data(self):
        records = generateData()
        print(records)

        #records = records[1:len(records) - 1].split("}, {")

        # result = []
        # for record in records:
        #     if not record.endswith("}"):
        #         record+="}"
        #     if not record.startswith("{"):
        #         record = "{"+record
        #     print(record)
        #     temp = consumeRecord()
        #     json_deserialize(record, temp)
        #     #temp = json.load(record, object_hook=dict2record)
        #     result.append(temp)
        #     for r in result:
        #         print(r.name)


        result = json_deserialize2objlist(records,consumeRecord)
        print(result.__len__())
        for r in result:
            print(r.name)
