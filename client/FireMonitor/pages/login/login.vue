<template>
	<view class="content">
		<view class="mak-box">
			<image src="../../static/login.png" mode='aspectFit' class="mak-logo"></image>
			<view class="mak-title">天津城投物联</view>

			<view class="flex padding align-center radius">
				<form>
					<view class="cu-form-group">
						<view class="title">用户名</view>
						<input placeholder="请输入用户名" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">密&nbsp&nbsp&nbsp码</view>
						<input placeholder="请输入密码" name="input"></input>
					</view>
				</form>

			</view>
		</view>

		<view class="justify-between bottom-box">
			﻿<view class="flex text-df padding justify-center">
				<navigator ﻿hover-class="none" :url="'forget'" class="text-grey">忘记密码？</navigator>
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
				
			}
		},
		methods: {
			onLogin(){
				uni.navigateTo({
					url:"../user_home/user_home",
				})
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
