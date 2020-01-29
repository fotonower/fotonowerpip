__author__ = 'moilerat'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mtr.lib.fotonower_api.fotonower_connect as ftn
import os

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", type="string", dest="file", default="",
                      help="folder where are photo to upload")
    parser.add_option("-t", "--token", action="store", type="string", dest="token",
                      default="", help=" token ")
    parser.add_option("-u", "--root_url", action="store", type="string", dest="root_url", default="jussieu.fotonower.com",
                      help="root_url to upload photos")
    parser.add_option("-d", "--datou", action="store", type="string", dest="datou",
                      default="1585",help="datou id to be treated")
    parser.add_option("-i", "--is_live", action="store_true", dest="is_live",
                      default=False, help="launch treatment datou immediatly")

    parser.add_option("-P", "--protocol", action="store", type="string", dest="protocol",
                      default="https", help="http or https")
    (x, args) = parser.parse_args()

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

    print(map_result_insert_aux)
    print(map_result_insert_aux["res_json"])
    #{'mtr_datou_id':9,'is_live':true,'list_datou_ids_unused':[19],"manual_labelling":{"manual":456,"hashtag_type":451}}

    if len(map_result_insert_aux['res_json']['result']) > 0:
        print(map_result_insert_aux['res_json']['result'][0]['result'])

    # to get results, may take some time depending on treatment asked
    res_datou = fc.get_datou_result(datou_current_ids_dict=list_current_datou_ids)
    print(res_datou)
