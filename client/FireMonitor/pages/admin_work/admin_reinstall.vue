<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">重装</block>
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
						<view class="title">业主电话</view>
						<input placeholder="请输入业主电话" name="input"></input>
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
						<view>
							<view class="title">地图位置</view>
							<map :latitude="latitude" :longitude="longitude" :markers="covers"></map>
						</view>
					</view>
					<view class="cu-bar bg-white margin-top solid-top">
						<view class="action">
							安装照片
						</view>
						<view class="action">
							{{imgList.length}}/4
						</view>
					</view>
					<view class="cu-form-group margin-bottom-sm">
						<view class="grid col-4 grid-square flex-sub">
							<view class="bg-img" v-for="(item,index) in imgList" :key="index" @tap="ViewImage" :data-url="imgList[index]">
								<image :src="imgList[index]" mode="aspectFill"></image>
								<view class="cu-tag bg-red" @tap.stop="DelImg" :data-index="index">
									<text class='cuIcon-close'></text>
								</view>
							</view>
							<view class="solids" @tap="ChooseImage" v-if="imgList.length<4">
								<text class='cuIcon-cameraadd'></text>
							</view>
						</view>
					</view>
				</form>
			</view>

			<view class="justify-between bottom-box">
				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @tap="onAddDevice">添加</button>
				</view>
			</view>
		</view>

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
				modalName: null,
				hasLocation: false,
				latitude: 39.909,
				longitude: 116.39742,
				covers: [{
					latitude: this.latitude,
					longitude: this.longitude,
					iconPath: '/../../static/pin.png'
				}],
				imgList: []
			}
		},
		onReady() {
			this.getLocation();
		},
		methods: {
			showModal(e) {
				this.modalName = 'PermissionModal'
			},
			hideModal(e) {
				this.modalName = null
			},
			DelImg(e) {
				uni.showModal({
					title: '删除照片',
					content: '确定要删除这张照片吗？',
					cancelText: '否',
					confirmText: '是',
					success: res => {
						if (res.confirm) {
							this.imgList.splice(e.currentTarget.dataset.index, 1)
						}
					}
				})
			},
			ChooseImage() {
				uni.chooseImage({
					count: 4, //默认9
					sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
					sourceType: ['album', 'camera'],
					success: (res) => {
						if (this.imgList.length != 0) {
							this.imgList = this.imgList.concat(res.tempFilePaths)
						} else {
							this.imgList = res.tempFilePaths
						}
					}
				});
			},
			// togglePopup(type) {
			// 	this.type = type;
			// },
			// showConfirm() {
			// 	this.type = 'showpopup';
			// },
			// hideConfirm() {
			// 	this.type = '';
			// },
			async getLocation() {
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
						this.latitude = res.latitude;
						this.longitude = res.longitude;
						this.covers[0].latitude = res.latitude;
						this.covers[0].longitude = res.longitude;
						this.covers[0].iconPath = '/../../static/pin.png';
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
