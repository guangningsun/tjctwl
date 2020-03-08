<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="false">
			<block slot="content">设备</block>
		</cu-custom>
		<view style="padding-bottom: 100upx;">
			<view class="cu-card">
				<view class="cu-item shadow shadow-lg shadow-blur bg-gradual-dark-purple2 text-black">
					<view class="padding cf">
						<img class="fl" style="width: 40upx;height: 40upx; margin-right: 15upx; margin-top: 10upx;" src="/static/home/user_home_device.png">
						</img>
						<view class="fl text-white text-lg" style="margin-right: 12upx; margin-top: 8upx;">
							总设备数
						</view>
						<view class="fl text-white text-lg" style="margin-top: 12upx;">
							{{device_total_num}}
						</view>
						<view class="fr">
							<img @click="onClickAddDevice" style="width: 55upx;height: 55upx; margin-right: 15upx;" src="/static/home/add_device.png"></img>
							<img @click="onClickAddDanger" style="width: 55upx;height: 55upx;" src="/static/home/add_danger.png"></img>
						</view>
					</view>

					<view class="flex justify-center">
						<view class="centerStatus text-xl" :style="[{backgroundColor:currentSelectBgColor}]">{{current_device_list_name}}</view>
					</view>

					<view class="flex" style="padding-bottom: 25upx;">

						<view class="flex-sub justify-center text-center solid-right line-white" @tap="onSelectNormal">
							<img class="device-icon" src="/static/home/normal.png"></img>
							<view class="text-light-green">
								正常
							</view>
							<view class="text-light-green">
								{{normal_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center solid-right line-white" @tap="onSelectOffline">
							<img class="device-icon" src="/static/home/offline.png"></img>
							<view class="text-gray">
								离线
							</view>
							<view class="text-gray">
								{{offline_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center solid-right line-white" @tap="onSelectAlert">
							<img class="device-icon" src="/static/home/alert2.png"></img>
							<view class="text-light-red">
								报警
							</view>
							<view class="text-light-red">
								{{alert_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center line-white" @tap="onSelectBreakdown">
							<img class="device-icon" src="/static/home/break_down.png"></img>
							<view class="text-light-orange">
								故障
							</view>
							<view class="text-light-orange">
								{{breakdown_device_num}}
							</view>
						</view>
					</view>
				</view>
			</view>

			<!-- 通知条 -->
			<!-- <view class="cu-card">
				<view class="solids text-black margin-bottom-sm" style="background-color: #FFFFFF; margin-top: -15upx;">
					<view class="cf" style="padding: 22upx;">
						<img class="fl" style="width: 42upx;height: 42upx; margin-right: 15upx; margin-top: 10upx; " src="/static/home/notice.png"></img>
						<view class="fl text-lg text-dark-orange" style="margin-right: 12upx; margin-top: 12upx;">
							test
						</view>
					</view>
				</view>
			</view> -->

			<view v-show="shouldShowEmpty" class="flex justify-center margin-top-xl">
				<view style="background-color: #00000000;">
					<image src="../../static/empty.png" mode="aspectFit" style="width: 200upx; height: 200upx;"></image>
					<view class="text-df text-gray text-center">
						无相关设备
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 正常 -->
			<view class="cu-card" v-show="shouldShowNormal" v-for="(item,index) in normal_device_list" :key="index" @tap="goToDeviceDetail(item)">
				<view class="cu-item list-item solid" style="background-color: #ebf5db; margin-top: 1upx;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备编码:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.code}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备名称:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.name}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备型号:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.model}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									地址:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.address}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									安装位置:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.location}}
								</view>
							</view>
						</view>
						<view class="flex-sub">
							<view class="flex align-center padding-sm">
								<img style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></img>
								<view class="cu-tag radius bg-gradual-green text-xs" style="margin-right: 10upx; padding: 8upx;">{{item.signal}}</view>
								<img style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></img>
								<view class="cu-tag radius line-black text-xs text-bold" style="padding: 3upx;">{{item.battery}}</view>
							</view>

							<img class="margin-left-xl" :src="item.image" :onerror="default_img" style="width: 150upx; height: 150upx;"></img>
						</view>
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 离线 -->
			<view class="cu-card" v-show="shouldShowOffline" v-for="(item,index) in offline_device_list" :key="index">
				<view class="cu-item list-item solid" style="background-color: #DBD8D8; margin-top: 1upx;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备编码:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.code}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备名称:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.name}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备型号:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.model}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									地址:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.address}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									安装位置:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.location}}
								</view>
							</view>
						</view>
						<view class="flex-sub">
							<view class="flex align-center justify-end padding-sm">
								<img style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></img>
								<view class="cu-tag radius bg-grey text-xs" style="margin-right: 10upx; padding: 8upx;">{{item.signal}}</view>
							</view>
							<img class="margin-left-xl margin-right-xl" :src="item.image" :onerror="default_img" style="width: 150upx; height: 150upx;"></img>
						</view>
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 报警 -->
			<view class="cu-card" v-show="shouldShowAlert" v-for="(item,index) in alert_device_list" :key="index">
				<view class="cu-item list-item solid" style="background-color: #FBE4DF;margin-top: 1upx;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备编码:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.code}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备名称:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.name}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备型号:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.model}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									地址:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.address}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									安装位置:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.location}}
								</view>
							</view>
						</view>
						<view class="flex-sub">
							<view class="flex align-center padding-sm">
								<image style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></image>
								<view class="cu-tag radius bg-dark-red text-xs" style="margin-right: 10upx; padding: 8upx;">{{item.signal}}</view>
								<image style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></image>
								<view class="cu-tag radius line-black text-xs text-bold" style="padding: 3upx;">{{item.battery}}</view>
							</view>

							<img class="margin-left-xl margin-right-xl" :src="item.image" :onerror="default_img" style="width: 150upx; height: 150upx;"></img>

						</view>
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 故障 -->
			<view class="cu-card" v-show="shouldShowBreakdown" v-for="(item,index) in breakdown_device_list" :key="index">
				<view class="cu-item list-item solid" style="background-color: #FBEFDF;margin-top: 1upx;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备编码:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.code}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备名称:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.name}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									设备型号:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.model}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									地址:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.address}}
								</view>
							</view>
							<view class="flex align-center">
								<view class="text-right text-black margin-top-sm" style="width: 120upx;font-weight: bold; margin-right: 5upx;">
									安装位置:
								</view>
								<view class="text-black margin-top-sm text-cut" style="width: 250upx;">
									{{item.location}}
								</view>
							</view>
						</view>
						<view class="flex-sub">
							<view class="flex align-center padding-sm">
								<image style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></image>
								<view class="cu-tag radius bg-orange2 text-xs" style="margin-right: 10upx; padding: 8upx;">{{item.signal}}</view>
								<image style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></image>
								<view class="cu-tag radius line-black text-xs text-bold" style="padding: 3upx;">{{item.battery}}</view>
							</view>

							<img class="margin-left-xl margin-right-xl" :src="item.image" :onerror="default_img" style="width: 150upx; height: 150upx;"></img>

						</view>
					</view>
				</view>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar bg-white">
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_activate.png"></image>
					</view>
					<view class="text-light-purple">设备</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_event/user_event'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_normal.png"></image>
					</view>
					<view class="text-black">事件</view>
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
				shouldShowNormal: true,
				shouldShowOffline: false,
				shouldShowAlert: false,
				shouldShowBreakdown: false,
				shouldShowEmpty: false,

				device_total_num: "0",
				normal_device_num: "0",
				breakdown_device_num: "0",
				alert_device_num: "0",
				offline_device_num: "0",

				current_device_list_name: '正常',
				currentSelectBgColor: '#AAE604',

				normal_device_list: [],
				offline_device_list: [],
				alert_device_list: [],
				breakdown_device_list: [],

				// normal_device_list: [{
				// 	"code": "",
				// 	"name": "test122",
				// 	"model": "-",
				// 	"address": "-",
				// 	"location": "-",
				// 	"signal": "-",
				// 	"battery": "",
				// 	"image": "-"
				// }],

				msg: [
					'测试滚动消息1',
					'测试滚动消息2',
					'测试滚动消息3',
				],

				default_img: 'this.src="' + require('../../static/default_device_img.png') + '"',
			}
		},
		onLoad: function(options) {

		},
		onShow() {
			let user_id = getApp().globalData.user_id;
			if (this.isEmpty(user_id)) {
				user_id = uni.getStorageSync('key_user_id');
			}
			let params = {
				username: this.user_name,
				password: this.user_pwd,
				user_id: user_id
			};
			this.request(
				getApp().globalData.api_get_user_index,
				params,
				this.successCallback,
				this.failCallback,
				this.completeCallback);
		},
		methods: {
			onClickAddDevice() {
				uni.navigateTo({
					url: 'user_add_device'
				});
			},
			onClickAddDanger() {
				uni.navigateTo({
					url: 'user_add_danger'
				});
			},

			successCallback(rsp) {
				console.log(rsp);
				let rspData = rsp.data.msg;
				if (rsp.data.error === 1) {
					if (rspData.indexOf("no device") != -1) {
						this.device_total_num = 0;
						this.normal_device_num = 0;
						this.breakdown_device_num = 0;
						this.alert_device_num = 0;
						this.offline_device_num = 0;
						this.normal_device_list = [];
						this.offline_device_list = [];
						this.alert_device_list = [];
						this.breakdown_device_list = [];
					}

				} else if (rsp.data.error === 0) {
					this.device_total_num = rspData.device_total_num;
					this.normal_device_num = rspData.normal_device_num;
					this.breakdown_device_num = rspData.breakdown_device_num;
					this.alert_device_num = rspData.alert_device_num;
					this.offline_device_num = rspData.offline_device_num;
					this.normal_device_list = rspData.normal_device_list;
					this.offline_device_list = rspData.offline_device_list;
					this.alert_device_list = rspData.alert_device_list;
					this.breakdown_device_list = rspData.breakdown_device_list;
				}

				this.showEmpty();

				uni.setStorage({
					key: 'key_user_normal_device_list',
					data: rspData.normal_device_list,
				});
				uni.setStorage({
					key: 'key_user_offline_device_list',
					data: rspData.offline_device_list,
				});
				uni.setStorage({
					key: 'key_user_alert_device_list',
					data: rspData.alert_device_list,
				});
				uni.setStorage({
					key: 'key_user_breakdown_device_list',
					data: rspData.breakdown_device_list,
				});

			},
			failCallback(err) {
				console.log('api_get_user_index failed', err);
			},
			completeCallback(rsp) {},

			onSelectNormal() {
				this.current_device_list_name = '正常';
				this.currentSelectBgColor = '#AAE604';

				this.shouldShowNormal = true;
				this.shouldShowOffline = false;
				this.shouldShowAlert = false;
				this.shouldShowBreakdown = false;

				this.shouldShowEmpty = this.normal_device_list.length === 0;
			},
			showEmpty() {
				if (this.current_device_list_name === '正常') {
					if (this.normal_device_list.length === 0) {
						this.shouldShowEmpty = true;
					} else {
						this.shouldShowEmpty = false;
					}
				}

				if (this.current_device_list_name === '离线') {
					if (this.offline_device_list.length === 0) {
						this.shouldShowEmpty = true;
					} else {
						this.shouldShowEmpty = false;
					}
				}

				if (this.current_device_list_name === '报警') {
					if (this.alert_device_list.length === 0) {
						this.shouldShowEmpty = true;
					} else {
						this.shouldShowEmpty = false;
					}
				}

				if (this.current_device_list_name === '故障') {
					if (this.breakdown_device_list.length === 0) {
						this.shouldShowEmpty = true;
					} else {
						this.shouldShowEmpty = false;
					}
				}
			},
			onSelectOffline() {
				this.current_device_list_name = '离线';
				this.currentSelectBgColor = '#939393';

				this.shouldShowNormal = false;
				this.shouldShowOffline = true;
				this.shouldShowAlert = false;
				this.shouldShowBreakdown = false;

				this.shouldShowEmpty = this.offline_device_list.length === 0;
			},
			onSelectAlert() {
				this.current_device_list_name = '报警';
				this.currentSelectBgColor = '#FF6B6B';

				this.shouldShowNormal = false;
				this.shouldShowOffline = false;
				this.shouldShowAlert = true;
				this.shouldShowBreakdown = false;

				this.shouldShowEmpty = this.alert_device_list.length === 0;
			},
			onSelectBreakdown() {
				this.current_device_list_name = '故障';
				this.currentSelectBgColor = '#F9A043';

				this.shouldShowNormal = false;
				this.shouldShowOffline = false;
				this.shouldShowAlert = false;
				this.shouldShowBreakdown = true;

				this.shouldShowEmpty = this.breakdown_device_list.length === 0;
			},
			show_default_image: function(event) {
				event.target.src = "https://ossweb-img.qq.com/images/lol/web201310/skin/big10001.jpg";
			},
			goToDeviceDetail(item) {
				console.log('send:' + JSON.stringify(item));
				uni.navigateTo({
					url: 'user_device_detail?deviceInfo=' + encodeURIComponent(JSON.stringify(item))
					// url: 'pages/user_home/user_device_detail?deviceInfo='+ encodeURIComponent(JSON.stringify(item))
				})
			}
		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	}

	.list-item {
		background-color: #f7ffed;
		margin-top: -10upx;
	}

	.scroll-Y {
		height: 300upx;
	}

	.scroll-view-item {
		height: 300upx;
		line-height: 300upx;
		text-align: center;
		font-size: 36upx;
	}

	.device-icon {
		width: 45upx;
		height: 45upx;
	}

	.centerStatus {
		border-radius: 1600upx;
		padding-left: 44upx;
		padding-right: 44upx;
		padding-top: 52upx;
		padding-bottom: 52upx;
		color: #FFFFFF;
		font-weight: bold;
		margin-bottom: 30upx;
	}
</style>
