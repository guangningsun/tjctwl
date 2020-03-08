<template>
	<view>
		<mask v-if="showMask"></mask>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="false">
			<block slot="content">设备</block>
		</cu-custom>

		<view class="box">

			<view> admin-device</view>

			<view class="cu-bar mytabbar foot tabbar bg-white">
				<!-- <navigator hover-class="none" :url="'../admin_home/admin_home'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/home-normal.png"></image>
					</view>
					<view class="text-blackb">首页</view>
				</navigator> -->
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_activate.png"></image>
					</view>
					<view class="text-light-purple">设备</view>
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
	import mask from '../../components/mask.vue';
	export default {
		data() {
			return {
				showMask: false,
			}
		},
		components: {
			mask
		},
		onBackPress() {
			if (this.showMask) {
				this.showMask = false;
				return true;
			} else {
				this.showQuitDialog();
				return true;
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
