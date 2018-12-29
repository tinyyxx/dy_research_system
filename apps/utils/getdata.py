# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import Search
#
# client = Elasticsearch()
#
# s = Search(using=client, index="my-index")\
#     .filter("term", category="search").query("match", title="python").exclude("match", description="beta")
#
# s.aggs.bucket('per_tag', 'terms', field='tags').metric('max_lines', 'max', field='lines')
#
# response = s.execute()
#
# for hit in response:
#     print(hit.meta.score, hit.title)
#
# for tag in response.aggregations.per_tag.buckets:
#     print(tag.key, tag.max_lines.value)
import json, requests


def search(uri):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match_all": {}
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

res = search("http://192.168.1.84:9200/dy_coalchemical_sxsypp/_search")
data = res["hits"]["hits"][0]["_source"]
print(data)

print(data['date'].split('T')[0])