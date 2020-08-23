import json

entity_parse_dict = {
    1: 'trafficAccident',
    2: 'loc',
    3: 'person',
    4: 'vehicle',
    5: 'action',
    6: 'proof',
    7: 'articleOfLaw',
    8: 'law',
    9: 'responsibility'
}


def main():
    for index in range(1, 54):
        with open(f'process/{index}.txt', 'r', encoding='utf-8') as f:
            record = json.load(f)
        temp_dict_record = {}
        for record_index, value in enumerate(record):
            temp_index = record_index + 1
            with open(f'dict/{entity_parse_dict[temp_index]}.txt', 'a', encoding='utf-8') as wf:
                wf.write(f"{value} {entity_parse_dict[temp_index]}\n")
            temp_dict_record[entity_parse_dict[temp_index]] = value
        # print(temp_dict_record)
        print(index)
        with open(f'input/{index}.txt', 'w', encoding='utf-8') as dict_f:
            json.dump(temp_dict_record, dict_f, ensure_ascii=False)


if __name__ == '__main__':
    main()
