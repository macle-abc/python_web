from elasticsearch import Elasticsearch
import json

def main():
    es = Elasticsearch(hosts=["127.0.0.1:9200"], timeout=5000)
    es.indices.create(index='transport', ignore=400)
    datas = []
    for item in range(1, 54):
        with open(f'input/{item}.txt', encoding='utf-8') as f:
            temp = json.load(f)
            datas.append(temp)

    for data in datas:
        es.index(index='transport', doc_type='book', body=data)

if __name__ == '__main__':
    main()
