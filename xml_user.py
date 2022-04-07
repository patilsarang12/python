import xmltodict

with open("xml_test.xml","r") as fp:
    xml_data=fp.read()
    xml_dict=xmltodict.parse(xml_data)
    print(xml_dict)
    print(xml_dict['myinfo'])
    print(xml_dict['myinfo']['technologies'])
    print(xml_dict['myinfo']['technologies']['skills'])
    xml_dict['myinfo']['firstname']="giriraj"
    xml_dict['myinfo']['lastname'] = "patil"
    print(xml_dict)
    my_xml_dict=xmltodict.unparse(xml_dict,pretty=True) # pretty parameter to xml format properly

with open("xml_duplicate.xml","w") as fs:
    fs.write(xmltodict.unparse(xml_dict,pretty=True))