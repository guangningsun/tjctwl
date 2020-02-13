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
						<input placeholder="设备的名称" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">设备型号</view>
						<input placeholder="设备的型号" name="input"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">业主姓名</view>
						<input placeholder="请输入业主姓名" name="input"></input>
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
					<view class="cu-form-group">
						<view class="title">地图位置</view>

					</view>

				</form>
			</view>

			<view class="justify-between bottom-box">
				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @click="onAddDevice">添加</button>
				</view>
			</view>
		</view>
<!-- 		<uni-popup :show="type === 'showpopup'" mode="fixed" @hidePopup="togglePopup('')">
			<view class="popup-view">
				<text class="popup-title">需要用户授权位置权限</text>
				<view class="uni-flex popup-buttons">
					<button class="uni-flex-item" type="primary" open-type="openSetting" @tap="openSetting">设置</button>
					<button class="uni-flex-item" @tap="togglePopup('')">取消</button>
				</view>
			</view>
		</uni-popup> -->

		<!-- 申请权限modal -->
		<view class="cu-modal bottom-modal" :class="modalName=='PermissionModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">位置权限申请</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
				<view class="padding-xl">
					需要用户授权位置权限
				</view>
				<view class="cu-bar bg-white">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" type="primary" open-type="openSetting" @tap="openSetting">设置</button>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	var util = require('../../common/util.js');
	var formatLocation = util.formatLocation;
	// #ifdef APP-PLUS
	import permision from "@/common/permission.js"
	// #endif

	export default {
		data() {
			return {
				imgList: ['111', '222'],
				title: 'getLocation',
				hasLocation: false,
				location: {},
				type: ''
			}
		},
		onReady() {
			this.getLocation();
		},
		methods: {
			togglePopup(type) {
				this.type = type;
			},
			showConfirm() {
				this.type = 'showpopup';
			},
			hideConfirm() {
				this.type = '';
			},
			async getLocation() {
				uni.showToast({
					title: "getLocation"
				});
				// #ifdef APP-PLUS
				let status = await this.checkPermission();
				if (status !== 1) {
					return;
				}
				// #endif
				// #ifdef MP-WEIXIN || MP-TOUTIAO || MP-QQ
				let status = await this.getSetting();
				if (status === 2) {
					this.showConfirm();
					return;
				}
				// #endif

				this.doGetLocation();
			},
			doGetLocation() {
				uni.getLocation({
					success: (res) => {
						this.hasLocation = true;
						this.location = formatLocation(res.longitude, res.latitude);
					},
					fail: (err) => {
						// #ifdef MP-BAIDU
						if (err.errCode === 202 || err.errCode === 10003) { // 202模拟器 10003真机 user deny
							this.showConfirm();
						}
						// #endif
						// #ifndef MP-BAIDU
						if (err.errMsg.indexOf("auth deny") >= 0) {
							uni.showToast({
								title: "访问位置被拒绝"
							})
						} else {
							uni.showToast({
								title: err.errMsg
							})
						}
						// #endif
					}
				})
			},
			getSetting: function() {
				return new Promise((resolve, reject) => {
					uni.getSetting({
						success: (res) => {
							if (res.authSetting['scope.userLocation'] === undefined) {
								resolve(0);
								return;
							}
							if (res.authSetting['scope.userLocation']) {
								resolve(1);
							} else {
								resolve(2);
							}
						}
					});
				});
			},
			openSetting: function() {
				this.hideConfirm();
				uni.openSetting({
					success: (res) => {
						if (res.authSetting && res.authSetting['scope.userLocation']) {
							this.doGetLocation();
						}
					},
					fail: (err) => {}
				})
			},
			async checkPermission() {
				let status = permision.isIOS ? await permision.requestIOS('location') :
					await permision.requestAndroid('android.permission.ACCESS_FINE_LOCATION');

				if (status === null || status === 1) {
					status = 1;
				} else if (status === 2) {
					uni.showModal({
						content: "系统定位已关闭",
						confirmText: "确定",
						showCancel: false,
						success: function(res) {}
					})
				} else if (status.code) {
					uni.showModal({
						content: status.message
					})
				} else {
					uni.showModal({
						content: "需要定位权限",
						confirmText: "设置",
						success: function(res) {
							if (res.confirm) {
								permision.gotoAppSetting();
							}
						}
					})
				}

				return status;
			},
		}
	}
</script>

<style>

</style>
