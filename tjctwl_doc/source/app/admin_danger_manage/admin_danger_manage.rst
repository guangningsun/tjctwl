隐患整改API设计
====================


隐患整改API
^^^^^^^^^^^^

- 获取待整改隐患列表

 获取待整改隐患列表

::

   get_danger_todo_list

   参数：
     start_index - 索引，传 "0" 表示从第一个开始查
     num - 步长，即每次查询的个数，用于分页查询 (默认 20)

   返回值：
     danger_todo_info_list - 待整改隐患列表
     ----------------
     danger_todo_info:
       submitter - 上报人
       class - 隐患等级
       type - 隐患类别
       floor - 隐患楼层
       location - 具体位置
       description - 隐患描述
       photo - 隐患照片
       date - 上报时间
       status - 任务状态

- 更新整改隐患任务

  更新整改隐患任务，如领取任务、整改完毕、驳回。

::

  update_danger_status

  参数：
    id - id
    status - 任务状态

  返回值：


- 获取整改中隐患列表

  获取整改中隐患列表

::

  get_danger_doing_list

  参数：
    start_index - 索引，传 "0" 表示从第一个开始查
    num - 步长，即每次查询的个数，用于分页查询 (默认 20)

  返回值：
    danger_doing_info_list - 整改中隐患列表
    ----------------
    danger_doing_info:
      id - id
      submitter - 上报人
      class - 隐患等级
      type - 隐患类别
      floor - 隐患楼层
      location - 具体位置
      description - 隐患描述
      photo - 隐患照片
      date - 上报时间
      status - 任务状态

      (列表,因为会有多次整改) :
      reform_desc - 整改描述
      reform_photo - 整改照片


- 添加整改中描述和照片

  整改描述和照片信息。

::

  add_danger_doing_info

  参数：
    id - id
    reform_desc - 整改描述
    reform_photo - 整改照片

  返回值：


- 获取整改完成隐患列表

  获取整改完成隐患列表

::

  get_danger_done_list

  参数：
    start_index - 索引，传 "0" 表示从第一个开始查
    num - 步长，即每次查询的个数，用于分页查询 (默认 20)

  返回值：
    danger_doing_done_list - 整改完成隐患列表
    ----------------
    danger_done_info:
      id - id
      submitter - 上报人
      class - 隐患等级
      type - 隐患类别
      floor - 隐患楼层
      location - 具体位置
      description - 隐患描述
      photo - 隐患照片
      date - 上报时间
      status - 任务状态

      (列表,因为会有多次整改) :
      reform_desc - 整改描述
      reform_photo - 整改照片
