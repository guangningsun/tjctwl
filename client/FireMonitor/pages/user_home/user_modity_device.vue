<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">设备信息修改</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">

				<view class="padding-sm cf">
					<view class="fl flex align-center">
						<image style="width: 35upx;height: 35upx; margin-right: 15upx;" src="/static/home/signal.png"></image>
						<view class="cu-tag radius bg-gradual-green text-sm" style="margin-right: 10upx; padding: 8upx;">正常</view>
					</view>

					<view class="flex fr align-center">
						<image style="width: 55upx;height: 55upx; margin-right: 15upx;" src="/static/home/battery.png"></image>
						<view class="cu-tag radius line-black text-xs" style="margin-right: 10upx; padding: 8upx;">100%</view>
					</view>
				</view>

				<view class="flex justify-center margin-top margin-bottom">
					<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>
				</view>
				
				<view class="flex cu-form-group">
					<view class="title">设备编码</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">设备类型</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">IMEI</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">ICCID</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">地址</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">详细地址</view>
					<input placeholder="111" name="input"></input>
				</view>
				<view class="flex cu-form-group">
					<view class="title">场所名</view>
					<input placeholder="111" name="input"></input>
				</view>
				
			</view>
		</view>

		<view class="justify-between bottom-box">
			<view class="padding flex flex-direction">
				<button class="cu-btn bg-dark-purple lg" @click="onConfirm">确认修改</button>
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
