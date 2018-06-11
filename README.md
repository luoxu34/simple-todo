# simple todo

simple-todo uses the flask web framework, created by RESTful APIs.

# Models

table name: todos

| Column Name | Type         | Nullable | Explain                   |
| :---------- | :----------- | :------- | :------------------------ |
| id          | String(64)   | False    | primary_key               |
| title       | String(128)  | False    | task name                 |
| complete    | Boolean      | False    | default is False          |
| notes       | String(1024) | True     | more explanation          |
| create_time | DateTime     | False    | format is %y-%m-%d %h%m%s |
| deadline    | DateTime     | True     | deadline                  |
| tag         | String(64)   | True     | for classification        |

# RESTful API

| Method | URL       | Code | Explain     |
| :----- | :-------- | :--- | :---------- |
| GET    | /todos/   | 200  | 获取所有任务 |
| GET    | /todos/id | 200  | 获取指定任务 |
| POST   | /todos/   | 201  | 提交新的任务 |
| PATCH  | /todos/id | 200  | 更新执行任务 |
| DELETE | /todos/id | 204  | 删除指定任务 |

# The Next?
* User authentication
* Multilingual support
* Sphinx API doc
* More database support, such as MySQL, ProgreSQL, MongoDB
* Database migration module
* Unittest and coverage
* CLI support
* Containerization
* ...
