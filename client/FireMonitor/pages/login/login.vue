<template>
	<view class="content">
		<view class="mak-box">
			<image src="../../static/login.png" mode='aspectFit' class="mak-logo"></image>
			<view class="mak-title">天津城投物联</view>

			<view class="flex padding align-center radius">
				<form>
					<view class="cu-form-group">
						<view class="title">用户名</view>
						<input placeholder="请输入用户名" name="input" v-model="user_name"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">密&nbsp&nbsp&nbsp码</view>
						<input password placeholder="请输入密码" name="input" v-model="user_pwd" data-val="password"></input>
					</view>
				</form>

			</view>
		</view>

		<view class="justify-between bottom-box">
			﻿<view class="flex text-df padding justify-center">
				<!-- <navigator ﻿hover-class="none" :url="'forget'" class="text-grey">忘记密码？</navigator> -->
				<view class="text-grey" @tap="showForgetToast">忘记密码？</view>
			</view>

			<view class="padding flex flex-direction">
				<button class="cu-btn bg-dark-purple lg" @click="onLogin">登录</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user_type: 0,
				user_name: '',
				user_pwd: ''
			}
		},
		onBackPress() {
			return;
		},
		methods: {
			successCallback(res) {
				uni.hideLoading();
				if (res.data.error === 0) {
					let rspData = res.data.msg;
					let user_type = rspData.user_permission;
					this.saveUserData(rspData);
					// console.log('phone:' + uni.getStorageSync('key_phone_number'));
					// 管理员跳转
					if (user_type === '0') {
						uni.navigateTo({
							url: "../admin_home/admin_home",
						});
					}
					// 普通用户跳转
					else if (user_type === '1') {
						uni.navigateTo({
							url: "../user_home/user_home",
						});
					}
				}
			},
			failCallback(err) {
				uni.hideLoading();
				this.showToast('登录失败!')
				console.log("登录失败：" + err.errMsg);
			},
			completeCallback (rsp) {
				if(rsp.data == undefined){
					return;
				}
				if (rsp.data.error === 1) {
					if (rsp.data.msg.indexOf('doesn`t match') != -1) {
						getApp().showToast('用户名或密码不正确，\n 请核实后输入')
					} else{
						getApp().showToast('登录失败，请核实')
					}
				}
			},
			onLogin() {
				uni.showLoading({
					title:'正在登录'
				})
				let params = {
					username: this.user_name,
					password: this.user_pwd
				};
				this.request(getApp().globalData.api_login, params, this.successCallback, this.failCallback, this.completeCallback);
			},
			showForgetToast() {
				this.showToast('请联系管理员更改密码')
			},
			saveUserData(rspData) {
				getApp().globalData.user_id = rspData.id;
				uni.setStorage({
					key: 'key_user_id',
					data: rspData.id,
				});
				uni.setStorage({
					key: 'key_login_name',
					data: rspData.login_name,
				});
				uni.setStorage({
					key: 'key_password',
					data: rspData.password,
				});
				uni.setStorage({
					key: 'key_user_name',
					data: rspData.username,
				});
				uni.setStorage({
					key: 'key_user_type',
					data: rspData.user_permission,
				});
				uni.setStorage({
					key: 'key_phone_number',
					data: rspData.phone_number,
				});
				uni.setStorage({
					key: 'key_user_sex',
					data: rspData.user_sex,
				});
				uni.setStorage({
					key: 'key_user_age',
					data: rspData.user_age,
				});
			}
		}
	}
</script>

<style>
	.mak-box {
		padding: 100upx 100upx;
		position: relative;
		background-color: #FFFFFF;
	}

	.content {
		background-color: #FFFFFF;
		min-height: 100vh;
	}

	.bottom-box {
		padding: 20upx 20upx;
		position: relative;
		background-color: #FFFFFF;
	}

	.mak-logo {
		width: 100%;
		width: 100%;
		height: 310upx;
	}

	.mak-title {
		position: absolute;
		top: 0;
		line-height: 500upx;
		font-size: 56upx;
		color: #fff;
		text-align: center;
		width: 100%;
		margin-left: -100upx;
	}
</style>
