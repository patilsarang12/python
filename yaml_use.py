import yaml

with open("yaml_test.yaml","r") as fp:
    data=fp.read()
    print(data)
    yaml_dict=yaml.load(data,Loader=yaml.Loader)
    for keys,values in yaml_dict.items():
        print(keys,values)
        print("City is ",values['Address']['state'])
        values['Address']['state']="karnataka"
    print(yaml_dict)

with open("backup.yaml","w") as ft:
    ft.write(yaml.dump(yaml_dict))
