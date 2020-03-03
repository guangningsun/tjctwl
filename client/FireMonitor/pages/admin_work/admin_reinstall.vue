<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">重装设备</block>
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
						<input :placeholder="device_sn === '' ? ph_device_sn : device_sn" :disabled="shouldDisableInputSn" name="input"
						 @blur="onEnterDeviceSn" v-model="device_sn"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">设备名称</view>
						<input :placeholder="device_name === '' ? ph_device_name :device_name" name="input" v-model="device_name"></input>
					</view>
					<!-- <view class="cu-form-group">
						<view class="title">业主姓名</view>
						<input :placeholder="owner_str === '' ?  ph_owner_str : owner_str" name="input"  v-model="owner_str"></input>
					</view> -->
					<view class="cu-form-group">
						<view class="title">业主电话</view>
						<input :placeholder="owner_tel_str === '' ?  ph_owner_tel_str : owner_tel_str" name="input" v-model="owner_tel_str"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">地址</view>
						<input :placeholder="device_address === '' ? ph_device_address : device_address" name="input" v-model="device_address"></input>
					</view>

					<view class="cu-form-group">
						<view class="title">安装位置</view>
						<input :placeholder="install_location === '' ?  ph_install_location : install_location" name="input" v-model="install_location"></input>
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
							{{imgList.length}}/1
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
							<view class="solids" @tap="ChooseImage" v-if="imgList.length<1">
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
				modalName: null,
				hasLocation: false,
				latitude: 39.909,
				longitude: 116.39742,
				covers: [{
					latitude: this.latitude,
					longitude: this.longitude,
					iconPath: '/../../static/pin.png'
				}],
				imgList: [],

				id: "",
				construction_createtime: "",
				deviceStatus: "",
				construction_image: "",
				device_sn: "",
				device_name: "",
				construction_worker: "",
				install_location: "",
				device_address: "",
				owner_str: '',
				owner_tel_str: '',
				owner_info_list: [],

				ph_device_sn: "设备的编码",
				ph_device_name: "设备的名称",
				ph_construction_worker: "",
				ph_install_location: "设备的安装位置",
				ph_device_address: "设备所在的地址",
				ph_owner_str: '请输入业主姓名',
				ph_owner_tel_str: '请输入业主电话',

				shouldDisableInputSn: false,
			}
		},
		onReady() {
			this.getLocation();
		},
		onLoad() {
			// 接收扫码的值
			uni.$on('scanResult', (data) => {
				this.device_sn = data.result;

				this.requestDeviceInfo();
			});
			
			if(option.installDeviceInfo !== undefined){
				let info = JSON.parse(option.installDeviceInfo);
				this.id = info.id;
				this.construction_createtime = info.construction_createtime;
				this.deviceStatus = info.deviceStatus;
				this.construction_image = info.construction_image;
				this.device_sn = info.device_sn;
				this.device_name = info.device_name;
				this.construction_worker = info.construction_worker;
				this.install_location = info.install_location;
				this.device_address = info.device_address;
				this.owner_info_list = info.owner_info_list;
				// this.owner_info_list = [{
				// 	"owner_name": "zysun",
				// 	"owner_tel": "1521918621"
				// }, {
				// 	"owner_name": "ssdun",
				// 	"owner_tel": "151918621"
				// }, {
				// 	"owner_name": "sun",
				// 	"owner_tel": "158621"
				// }];
				this.owner_str = this.owner_info_list.map(item => item.owner_name).toString();
				this.owner_tel_str = this.owner_info_list.map(item => item.owner_tel).toString();
			}
		},
		onUnload() {
			// 移除监听事件  
			uni.$off('scanResult');
		},
		methods: {
			// 扫码
			openScan() {
				uni.navigateTo({
					url: '../scan/scan'
				});
			},

			onEnterDeviceSn() {
				this.requestDeviceInfo();
			},

			successGetInfoCb(rsp) {
				if (rsp.data.error === 0) {
					let info = rsp.data.msg.device_info;
					this.id = info.id;
					this.construction_createtime = info.construction_createtime;
					this.deviceStatus = info.deviceStatus;
					this.construction_image = info.construction_image;
					this.device_sn = info.device_sn;
					this.device_name = info.device_name;
					this.construction_worker = info.construction_worker;
					this.install_location = info.install_location;
					this.device_address = info.device_address;
					this.owner_info_list = info.owner_info_list;

					this.shouldDisableInputSn = !this.isEmpty(this.device_sn);

					this.imgList.push(this.image);

				}
			},

			failGetInfoCb(err) {
				console.log('api_get_install_by_device_sn failed', err);
			},

			completeGetInfoCb(rsp) {},

			requestDeviceInfo() {
				let params = {
					device_sn: this.device_sn,
				};

				this.request(
					getApp().globalData.api_get_install_by_device_sn,
					params,
					this.successGetInfoCb,
					this.failGetInfoCb,
					this.completeGetInfoCb);
			},

			successCb(rsp) {
				console.log('success cb')
				if (rsp.data.error === 0) {
					// this.install_device_list = rsp.data.msg.install_device_list;
					uni.showToast({
						title: '添加成功'
					})
				}
			},
			failCb(err) {
				console.log('api_install_device failed', err);
			},
			completeCb(rsp) {
				if (rsp.data == undefined) {
					return;
				}
				if (rsp.data.error === 1) {
					if (rsp.data.msg.indexOf('doesn`t exist') != -1) {
						getApp().showToast('业主手机号不存在，\n 请核实后输入')
					} else {
						getApp().showToast('绑定失败，请重试或联系管理员')
					}
				}
			},

			onAddDevice() {

				let user_name = uni.getStorageSync('key_user_name');

				let params = {
					device_sn: this.device_sn,
					device_name: this.device_name,
					construction_worker: user_name,
					install_location: this.install_location,
					device_address: this.device_address,

				};

				this.requestWithMethod(
					getApp().globalData.api_install_device + this.owner_tel_str,
					"PUT",
					params,
					this.successCb,
					this.failCb,
					this.completeCb);
			},

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
					count: 1, //默认9
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
			async getLocation() {
				let status;
				// #ifdef APP-PLUS
				tatus = await this.checkPermission();
				if (status !== 1) {
					return;
				}
				// #endif
				// #ifdef MP-WEIXIN || MP-TOUTIAO || MP-QQ
				status = await this.getSetting();
				if (status === 2) {
					// this.showConfirm();
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
							// this.showConfirm();
						}
						// #endif
						// #ifndef MP-BAIDU
						if (err.errMsg.indexOf("auth deny") >= 0) {
							uni.showToast({
								title: "访问位置被拒绝",
								icon: 'none'
							})
						} else {
							uni.showToast({
								title: err.errMsg,
								icon: 'none'
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
