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
						<view class="title">设备编码</view>
						<input placeholder="设备的编码" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">设备名称</view>
						<input placeholder="设备的型号" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">地址</view>
						<input placeholder="设备所在的省市区" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">详细地址</view>
						<input placeholder="如道路/门牌号/小区/楼栋号/单元/室等" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">安装位置</view>
						<input placeholder="设备的安装位置" name="input"></input>
					</view>
				</form>
			</view>

			<view class="cu-card cu-item">
				<view class="cu-form-group">
					<view class="title">报警时是否启用电话通知</view>
					<switch @change="switchEnableTel" :class="switch_enable_tel?'checked':''" :checked="switchA?true:false"></switch>
				</view>
			</view>

			<view class="justify-between bottom-box">
				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @click="onAddDevice">添加</button>
				</view>
			</view>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				switch_enable_tel: false,
			}
		},
		methods: {
			onAddDevice() {

			},
			switchEnableTel(e) {
				this.switch_enable_tel = e.detail.value
			},
		}
	}
</script>

<style>

</style>
