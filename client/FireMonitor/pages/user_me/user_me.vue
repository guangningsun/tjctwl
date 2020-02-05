<template>
	<view>
		<view class="cu-card margin-top-xl">
			<view class="flex align-center cu-item bg-gradual-dark-purple2">

				<view class="flex solid-bottom padding justify-between">
					<view class="padding-sm margin-xs radius">
						<view class="flex align-center margin-right">
							<view class="cu-avatar xl round" style="background-image:url(../../static/me/head3.png);"></view>
							<view class="text-white text-lg margin-left-sm">
								<view class="margin-bottom-xs">昵称XX</view>
								<view class="margin-bottom-xs">18638492948</view>
							</view>
						</view>
					</view>
					<view class="padding-sm margin-xs radius margin-top-xl">
						<text class="cuIcon-right text-white"></text>
					</view>
				</view>
			</view>
		</view>

		<view class="cu-card">
			<view class="cu-item">
				<view class="cu-form-group">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/add_device_me.png" style="width: 60upx;height: 60upx;"></image>
						<text class="text-lg">添加设备</text>
					</view>
					<text class="cuIcon-right text-gray"></text>
				</view>

				<view class="cu-form-group">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/tel_me.png" style="width: 47upx;height: 47upx;"></image>
						<text class="text-lg">火警电话通知</text>
					</view>
					<text class="cuIcon-right text-gray"></text>
				</view>

				<view class="cu-form-group" open-type="contact" @tap="showModal" data-target="ClearCache">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/clear_me.png" style="width: 50upx;height: 50upx;"></image>
						<text class="text-lg">清除内存</text>
					</view>
					<text class="cuIcon-right text-gray"></text>
				</view>

				<view class="cu-form-group">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/version_me.png" style="width: 50upx;height: 50upx;"></image>
						<text class="text-lg">版本信息</text>
					</view>
					<text class="cuIcon-right text-gray"></text>
				</view>

				<view class="cu-form-group">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/contact_me.png" style="width: 50upx;height: 50upx;"></image>
						<text class="text-lg">联系我们</text>
					</view>
					<text class="cuIcon-right text-gray"></text>
				</view>


			</view>

		</view>

		<view class="justify-between bottom-box">
			<view class="padding flex flex-direction">
				<button class="cu-btn bg-dark-purple lg" @click="onLogout">退出登录</button>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar bg-white">
				<navigator hover-class="none" :url="'../user_home/user_home'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_normal.png"></image>
					</view>
					<view class="text-black">设备</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_event/user_event'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_normal.png"></image>
					</view>
					<view class="text-black">事件</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_me/user_me'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/me-activate.png"></image>
					</view>
					<view class="text-light-purple">我的</view>
				</navigator>
			</view>
		</view>

		<!-- 删除modal -->
		<view class="cu-modal" :class="modalName=='ClearCache'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">清除内存</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
				<view class="padding-xl">
					是否清除内存？
				</view>
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmClear">确定</button>

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
			onLogout() {

			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			onConfirmClear(){
				
			}
		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	}
</style>
