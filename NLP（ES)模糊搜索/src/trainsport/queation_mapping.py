#!/usr/bin/python
# coding=utf-8

from refo import finditer, Predicate, Star, Any
import re


class WordReplace(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(WordReplace, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2


class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action
        self.condition_num = condition_num

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        return self.action(matches), self.condition_num


pos_action = "action"  # 交通事故
pos_articleOfLaw = "articleOfLaw"  # 法律条文
pos_law = "law"  # 法律法规
pos_loc = "loc"  # 地点
pos_person = "person"  # 人
pos_proof = "proof"  # 证据
pos_responsibility = "responsibility"  # 责任
pos_trafficAccident = "trafficAccident"  # 道路交通事故
pos_vehicle = "vehicle"  # 车辆

# 定义实体
action_entity = (WordReplace(pos=pos_action))
articleOfLaw_entity = (WordReplace(pos=pos_articleOfLaw))
law_entity = (WordReplace(pos=pos_law))
loc_entity = (WordReplace(pos=pos_loc))
person_entity = (WordReplace(pos=pos_person))
proof_entity = (WordReplace(pos=pos_proof))
responsibility_entity = (WordReplace(pos=pos_responsibility))
trafficAccident_entity = (WordReplace(pos=pos_trafficAccident))
vehicle_entity = (WordReplace(pos=pos_vehicle))

# 定义别名
action = (WordReplace("交通事故") | (WordReplace("事故")))
articleOfLaw = (WordReplace("法律条文") | (WordReplace("法律")))
law = (WordReplace("法律法规") | (WordReplace("法规")))
loc = (WordReplace("地点") | (WordReplace("地方")) | WordReplace("哪里") | WordReplace("哪儿") | WordReplace(
    "位置") | WordReplace("哪"))
person = (WordReplace("人") | WordReplace("肇事者") | WordReplace("责任人") | WordReplace("负责人") | WordReplace("当事人"))
proof = (WordReplace("证据") | WordReplace("证明") | WordReplace("凭证"))
responsibility = (WordReplace("责任") | WordReplace("承担"))
trafficAccident = (WordReplace("道路交通事故"))
vehicle = (WordReplace("车辆") | WordReplace("车") | WordReplace("行驶工具") | WordReplace("肇事车辆"))


class Question:
    def __init__(self):
        pass

    @staticmethod
    def loc_question_search(word_objects):
        content = "".join([item.token for item in word_objects])
        trafficAccident_content = re.search(r"(深公交.*?认字.*?号)", content)
        if not trafficAccident_content:
            return None
        loc_content = re.search(r"(地点|地方|哪里|哪儿|位置|哪)", content)
        if not loc_content:
            return None
        trafficAccident_content = trafficAccident_content.group(1)
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "trafficAccident": trafficAccident_content
                            }
                        }
                    ]
                }
            },
            "size": 1
        }
        return query

    @staticmethod
    def proof_question_search(word_objects):
        query = None
        for w in word_objects:
            # print(f"pos={w.pos}, token={w.token}")
            if w.pos == pos_person:
                query = {
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "match": {
                                        "person.keyword": w.token
                                    }
                                }
                            ]
                        }
                    },
                    "size": 1
                }
        return query

    @staticmethod
    def person_question_search(word_objects):
        content = "".join([item.token for item in word_objects])
        trafficAccident_content = re.search(r"(深公交.*?认字.*?号)", content)
        if not trafficAccident_content:
            return None
        person_content = re.search(r"(人|肇事者|责任人|负责人|当事人)", content)
        if not person_content:
            return None
        trafficAccident_content = trafficAccident_content.group(1)
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "trafficAccident": trafficAccident_content
                            }
                        }
                    ]
                }
            },
            "size": 1
        }
        return query

    @staticmethod
    def vehicle_question_search(word_objects):
        content = "".join([item.token for item in word_objects])
        trafficAccident_content = re.search(r"(深公交.*?认字.*?号)", content)
        if not trafficAccident_content:
            return None
        vehicle_content = re.search(r"(车辆|行驶工具|肇事车辆|车)", content)
        if not vehicle_content:
            return None
        trafficAccident_content = trafficAccident_content.group(1)
        query = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "trafficAccident": trafficAccident_content
                            }
                        }
                    ]
                }
            },
            "size": 1
        }
        return query

    @staticmethod
    def responsibility_question_search(word_objects):
        person_content = ""
        for w in word_objects:
            if w.pos == pos_person:
                person_content = w.token
        content = "".join([item.token for item in word_objects])
        trafficAccident_content = re.search(r"(深公交.*?认字.*?号)", content)
        if not trafficAccident_content:
            return None
        trafficAccident_content = trafficAccident_content.group(1)
        query = {
                "query": {
                    "bool": {
                        "must": [{
                            "term": {
                                "person.keyword": person_content
                            }
                        }, {
                            "match": {
                                "trafficAccident": trafficAccident_content
                            }
                        }],
                    }
                },
                "size": 1,
        }
        return query



# 王某违反交通法则的凭证是什么
# (person_entity) + Star(Any(), greedy=False) + proof + Star(Any(), greedy=False)
# 深公交宝安认字2018第A00001号交通事故发生在什么地点
# Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + loc
# xxxx号交通事故的当事人是谁
#  Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + person + Star(Any(), greedy=False)
# xxxx号交通事故的肇事车辆是什么
# Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + vehicle + Star(Any(), greedy=False)
# 王某在xxx号交通事故中承担什么
# person_entity + Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + responsibility + Star(Any(), greedy=False)

rules = [
    Rule(condition_num=1,
         condition=(Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + loc),
         action=Question.loc_question_search),
    Rule(condition_num=2,
         condition=(person_entity + Star(Any(), greedy=False) + proof + Star(Any(), greedy=False)),
         action=Question.proof_question_search),
    Rule(condition_num=3,
         condition=(Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + person + Star(Any(),
                                                                                                   greedy=False)),
         action=Question.person_question_search),
    Rule(condition_num=4,
         condition=(Star(Any(), greedy=False) + action + Star(Any(), greedy=False) + vehicle + Star(Any(),
                                                                                                    greedy=False)),
         action=Question.vehicle_question_search),
    Rule(condition_num=5,
         condition=(person_entity + Star(Any(), greedy=False) + action + Star(Any(),
                                                                              greedy=False) + responsibility + Star(
             Any(), greedy=False)),
         action=Question.responsibility_question_search)
]
