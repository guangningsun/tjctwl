登录 API设计
====================


登录 API
^^^^^^^^^^^^

- 获取用户类型

::

   get_user_type

   参数：
       user_id - 用户ID
   返回值：
       user_type: “0” - 管理员
                  “1” - 普通用户

- 获取用户类型

::

    user_login

    参数：
        user_id - 用户ID
        pass - 登录密码
    返回值：

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
