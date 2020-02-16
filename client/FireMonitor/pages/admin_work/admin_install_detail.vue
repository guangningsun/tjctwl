<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">安装详情</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">
				<view class="bg-white">
					<view class="flex justify-center margin-top margin-bottom">
						<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>
					</view>
				</view>

				<view class="flex cu-form-group">
					<view class="title">设备编码</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">设备名称</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">设备型号</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">业主姓名</view>
					<view>XXX</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">业主电话</view>
					<view>18635969580</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">地址</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">详细地址</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">安装位置</view>
					<view>XXX</view>
				</view>
				<view class="cu-form-group">
					<view class="padding-bottom-sm">
						<view class="title margin-top-sm">地图位置</view>
						<map :latitude="latitude" :longitude="longitude" :markers="covers"></map>
					</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">安装时间</view>
					<view>2020-02-14 10:00</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				latitude: 39.909,
				longitude: 116.39742,
			}
		},
		methods: {

		}
	}
</script>

<style>

</style>
