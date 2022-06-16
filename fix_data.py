import json

if __name__ == '__main__':
    print("START")
    
    with open('cpus0.json', 'r') as f:
        data = json.loads(f.read())
    
    for d in data:
        d.pop('price')
        d.pop('output')
        d.pop('value')
        d.pop('threadValue')
        d.pop('powerPerf')
        d['cpumark'] = d['cpumark'].replace(',', '')
        d['thread'] = d['thread'].replace(',', '')
        

    with open('cpus.json', 'w') as f:
        f.write(json.dumps(data))

    print("DONE")