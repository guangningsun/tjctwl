<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">添加设备</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">

				<view class="flex justify-center margin-top margin-bottom-xs">
					<image class="flex justify-center margin-top margin-bottom-sm" src="../../static/home/qrcodescan.png" style="width: 200upx; height: 200upx;"></image>
				</view>

				<view class="flex justify-center text-gray">
					扫一扫获取设备基本信息
				</view>

				<form>
					<view class="cu-form-group margin-top">
						<view class="title">邮件</view>
						<input placeholder="两字短标题" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">输入框</view>
						<input placeholder="三字标题" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">收货地址</view>
						<input placeholder="统一标题的宽度" name="input"></input>
					</view>
				</form>

				<!-- <view class="flex-twice padding-sm" style="font-size: 26upx;">
						<view class="flex align-center">
							<view class="text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">设备编码:</view>
							<view class="text-black margin-top-sm text-cut" style="width: 250upx;">xxxxxxxxxx</view>
						</view>
						<view class="flex align-center">
							<view class="text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">设备编码:</view>
							<view class="text-black margin-top-sm text-cut" style="width: 250upx;">xxxxxxxxxx</view>
						</view>
						<view class="flex align-center">
							<view class="text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">设备编码:</view>
							<view class="text-black margin-top-sm text-cut" style="width: 250upx;">xxxxxxxxxx</view>
						</view>
						<view class="flex align-center">
							<view class="text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">设备编码:</view>
							<view class="text-black margin-top-sm text-cut" style="width: 250upx;">xxxxxxxxxx</view>
						</view>
						<view class="flex align-center">
							<view class="text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">设备编码:</view>
							<view class="text-black margin-top-sm text-cut" style="width: 250upx;">xxxxxxxxxx</view>
						</view>
					</view>
					<view class="flex-sub">
						<view class="flex align-end padding-sm">
							<image style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></image>
							<view class="cu-tag radius bg-orange2 text-xs" style="margin-right: 10upx; padding: 8upx;">故障</view>
							<image style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></image>
							<view class="cu-tag radius line-black text-xs" style="padding: 3upx;">100%</view>
						</view>
		
						<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>
		
					</view> -->

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

</style>
