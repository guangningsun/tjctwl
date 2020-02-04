<template>
	<view>
		<view class="box">
			<view class="cu-bar bg-gradual-dark-purple" style="z-index: 9999;">
				<view class="round"></view>
				<view class="content">
					设备详情
				</view>
				<view class="action">
					<text class="cuIcon-more" @tap="showModal" data-target="DrawerModalR"></text>
				</view>
			</view>
		</view>

		<view class="cu-card">
			<view class="cu-item">
				<view class="bg-white">
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
				</view>

				<view class="flex cu-form-group">
					<view class="title">设备编码</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">设备类型</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">IMEI</view>
					<view>0</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">ICCID</view>
					<view>0</view>
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
					<view class="title">场所名</view>
					<view>0</view>
				</view>

			</view>
		</view>

		<view class="justify-between bottom-box">
			<view class="padding flex flex-direction">
				<button class="cu-btn bg-dark-purple lg" @click="onModifyDevice">修改信息</button>
			</view>
		</view>

		<!-- 右侧model -->
		<view class="cu-modal drawer-modal justify-end" :class="modalName=='DrawerModalR'?'show':''" @tap="hideModal">
			<view class="cu-dialog basis-lg" @tap.stop="" :style="[{top:CustomBar+'px',height:'calc(100vh - ' + CustomBar + 'px)'}]">
				<view class="cu-list menu" :class="[menuBorder?'sm-border':'',menuCard?'card-menu margin-top':'']">
					<view class="cu-item" :class="menuArrow?'arrow':''">
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-deletefill text-red"></text>
							<text class="text-black">删除设备</text>
						</button>
					</view>
					<view class="cu-item" :class="menuArrow?'arrow':''">
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-down text-olive"></text>
							<text class="text-black">下载二维码</text>
						</button>
					</view>
					<view class="cu-item" :class="menuArrow?'arrow':''">
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-share text-light-orange"></text>
							<text class="text-black">分享</text>
						</button>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				modalName: null,
			}
		},
		methods: {
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			onModifyDevice() {

			}
		}
	}
</script>

<style>

</style>
