<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
			<!-- <view class="cu-bar bg-gradual-dark-purple" style="z-index: 9999;"> -->
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
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
						<button class="cu-btn content" open-type="contact" @tap="showModal" data-target="DeleteModal">
							<text class="cuIcon-deletefill text-red"></text>
							<text class="text-black">删除设备</text>
						</button>
					</view>
					<view class="cu-item" :class="menuArrow?'arrow':''" @tap="onDownloadQrCode">
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-down text-olive"></text>
							<text class="text-black">下载二维码</text>
						</button>
					</view>
					<view class="cu-item" :class="menuArrow?'arrow':''" >
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-share text-light-orange"></text>
							<text class="text-black">分享</text>
						</button>
					</view>
				</view>
			</view>
		</view>

		<!-- 删除modal -->
		<view class="cu-modal" :class="modalName=='DeleteModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">删除设备</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
				<view class="padding-xl">
					是否删除当前设备？
				</view>
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmDelete">确定</button>

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
				StatusBar: this.StatusBar,
				CustomBar: this.CustomBar,
				modalName: null,
			}
		},
		computed: {
			style() {
				var StatusBar= this.StatusBar;
				var CustomBar= this.CustomBar;
				var bgImage = this.bgImage;
				var style = `height:${CustomBar}px;padding-top:${StatusBar}px;`;
				if (this.bgImage) {
					style = `${style}background-image:url(${bgImage});`;
				}
				return style
			}
		},
		methods: {
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			onModifyDevice(e) {

			},
			BackPage() {
				uni.navigateBack({
					delta: 1
				});
			},
			onConfirmDelete(e) {

			},
			onDownloadQrCode(e) {
				this.hideModal(e);
				plus.gallery.save('../../static/tabbar/device_normal.png', function() {
					uni.showToast({
						title: '保存成功',
						icon: 'none'
					});
				}, function() {
					uni.showToast({
						title: '保存失败，请重试！',
						icon: 'none'
					});
				});
			},
			
			// #ifdef APP-PLUS
			onShare(e) {
				if (this.providerList.length === 0) {
					uni.showModal({
						title: '当前环境无分享渠道!',
						showCancel: false
					});
					return;
				}
				let itemList = this.providerList.map(function(value) {
					return value.name;
				})
				uni.showActionSheet({
					itemList: itemList,
					success: (res) => {
						let provider = this.providerList[res.tapIndex].id;
						uni.share({
							provider: provider,
							scene: this.providerList[res.tapIndex].type && this.providerList[res.tapIndex].type === 'WXSenceTimeline' ?
								'WXSenceTimeline' : "WXSceneSession",
							type: (provider === "qq") ? 1 : 0,
							title: '欢迎体验uni-app',
							summary: 'uni-app 是一个使用 Vue.js 开发跨平台应用的前端框架',
							imageUrl: 'https://img-cdn-qiniu.dcloud.net.cn/uploads/nav_menu/8.jpg',
							href: "https://m3w.cn/uniapp",
							success: (res) => {
								console.log("success:" + JSON.stringify(res));
							},
							fail: (e) => {
								uni.showModal({
									content: e.errMsg,
									showCancel: false
								})
							}
						});
					}
				})
			}
			// #endif
		}
	}
</script>

<style>

</style>
