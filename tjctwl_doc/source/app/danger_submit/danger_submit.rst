隐患上报API设计
====================


隐患上报API
^^^^^^^^^^^^

- 添加隐患

 添加隐患

::

   danger

   请求方式：
   post

   参数：
      danger_create_user - 上报人
      danger_floor_level - 隐患楼层
      danger_address_detail - 具体位置
      danger_desc - 隐患描述
      danger_image - 隐患照片
      danger_create_time - 添加时间

   返回值：

- 隐患整改列表

 获取隐患整改列表

::

   danger

   请求方式：
   get

   参数：
    user_id

   返回值：
    danger_list - 隐患列表
    ------------
      danger_info:
        submitter - 上报人
        class - 隐患等级
        type - 隐患类别
        floor - 隐患楼层
        location - 具体位置
        description - 隐患描述
        photo - 隐患照片
        date - 上报时间
        status - 任务状态
        feedback - 后台反馈
