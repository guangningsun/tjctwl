<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">修改密码</block>
		</cu-custom>
		﻿<form>

			<view class="cu-form-group margin-top">
				<view class="title">原密码</view>
				<input password placeholder="请输入旧密码" name="input" v-model="old_pass"></input>
			</view>

			<view class="cu-form-group margin-top">
				<view class="title">新密码</view>
				<input password placeholder="请输入新密码" name="input" v-model="new_pass"></input>
			</view>

			<view class="cu-form-group">
				<view class="title">新密码</view>
				<input password placeholder="请再次输入新密码" name="input" v-model="new_pass_2"></input>
			</view>
		</form>

		<view class="flex text-sm padding justify-center margin-top">
			<view class="text-grey">密码长度8-32位，须包含数字、字母、符号至少2种或以上元素</view>
		</view>

		<view class="padding flex flex-direction">
			<button class="cu-btn bg-dark-purple lg" @tap="onModifyPass">确认修改</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				old_pass: '',
				new_pass: '',
				new_pass_2: '',
			}
		},
		methods: {
			onModifyPass(){
				let real_old_pass = uni.getStorageSync('key_password');
				let user_id = getApp().globalData.user_id;
				if(this.new_pass === this.new_pass_2 && real_old_pass === this.old_pass){
					uni.request({
						url: getApp().globalData.domain_port + getApp().globalData.api_reset_pass,
						method: "POST",
						dataType: 'json',
						header: {
							'Content-Type': 'application/x-www-form-urlencoded'
						},
						data: {
							old_password: this.old_pass,
							new_password: this.new_pass,
							user_id: user_id
						},
						success: res => {
					        if (res.data.error === 0) {
								uni.showToast({
									title:'修改密码成功！'
								});
								uni.setStorage({
									key: 'key_password',
									data: this.new_pass,
								});
								uni.navigateBack({
									delta: 1
								});
					        }
						},
						fail: (err) => {
							console.log('modify pass failed', err);
							uni.showToast({
								title:'修改密码失败:' + err,
								icon:'none',
							})
						},
						complete: () => {}
					});
				}
				else if (this.new_pass !== this.new_pass_2){
					uni.showToast({
						title:'再次输入不一致！请重新输入！',
						icon:'none',
					})
				}
				else if (real_old_pass !== this.old_pass){
					uni.showToast({
						title:'原密码不正确，请核实后输入！',
						icon:'none',
					})
				}
			}
		}
	}
</script>

<style>

</style>
