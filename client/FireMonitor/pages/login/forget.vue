<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
		    <block slot="content">重置密码</block>
		</cu-custom>
        ﻿<form>

        <view class="cu-form-group margin-top">
            <view class="title">新密码</view>
            <input placeholder="请输入新密码" name="input"></input>
        </view>

        <view class="cu-form-group">
            <view class="title">新密码</view>
            <input placeholder="请再次输入新密码" name="input"></input>
        </view>
    </form>

        <view class="flex text-sm padding justify-center margin-top">
            <view class="text-grey">密码长度8-32位，须包含数字、字母、符号至少2种或以上元素</view>
        </view>

        <view class="padding flex flex-direction">
            <button class="cu-btn bg-dark-purple lg">确认修改</button>
        </view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
