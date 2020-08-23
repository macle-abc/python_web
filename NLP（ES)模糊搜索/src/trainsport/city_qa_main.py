#!/usr/bin/python
# coding=utf-8

import os
from src.trainsport import query_analysis
from src.trainsport import elastic_connnect


def answer(query: str) -> list:
    dirname = os.path.dirname(__file__)
    print(dirname)
    es = elastic_connnect.ElasticConnect()
    query2search = query_analysis.QuestionMatch([f'{dirname}/data/action.txt',
                                                 f'{dirname}/data/articleOfLaw.txt',
                                                 f'{dirname}/data/law.txt',
                                                 f'{dirname}/data/loc.txt',
                                                 f'{dirname}/data/person.txt',
                                                 f'{dirname}/data/proof.txt',
                                                 f'{dirname}/data/responsibility.txt',
                                                 f'{dirname}/data/trafficAccident.txt',
                                                 f'{dirname}/data/vehicle.txt',
                                                 f'{dirname}/data/other.txt'])
    if not query:
        return None
    condition_num, values = query2search.get_result(query)
    print('con_num: {}, values: {}'.format(condition_num, values))
    if values is not None:
        es_result = es.query_search(query=values)
        results = es.get_es_result(condition_num=condition_num, result=es_result)
        return results
        # print(results)
    else:
        return None


if __name__ == '__main__':
    es = elastic_connnect.ElasticConnect()
    query2search = query_analysis.QuestionMatch([u'./data/action.txt',
                                                 u'./data/articleOfLaw.txt',
                                                 u'./data/law.txt',
                                                 u'./data/loc.txt',
                                                 u'./data/person.txt',
                                                 u'./data/proof.txt',
                                                 u'./data/responsibility.txt',
                                                 u'./data/trafficAccident.txt',
                                                 u'./data/vehicle.txt',
                                                 u'./data/other.txt'])

    while True:
        query = input("请输入问题(输入q退出): ")
        if query == 'q':
            break

        condition_num, values = query2search.get_result(query)

        print('con_num: {}, values: {}'.format(condition_num, values))

        if values is not None:
            es_result = es.query_search(query=values)
            results = es.get_es_result(condition_num=condition_num, result=es_result)
            print(results)
        else:
            print("无数据")
