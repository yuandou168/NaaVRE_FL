from laserfarm.remote_utils import get_wdclient
import pathlib
from laserfarm.remote_utils import list_remote

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()

id = args.id



conf_remote_path_ahn = conf_remote_path_root + '/ahn'
conf_hostname = 'https://lifewatch.lab.uvalight.net:32443'
conf_login = 'MTg5OWI3YjZkYTUyOT'
conf_password = 'cxYTBmMjgxZWZi'

conf_remote_path_ahn = conf_remote_path_root + '/ahn'
conf_hostname = 'https://lifewatch.lab.uvalight.net:32443'
conf_login = 'MTg5OWI3YjZkYTUyOT'
conf_password = 'cxYTBmMjgxZWZi'
conf_wd_opts = { 'webdav_hostname': conf_hostname, 'webdav_login': conf_login, 'webdav_password': conf_password}
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), pathlib.Path(conf_remote_path_ahn).as_posix())
             if f.lower().endswith('.laz')]
print(laz_files)

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
