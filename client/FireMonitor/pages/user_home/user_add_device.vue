<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">添加设备</block>
		</cu-custom>

		<view class="cu-card">
			<view class="cu-item">

				<view class="flex justify-center margin-top margin-bottom-xs" @tap="openScan">
					<image class="flex justify-center margin-top margin-bottom-sm" src="../../static/home/qrcodescan.png" style="width: 200upx; height: 200upx;"></image>
				</view>

				<view class="flex justify-center text-gray">
					扫一扫获取设备基本信息
				</view>

				<form>
					<view class="cu-form-group margin-top">
						<view class="title">设备编码</view>
						<input placeholder="设备的编码" name="input" v-model="device_sn"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">设备名称</view>
						<input placeholder="设备的名称" name="input" v-model="name"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">地址</view>
						<input placeholder="设备所在的地址" name="input" v-model="address"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">安装位置</view>
						<input placeholder="设备的安装位置" name="input" v-model="location"></input>
					</view>
				</form>
			</view>

			<!-- 			<view class="cu-card cu-item">
				<view class="cu-form-group">
					<view class="title">报警时是否启用电话通知</view>
					<switch class="light-purple" @change="switchEnableTel" :class="tel_notic?'checked':''" :checked="switchA?true:false"></switch>
				</view>
				<view class="cu-form-group">
					<view class="title">报警时是否启用短信通知</view>
					<switch class="light-purple" @change="switchEnableSms" :class="sms_notic?'checked':''" :checked="switchB?true:false"></switch>
				</view>
			</view> -->

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
				tel_notic: false,
				sms_notic: false,
				device_sn: '',
				name: '',
				address: '',
				location: '',
			}
		},
		// onLoad: function(option) {
		// 	this.showToast("load");
		// 	// 接收扫码的值
		// 	uni.$on("scanResult", function(data) {
		// 		this.showToast(data.result);
		// 		uni.showToast({
		// 			title: data.result
		// 		})
		// 		_this.device_sn = data.result;
		// 	});

		// },

		onLoad() {
			this.showToast("load");
			// 接收扫码的值
			uni.$on('scanResult', (data) => {
				this.device_sn = data.result;
			});
		},
		onUnload() {
			// 移除监听事件  
			uni.$off('scanResult');
		},
		methods: {
			successCallback(rsp) {
				if (rsp.data.error === 0) {
					this.showToast('成功添加设备!');
					uni.navigateBack({
						delta: 1
					});
				}
			},
			failCallback(err) {
				console.log('api_bound_device failed', err);
			},
			completeCallback(rsp) {},
			onAddDevice() {
				let user_id = getApp().globalData.user_id;
				if (this.isEmpty(user_id)) {
					user_id = uni.getStorageSync('key_user_id');
				}
				let params = {
					device_sn: this.device_sn,
					name: this.name,
					address: this.address,
					location: this.location,

				};
				if (this.isEmpty(this.device_sn) || this.isEmpty(this.name) ||
					this.isEmpty(this.address) || this.isEmpty(location)) {
					this.showToast("请检查输入!");
					return;
				}
				this.requestWithMethod(getApp().globalData.api_device_opt + user_id + '/', "PUT", params, this.successCallback,
					this.failCallback,
					this.completeCallback);
			},
			switchEnableTel(e) {
				this.switch_enable_tel = e.detail.value
			},
			switchEnableSms(e) {
				this.switch_enable_sms = e.detail.value
			},
			// 扫码
			openScan() {
				uni.navigateTo({
					url: '../scan/scan'
				});
			},

		}
	}
</script>

<style>

</style>
