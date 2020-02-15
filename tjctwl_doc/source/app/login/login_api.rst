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
