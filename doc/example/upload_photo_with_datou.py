__author__ = 'moilerat'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftn
import os

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Example for upload of photos and launch of datous')

    parser.add_argument("-f", "--file", action="store", type=str, dest="file", default="",
                      help="folder where are photos to upload")
    parser.add_argument("-t", "--token", action="store", type=str, dest="token",
                      default="", help=" token ")
    parser.add_argument("-u", "--root_url", action="store", type=str, dest="root_url", default="jussieu.fotonower.com",
                      help="root_url to upload photos")
    parser.add_argument("-d", "--datou", action="store", type=str, dest="datou",
                      default="1585",help="datou id to be treated")
    parser.add_argument("-i", "--is_live", action="store_true", dest="is_live",
                      default=False, help="launch treatment datou immediatly")
    parser.add_argument("-P", "--protocol", action="store", type=str, dest="protocol",
                      default="https", help="http or https")
    x = parser.parse_args()

    if x.token == "":
        print("please provide a valid token")
        exit(1)
    try:
        fc = ftn.FotonowerConnect(x.token, x.root_url, x.protocol)
    except :
        print("please provide a valid token")
        exit(1)
    if not os.path.isfile(x.file):
        print("please provide a valid file")
        exit(2)
    files = [x.file]

    map_result_insert_aux, list_current_datou_ids = fc.upload_medias(files, list_datou_ids=[x.datou], is_live=x.is_live, upload_small=True, verbose=True)

    if x.is_live : 
        print(map_result_insert_aux)
        print(map_result_insert_aux["res_json"])
    
        if len(map_result_insert_aux['res_json']['result']) > 0:
            print(map_result_insert_aux['res_json']['result'][0]['result'])
    else : 
        print("option is_live egale false , vous devez attendre un peu pour recuperer les resultats" )
        print("vous obtiendrez les resultats dans l'endpoint : ")
        list_datou_ids  =  list_current_datou_ids['list_datou_current']
        csv_datou_ids = ",".join([str(item) for item in list_datou_ids])
        url = "https://www.fotonower.com/api/v1/secured/datou/result?token={}&datou_current_ids={}".format(x.token,csv_datou_ids)
        print(url)
        
