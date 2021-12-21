from apps import db
import datetime

class issueinfo(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True) # 自增长id
    imageinfo = db.Column(db.String(100))        # 镜像tag
    issueid = db.Column(db.String(100))          # 工单ID
    issuename = db.Column(db.String(255))        # 描述
    deployinfo = db.Column(db.String(1024))      # 发布信息
    updatedtime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<issueifno %r>' % self.name

db.create_all()