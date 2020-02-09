<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="false">
			<block slot="content">设备</block>
		</cu-custom>
		<view style="padding-bottom: 100upx;">
			<view class="cu-card">
				<view class="cu-item shadow shadow-lg shadow-blur bg-gradual-dark-purple2 text-black">
					<view class="padding cf">
						<image class="fl" style="width: 40upx;height: 40upx; margin-right: 15upx; margin-top: 10upx;" src="/static/home/user_home_device.png"> </image>
						<view class="fl text-white text-lg" style="margin-right: 12upx; margin-top: 8upx;">
							总设备数
						</view>
						<view class="fl text-white text-lg" style="margin-top: 12upx;">
							{{total_device_num}}
						</view>
						<view class="fr">
							<image @click="onClickAddDevice" style="width: 55upx;height: 55upx; margin-right: 15upx;" src="/static/home/add_device.png"></image>
							<image @click="onClickAddDanger" style="width: 55upx;height: 55upx;" src="/static/home/add_danger.png"></image>
						</view>
					</view>

					<view class="flex justify-center">
						<view class="centerStatus text-xl">正常</view>
					</view>

					<view class="flex" style="padding-bottom: 25upx;">

						<view class="flex-sub justify-center text-center solid-right line-white">
							<image class="device-icon" src="/static/home/normal.png"></image>
							<view class="text-light-green">
								正常
							</view>
							<view class="text-light-green">
								{{normal_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center solid-right line-white">
							<image class="device-icon" src="/static/home/offline.png"></image>
							<view class="text-gray">
								离线
							</view>
							<view class="text-gray">
								{{offline_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center solid-right line-white">
							<image class="device-icon" src="/static/home/alert2.png"></image>
							<view class="text-light-red">
								报警
							</view>
							<view class="text-light-red">
								{{alert_device_num}}
							</view>
						</view>

						<view class="flex-sub justify-center text-center line-white">
							<image class="device-icon" src="/static/home/break_down.png"></image>
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
			<view class="cu-card">
				<view class="solids text-black margin-bottom-sm" style="background-color: #FFFFFF; margin-top: -15upx;">
					<view class="cf" style="padding: 22upx;">
						<image class="fl" style="width: 42upx;height: 42upx; margin-right: 15upx; margin-top: 10upx; " src="/static/home/notice.png"></image>
						<view class="fl text-lg text-dark-orange" style="margin-right: 12upx; margin-top: 12upx;">
							<!-- <swiper vertical="true" autoplay="true" circular="true" interval="3000">
								<swiper-item v-for="(item, index) in msg" :key="index">
									<navigator class="text-black">{{item}}</navigator>
								</swiper-item>
							</swiper> -->
							test
						</view>
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 正常 -->
			<view class="cu-card">
				<view class="cu-item list-item">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
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
							<view class="flex align-start padding-sm">
								<image style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></image>
								<view class="cu-tag radius bg-gradual-green text-xs" style="margin-right: 10upx; padding: 8upx;">正常</view>
								<image style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></image>
								<view class="cu-tag radius line-black text-xs" style="padding: 3upx;">100%</view>
							</view>

							<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>

						</view>
					</view>
				</view>
			</view>

			<!-- 设备情况卡片 离线 -->
			<view class="cu-card">
				<view class="cu-item list-item" style="background-color: #DBD8D8;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
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
							<view class="flex align-start padding-sm">
								<image style="width: 30upx;height: 30upx; margin-right: 15upx; margin-top: 5upx;" src="/static/home/signal.png"></image>
								<view class="cu-tag radius bg-grey text-xs" style="margin-right: 10upx; padding: 8upx;">离线</view>
							</view>

							<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>

						</view>
					</view>
				</view>
			</view>
			
			<!-- 设备情况卡片 报警 -->
			<view class="cu-card">
				<view class="cu-item list-item" style="background-color: #FBE4DF;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
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
								<view class="cu-tag radius bg-dark-red text-xs" style="margin-right: 10upx; padding: 8upx;">报警</view>
								<image style="width: 55upx;height: 55upx; margin-right: 10upx;" src="/static/home/battery.png"></image>
								<view class="cu-tag radius line-black text-xs" style="padding: 3upx;">100%</view>
							</view>
			
							<image class="margin-left-xl" src="../../static/tabbar/device_normal.png" style="width: 150upx; height: 150upx;"></image>
			
						</view>
					</view>
				</view>
			</view>
			
			<!-- 设备情况卡片 故障 -->
			<view class="cu-card">
				<view class="cu-item list-item" style="background-color: #FBEFDF;">
					<view class="flex">
						<view class="flex-twice padding-sm" style="font-size: 26upx;">
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
				total_device_num: "0",
				normal_device_num: "0",
				breakdown_device_num: "0",
				alert_device_num: "0",
				offline_device_num: "0",

				msg: [
					'测试滚动消息1',
					'测试滚动消息2',
					'测试滚动消息3',
				]
			}
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
		background-color: #AAE604;
		padding-left: 44upx;
		padding-right: 44upx;
		padding-top: 52upx;
		padding-bottom: 52upx;
		color: #FFFFFF;
		font-weight: bold;
		margin-bottom: 30upx;
	}
</style>
