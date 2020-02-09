<template>
	<view>
		
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="false">
			<block slot="content">工作</block>
		</cu-custom>
		
		<view class="cu-list grid col-3 no-border margin-top-xl">
			<view class="cu-item">
				<view class="flex justify-center">
					<image src="../../static/work/work_icon.png" style="width: 80upx; height: 80upx;"></image>
				</view>
				<text class="margin-top-sm">施工安装</text>
			</view>
			<view class="cu-item">
				<view class="flex justify-center">
					<image src="../../static/work/danger_icon.png" style="width: 80upx; height: 80upx;"></image>
				</view>
				<text class="margin-top-sm">隐患整改</text>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar bg-white">
				<!-- <navigator hover-class="none" :url="'../admin_home/admin_home'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/home-normal.png"></image>
					</view>
					<view class="text-blackb">首页</view>
				</navigator> -->
				<navigator hover-class="none" :url="'../admin_device/admin_device'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_normal.png"></image>
					</view>
					<view class="text-black">设备</view>
				</navigator>
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/work-activate.png"></image>
					</view>
					<view class="text-light-purple">工作</view>
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
