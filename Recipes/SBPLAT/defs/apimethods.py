### IMPORTS
from requests import request
import json
from urllib2 import urlopen
import os
from time import sleep

### METHODS
def api_call(path, method='GET', query=None, data=None, token=None, flag_full_path=False):
    # Translates all the HTTP calls to interface with the API

    data = json.dumps(data) if isinstance(data, dict) or isinstance(data,list)  else None
    base_url = 'https://api.sbgenomics.com/v2/'
    if token == None:
        if 'AUTH_TOKEN' in os.environ.keys():
            token = os.environ['AUTH_TOKEN']
        else:
            print("""
            You have failed to set your AUTH_TOKEN, we can not continue.
            Please go to set_AUTH_TOKEN.ipynb and set it properly. 
            """)
            return False
                  
    headers = {
        'X-SBG-Auth-Token': token,
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }
    
    if flag_full_path:
        response = request(method, path, params=query, data=data, headers=headers)
    else:
        response = request(method, base_url + path, params=query, data=data, headers=headers)
    response_dict = json.loads(response.content) if response.content else {}

    if response.status_code / 100 != 2:
        print(response_dict['message'])
        print('Error Code: %i.' % (response_dict['code']))
        print(response_dict['more_info'])
        raise Exception('Server responded with status code %s.' % response.status_code)
    return response_dict


def download_files(fileList):
    # download a list of files from URLs (adapted from a few stackoverflow threads)
    dl_dir = 'files/downloads/'
    try:                    
        # make sure we have the download directory
        os.stat(dl_dir)
    except:
        a = dl_dir.split('/')[:-1]
        b = ''
        for a_dir in a:
            b = b + a_dir
            os.mkdir(b)
            b = b + '/'
        del a, b, a_dir

    for ii in range(1, len(fileList)):  # skip first [0] entry, it is a text header
        url = fileList[ii]
        file_name = url.split('/')[-1]
        file_name = file_name.split('?')[0]
        file_name = file_name.split('%2B')[1]
        u = urlopen(url)
        f = open((dl_dir + file_name), 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print("Downloading: %s Bytes: %s" % (file_name, file_size))

        file_size_dl = 0
        block_sz = 1024*1024
        prior_percent = 0
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            if (file_size_dl * 100. / file_size) > (prior_percent+20):
                print(status + '\n')
                prior_percent = (file_size_dl * 100. / file_size)
        f.close()


### CLASSES
class API(object):
    # making a class out of the api_call() function, adding other methods for housekeeping
    def __init__(self, path, method='GET', query=None, data=None, token=None, flag_full_path=False):
        self.flag = {'longList': False}
        response_dict = api_call(path, method, query, data, token, flag_full_path)
        self.response_to_fields(response_dict)

        if self.flag['longList']:
            self.long_list(response_dict, path, method, query, data)

    def response_to_fields(self,rd):
        if 'items' in rd.keys():        # get * {files, projects, tasks, apps}              (object name plural)
            if len(rd['items']) > 0:
                self.list_read(rd)
            else:
                self.empty_read(rd)
        else:                           # get details about ONE {file, project, task, app}  (object name singular)
            self.detail_read(rd)

    def list_read(self,rd):
        n = len(rd['items'])
        keys = rd['items'][0].keys()
        m = len(keys)

        for jj in range(m):
            temp = [None]*n
            for ii in range(n):
                temp[ii] = rd['items'][ii][keys[jj]]
            setattr(self, keys[jj], temp)

        if ('links' in rd.keys()) & (len(rd['links']) > 0):
            self.flag['longList'] = True

    def empty_read(self,rd):    # For the (unlikely) case an empty project is queried
        self.href = []
        self.id = []
        self.name = []
        self.project = []

    def detail_read(self,rd):
        keys = rd.keys()
        m = len(keys)

        for jj in range(m):
            setattr(self, keys[jj], rd[keys[jj]])

    def long_list(self, rd, path, method, query, data):
        prior = rd['links'][0]['rel']
        # Normally .rel[0] is the next, and .rel[1] is prior. If .rel[0] = prior, then you are at END_OF_LIST
        keys = rd['items'][0].keys()
        m = len(keys)

        while prior == 'next':
            rd = api_call(rd['links'][0]['href'], method, query, data, flag_full_path=True)
            prior = rd['links'][0]['rel']
            n = len(rd['items'])
            for jj in range(m):
                temp = getattr(self, keys[jj])          # possible speed bottleneck next three ops (allocating memory)
                for ii in range(n):
                    temp.append(rd['items'][ii][keys[jj]])
                setattr(self, keys[jj], temp)
    