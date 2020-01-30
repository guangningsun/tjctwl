系统管理 API设计
====================


设备管理 API
^^^^^^^^^^^^

- 系统初始化设置

::

  pip install django-import-export
  python manage.py collectstatic
  pip install django-simpleui

- 新增设备

::

   add_device

- 批量导入设备


::

  upload_device


- 删除设备

::

    delete_device

- 获取设备


:: 

   get_all_device

- 修改设备信息
   
::

   update_device




绑定记录 API
^^^^^^^^^^^^


角色管理 API
^^^^^^^^^^^^

-  获取全部角色

::
  
   get_all_roles

-  新增角色

::
   
   add_role

-  删除角色


::

   delete_role


- 修改角色

::
    update_role



用户管理 API
^^^^^^^^^^^^

- 新增用户

::

   add_user

- 创建初始化用户

::

  python manage.py createsuperuser

- 删除用户

:: 

   delete_user

- 查询所有用户


::

   get_all_users


- 修改用户


::

   update_user


机构管理 API
^^^^^^^^^^^^


- 新增机构

::

   add_institution


- 删除机构

::

  delete_institution


- 查询机构

::

   get_all_institution

- 修改机构

::

  update_institution


联网单位管理API
^^^^^^^^^^^^^^^^^

- 获取联网单位信息

::
   
   get_unit_info

- 