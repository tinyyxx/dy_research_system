import json
import requests


def search(uri, start_date, end_date):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "range": {
                "date": {
                    "gte": start_date,
                    "lte": end_date,
                    "time_zone": "Asia/Shanghai"
                }
            }
        },
        "size": 50,
        "sort": [{
            "date": {
                "order": "asc"
            }
        }]
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

# res = search("http://192.168.1.84:9200/dy_coalchemical_sxsypp/_search", "2018-12-25", "now")
# data = res["hits"]["hits"][0]["_source"]
# print(data)
#
# print(data['date'].split('T')[0])