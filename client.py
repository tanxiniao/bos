import pickle
import os
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce import exception
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient
import logging

logging.basicConfig(level=logging.DEBUG)
__logger = logging.getLogger(__name__)

bos_host = "http://bj.bcebos.com"
access_key_id = ""
secret_access_key = ""

config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = bos_host)
bos_client = BosClient(config)
bucket_name = "wordpressxd"
file_name = "baidutest.ISO"
object_key = "baidutest.ISO"
f = open(file_name,'r')

upload_id = bos_client.initiate_multipart_upload(bucket_name, object_key).upload_id
left_size = os.path.getsize(file_name)
#print left_size

offset = 0
part_number = 1
part_list = []

while left_size > 0:
        part_size = 5 * 1024 * 1024
        if left_size < part_size:
            part_size = left_size

        response = bos_client.upload_part_from_file(
            bucket_name, object_key, upload_id, part_number, part_size, file_name, offset)
        left_size -= part_size
        offset += part_size
        # your should store every part number and etag to invoke complete multi-upload
        part_list.append({
            "partNumber": part_number,
            "eTag": response.metadata.etag
        })
        print "left_size is:%d"%(left_size) 
        print "\n"
        print "offset is:%d"%(offset)
        print "\n"
        f1 = open("./b","wb")
        pickle.dump(part_list,f1)
        f1.close()
        print part_number
#print part_list
        part_number += 1
#bos_client.complete_multipart_upload(bucket_name, object_key, upload_id, part_list)

