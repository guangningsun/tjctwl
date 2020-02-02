<template>
	<view>

		<view class="box">

			<view> admin-home</view>

			<view class="cu-bar mytabbar foot tabbar bg-white">
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/home-activate.png"></image>
					</view>
					<view class="text-light-purple">首页</view>
				</navigator>
				<navigator hover-class="none" :url="'../admin_device/admin_device'" class="action">
				    <view class="cuIcon-cu-image">
				        <image src="/static/tabbar/device_normal.png"></image>
				    </view>
				    <view class="text-black">设备</view>
				</navigator>
				<navigator hover-class="none" :url="'../admin_work/admin_work'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/work-normal.png"></image>
					</view>
					<view class="text-black">工作</view>
				</navigator>
				<navigator hover-class="none" :url="'../admin_event/admin_event'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_normal.png"></image>
					</view>
					<view class="text-black">事件</view>
				</navigator>
				<navigator hover-class="none" :url="'../admin_me/admin_me'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/me-normal.png"></image>
					</view>
					<view class="text-blackb">我的</view>
				</navigator>
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

		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	}
</style>
