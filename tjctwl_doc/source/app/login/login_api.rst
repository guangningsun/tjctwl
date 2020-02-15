登录 API设计
====================


登录 API
^^^^^^^^^^^^

- 登录

::

    user_login

    参数：
        username - 用户名
        password - 登录密码
    返回值：
    成功后返回如下数据

    {
    "error": 0,
    "msg": {
        "id": "22",
        "login_name": "mm",
        "username": "mm",
        "password": "mm",
        "user_permission": "0",
        "phone_number": "122222222",
        "create_time": "11111",
        "description": "11111",
        "user_sex": "男",
        "user_age": "30"
        }
    }
    
    失败后返回如下数据

    {
        "error": 1,
        "msg": "login false"
    }

- 用户登出

  用户登出

::

    user_logout

    参数：
        user_id - 用户ID
    返回值：

- 重置密码

::

    reset_password
    参数：
        old_password - 旧密码
        new_password - 新密码
    返回值：
