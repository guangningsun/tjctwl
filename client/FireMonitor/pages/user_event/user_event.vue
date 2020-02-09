<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="false">
			<block slot="content">事件</block>
		</cu-custom>
		
		<view class="box">
			<view class="cu-bar bg-gradual-dark-purple search">
				<view class="search-form radius">
					<text class="cuIcon-search"></text>
					<input @focus="InputFocus" @blur="InputBlur" :adjust-position="false" type="text" placeholder="搜索事件"
					 confirm-type="search"></input>
				</view>
				<view class="action">
					<text class="cuIcon-calendar"></text>
				</view>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar bg-white">
				<navigator hover-class="none" :url="'../user_home/user_home'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_normal.png"></image>
					</view>
					<view class="text-black">设备</view>
				</navigator>
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_activate.png"></image>
					</view>
					<view class="text-light-purple">事件</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_me/user_me'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/me-normal.png"></image>
					</view>
					<view class="text-black">我的</view>
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
