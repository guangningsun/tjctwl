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
				shouldRequestModify: false,
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
			successUpdateDeviceCb(rsp) {
				uni.hideLoading();

				if (rsp.data.error === 0) {
					console.log('successUpdateDeviceCb');
					uni.showToast({
						title: "成功添加设备"
					})
				}
				setTimeout(function() {
					 uni.navigateBack({
					 	delta: 1
					 });
				}, 1500)
			},
			failUpdateDeviceCb(err) {
				uni.hideLoading();
				console.log('api_device failed: 设备成功添加，但是修改设备修复失败' + err);
				this.showToast("设备成功添加，但是修改设备修复失败");
				setTimeout(function() {
					 uni.navigateBack({
					 	delta: 1
					 });
				}, 1500);
			},
			completeUpdateDeviceCb(rsp) {},

			successCallback(rsp) {
				if (rsp.data.error === 0) {
					if (this.shouldRequestModify) {
						//修改设备信息
						let user_id = getApp().globalData.user_id;
						if (this.isEmpty(user_id)) {
							user_id = uni.getStorageSync('key_user_id');
						}
						let params = {
							user_id: user_id,
							device_name: this.name,
							device_address: this.address,
							install_location: this.location,
						};
						this.requestWithMethod(
							getApp().globalData.api_device + this.device_sn + '/',
							"PUT",
							params,
							this.successUpdateDeviceCb,
							this.failUpdateDeviceCb,
							this.completeUpdateDeviceCb);
					} else {
						uni.hideLoading();

						setTimeout(function() {
							uni.navigateBack({
								delta: 1
							});
						}, 1500);
					}

				}
			},
			failCallback(err) {
				uni.hideLoading();
				console.log('api_device_opt failed', err);
			},
			completeCallback(rsp) {},
			onAddDevice() {
				if (!this.isEmpty(this.name) ||
					!this.isEmpty(this.address) ||
					!this.isEmpty(this.location)) {
					this.shouldRequestModify = true;
				}
				uni.showLoading({
					title: '正在添加设备',
				})
				let user_id = getApp().globalData.user_id;
				if (this.isEmpty(user_id)) {
					user_id = uni.getStorageSync('key_user_id');
				}
				let params = {
					device_sn: this.device_sn
				};
				if (this.isEmpty(this.device_sn)) {
					this.showToast("请至少输入设备编码!");
					return;
				}
				this.requestWithMethod(
					getApp().globalData.api_device_opt + user_id + '/',
					"PUT",
					params,
					this.successCallback,
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
