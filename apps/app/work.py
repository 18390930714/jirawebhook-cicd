from flask import request
from flask import jsonify
from pprint import pprint
from apps import app
from apps.models import db
from apps.models import issueinfo
from views import getAllimages

#db.init_app(app)

@app.route('/')
def hello_world():
    print("hello")
    return 'hello world'

@app.route('/webhook', methods=['POST'])
def register():
    print(request.headers)
    data = request.json
    pprint(data)
    if data['issue']['fields']['customfield_10200']:
        deployInfo = data['issue']['fields']['customfield_10200']      #deployInfo : 发布信息
        if deployInfo.splitlines():
            deployInfolist = deployInfo.splitlines()
            getAllimagescode = getAllimages(deployInfo.splitlines(), len(deployInfo.splitlines()))
            if getAllimagescode == "-1":
                imageInfoAll = deployInfolist[1]
            else:
                imageInfoAll = deployInfolist[1:getAllimagescode]
            if imageInfoAll[5:]:
                imageInfo = imageInfoAll[5:]
            else:
                imageInfo = "无"
        else:
            return 0;
    else:
        deployInfo = "无"
        imageInfo = "无"
    issue_id = data.get("issue", {}).get("key")
    issue_name = data['issue']['fields']['summary']

    #插入数据库
    issue = issueinfo(imageinfo=imageInfo, issueid=issue_id, issuename=issue_name, deployinfo=deployInfo)
    db.session.add(issue)
    db.session.commit()

    return jsonify({"code": 0})

## 表结构  issueId, issueName, IMAGE, deployInfo, updateTime

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5391, debug=True)