#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
with open("./Scenery/Scenery_0.json", 'r') as j:
    json_data = json.load(j)
    #print(json_data)
    functions = json_data['functions']
    print("lenFunc:",len(functions))
    for n in range(len(functions)):
        function = functions[n]
        funcName = function["function"]
        print(funcName)
        if funcName == "Image":
            print(function["imagePath"])
        #else:
            #print('no path req')
