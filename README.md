# jirawebhook-cicd
目标：通过设置jira的webhook获取QA状态的工单(issue)的信息
\b    jira webhook + 触发器 + 后置动作(post function)实现 post 数据到指定URL
\b    该服务基于python flask 在接收jira webhook数据后将数据存入mysl数据库;
