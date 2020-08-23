#!/usr/bin/python
# coding=utf-8

from elasticsearch import Elasticsearch


class ElasticConnect:
    def __init__(self):
        self.elastic_connect = Elasticsearch(timeout=50000)

    def query_search(self, query):
        return self.elastic_connect.search(index='transport', body=query)

    @staticmethod
    def get_es_result(condition_num, result):
        values = []
        # xxx号交通事故发生在哪
        if condition_num == 1:
            for hit in result['hits']['hits']:
                value = hit['_source']['loc']
            values.append(value)
        # 王某违反交通法规的凭证是什么
        elif condition_num == 2:
            for hit in result['hits']['hits']:
                value = hit['_source']['proof']
            values.append(value)
        # xxx号交通事故的当事人是谁
        elif condition_num == 3:
            for hit in result['hits']['hits']:
                value = hit['_source']['person']
            values.append(value)
        # xxx号交通事故的肇事车辆是什么
        elif condition_num == 4:
            for hit in result['hits']['hits']:
                value = hit['_source']['vehicle']
            values.append(value)
        # 王某在xxx号交通事故中承担什么
        elif condition_num == 5:
            for hit in result['hits']['hits']:
                value = hit['_source']['responsibility']
            values.append(value)
        return list(set(values))
