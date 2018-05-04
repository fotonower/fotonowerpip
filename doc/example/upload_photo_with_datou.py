#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fotonower as FC
import os

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", type="string", dest="file", default="",
                      help="folder where are photo to upload")
    parser.add_option("-t", "--token", action="store", type="string", dest="token",
                      default="", help=" token ")
    parser.add_option("-u", "--root_url", action="store", type="string", dest="root_url", default="vision.fotonower.com",
                      help="root_url to upload photos")
    parser.add_option("-d", "--datou", action="store", type="string", dest="datou",
                      default="2",help="datou id to be treated")
    parser.add_option("-P", "--protocol", action="store", type="string", dest="protocol",
                      default="https", help="http or https")
    (x, args) = parser.parse_args()

    if x.token == "":
        print("please provide a valid token")
        exit(1)
    try:
        fc = FC.FotonowerConnect(x.token, x.root_url, x.protocol)
    except :
        print("please provide a valid token")
        exit(1)
    if not os.path.isfile(x.file):
        print("please provide a valid file")
        exit(2)
    files = [x.file]

    map_result_insert_aux = fc.upload_medias(files, upload_small=True,
                                                 verbose=True, compute_classification=True, arg_aux={'classification_actions':"{'list_datou_ids':["+str(x.datou)+"], 'is_live' : true}"})

    print(map_result_insert_aux)
    #{'mtr_datou_id':9,'is_live':true,'list_datou_ids_unused':[19],"manual_labelling":{"manual":456,"hashtag_type":451}}