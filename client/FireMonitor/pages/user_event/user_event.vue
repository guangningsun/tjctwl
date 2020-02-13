<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
			<!-- <view class="cu-bar bg-gradual-dark-purple" style="z-index: 9999;"> -->
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					事件
				</view>
			</view>
		</view>

		<view class="box" >
			<view class="cu-bar bg-gradual-dark-purple search">
				<view class="search-form radius">
					<text class="cuIcon-search"></text>
					<input @focus="InputFocus" @blur="InputBlur" :adjust-position="false" type="text" placeholder="搜索事件" confirm-type="search"></input>
				</view>
				<view class="action" @tap="showModal" data-target="DrawerModalR">
					<text class="cuIcon-calendar"></text>
				</view>
			</view>
		</view>

		<view class="cu-list margin-top bg-white">
			<view class="cu-item flex solid-bottom">
				<view class="flex align-center margin">
					<image src="../../static/event/upload.png" style="width: 80upx; height: 80upx;"></image>
				</view>
				<view class="flex align-center justify-between" style="width: 100%;">
					<view class="margin-top-sm margin-bottom-sm">
						<view class="title">
							上报电池电压
						</view>
						<view class="text-gray text-df">
							安装位置：办公室
						</view>
					</view>
					<view class="margin-sm">
						<view class="text-grey text-sm">2020-02-01 10:00</view>
						<view class="flex justify-end">
							<view class="cu-tag round bg-red sm margin-sm"></view>
						</view>
					</view>
				</view>
			</view>

			<view class="cu-item flex solid-bottom">
				<view class="flex align-center margin">
					<image src="../../static/event/heartbeat.png" style="width: 80upx; height: 80upx;"></image>
				</view>
				<view class="flex align-center justify-between" style="width: 100%;">
					<view class="margin-top-sm margin-bottom-sm">
						<view class="title">
							心跳
						</view>
						<view class="text-gray text-df">
							安装位置：走廊
						</view>
					</view>
					<view class="margin-sm">
						<view class="text-grey text-sm">2020-02-01 10:00</view>
						<view class="flex justify-end">
							<view class="cu-tag round bg-red sm margin-sm"></view>
						</view>
					</view>
				</view>
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
				<navigator hover-class="none" class="action" >
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_activate.png"></image>
					</view>
					<view class="text-light-purple">事件</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_me/user_me'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/me-normal.png"></image>
					</view>
					<view class="text-black">我的</view>
				</navigator>
			</view>
		</view>

		<!-- 右侧model -->
		<view class="cu-modal drawer-modal justify-end" :class="modalName=='DrawerModalR'?'show':''" @tap="hideModal">
			<view class="cu-dialog basis-lg" @tap.stop="" :style="[{top:CustomBar+'px',height:'calc(100vh - ' + CustomBar + 'px)'}]">
				<view class="cu-list menu" :class="[menuBorder?'sm-border':'',menuCard?'card-menu margin-top':'']">
					<view class="cu-item" :class="menuArrow?'arrow':''">
						<button class="cu-btn content" open-type="contact" @tap="onStartDate">
							<text class="cuIcon-btn text-olive"></text>
							<text class="text-black">起始日期</text>
						</button>
						<picker mode="date" :value="startDate" start="2015-09-01" end="2020-09-01" @change="startDateChange" @tap="hideModal">
							<view class="flex align-center justify-end">
								<view class="picker">
									{{startDate}}
								</view>
								<text class="cuIcon-right text-gray"></text>
							</view>
						</picker>

					</view>
					<view class="cu-item" :class="menuArrow?'arrow':''" @tap="onEndDate">
						<button class="cu-btn content" open-type="contact">
							<text class="cuIcon-btn text-light-orange"></text>
							<text class="text-black">结束日期</text>
						</button>
						<picker mode="date" :value="endDate" start="2015-09-01" end="2020-09-01" @change="endDateChange" @tap="hideModal">
							<view class="flex align-center justify-end">
								<view class="picker">
									{{endDate}}
								</view>
								<text class="cuIcon-right text-gray"></text>
							</view>
						</picker>
					</view>
				</view>

				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @click="onDateSearch">查询</button>
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
				startDate: '2020-02-01',
				endDate: '2020-02-01',
			}
		},
		computed: {
			style() {
				var StatusBar = this.StatusBar;
				var CustomBar = this.CustomBar;
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
			startDateChange(e) {
				this.startDate = e.detail.value;
				e.currentTarget.dataset.target = 'DrawerModalR';
				this.showModal(e);
			},
			endDateChange(e) {
				this.endDate = e.detail.value;
				e.currentTarget.dataset.target = 'DrawerModalR';
				this.showModal(e);
			},
			onDateSearch() {
				
			}

		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	}
</style>
