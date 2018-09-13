import os
import json
import time
import glob
from urllib.request import urlretrieve

import yaml
from flask import Flask
from flask import request
from github import Github
from flask import render_template


GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN', '')

app = Flask(__name__, static_url_path='/static')
app.config['FREEZER_DESTINATION'] = 'docs'

g = Github(GITHUB_ACCESS_TOKEN)

def check_pr(pr):
    print(pr)
    files = [file for file in pr.get_files()]
    
    # check number of file
    print(files) 
    if len(files) != 1:
        return False, '咦？你是不是不只改了一個檔案？'

    # check file status
    print(files[0].status)
    if files[0].status != 'added':
        print(files[0].status)
        return False, '只能新增檔案喔！'

    # check filename
    login = pr.user.login 
    filename = files[0].filename.replace("messages/", "")
    if 'yaml' in filename:
        login_yml = "{login}.yaml".format(login=login)
    else:
        login_yml = "{login}.yml".format(login=login)
    print(filename)
    print(login_yml)
    if filename != login_yml:
        return False, '你的 YAML 檔名是不是跟 username 不一樣呢？'

    # check yaml format
    print(files[0].raw_url)
    urlretrieve(files[0].raw_url, filename)
    with open(filename, 'r') as stream:
        try:
            data = yaml.load(stream)
            if not data.get('displayname') or not data.get('message'):
                return False, '請留下你的 displayname 和 message，謝謝！'
        except yaml.YAMLError as exc:
            print(exc)
            return False, 'YAML 檔案讀取錯誤，請確定格式是否正確唷！'
    os.remove(filename)

    return True, ''

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        payload = json.loads(request.data)
        if payload.get('action') and payload['action'] in ['opened', 'reopened']:
            repo = g.get_repo(payload['repository']['id'])
            pr_number = payload['number']
            pr = repo.get_pull(pr_number)
            is_ok, error_msg = check_pr(pr)
            if is_ok:
                pr.as_issue().create_comment('This is good. Nice to meet you :)')
                pr.merge()
            else:
                pr.as_issue().create_comment(error_msg)
            return ''

    messages = []
    for f in glob.glob("messages/*.yml"):
        with open(f, 'r') as stream:
            data = yaml.load(stream)
            try:
                messages.append({
                    'message': data['message'],
                    'display_name': data['displayname'],
                    'username': f.replace("messages/", "").replace(".yml", "")
                })
            except yaml.YAMLError as exc:
                print(exc)
    for f in glob.glob("messages/*.yaml"):
        with open(f, 'r') as stream:
            data = yaml.load(stream)
            try:
                messages.append({
                    'message': data['message'],
                    'display_name': data['displayname'],
                    'username': f.replace("messages/", "").replace(".yaml", "")
                })
            except yaml.YAMLError as exc:
                print(exc)

    return render_template('index.html', messages=messages)
