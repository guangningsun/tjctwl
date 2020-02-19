事件API设计
====================


事件API
^^^^^^^^^^^^

- 查询事件列表

 获取按最新时间排序的事件列表，可以添加条件搜索

::

   get_event_list

   参数：
      user_id
      start_index - 事件起始索引，传 "0" 表示从最新的第一个开始查（必要）
      num - 步长，即每次查询的个数，用于分页查询 (默认 20)
      start_time - 时间条件搜索，起始时间(非必要)
      end_time - 时间条件搜索，结束时间（非必要）
      event_msg - 内容条件搜索，内容模糊查询（非必要）
      device_location - 设备位置条件查询，模糊查询（非必要）

   返回值：
      event_info_list - 事件查询结果列表
      ------------
      event_info:
        event_id - 事件id
        event_msg - 事件内容
        device_location - 设备安装位置
        event_time - 事件时间
        read_state - 是否已读 ( "0" : 未读    "1" : 已读)

- 修改事件状态

 修改事件为已读状态

::

   update_event_read_state

   参数：
      event_id - 事件id

   返回值：

- 全部已读

  修改该用户下所有事件为已读状态

::

  update_event_read_state_all

  参数：
     event_id - 事件id

  返回值：
