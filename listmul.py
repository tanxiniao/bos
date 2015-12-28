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
object_key = "baidutest.ISO"

#response = bos_client.list_multipart_uploads(bucket_name)
#for upload in response.uploads:
#     __logger.debug("[Sample] list multi-uploads, upload_id:%s", upload.upload_id)

response2 = bos_client.list_parts(bucket_name, object_key, upload_id = upload_id)
for part in response2.parts:
    print part.part_number
