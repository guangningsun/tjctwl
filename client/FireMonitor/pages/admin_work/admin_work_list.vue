<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					施工安装
				</view>
				<view class="action">
					<text class="cuIcon-add lg margin-right-sm" @tap="gotoInstall"></text>
					<text class="cuIcon-filter lg" @tap="showModal" data-target="FilterModal"></text>
				</view>
			</view>
		</view>

		<view class="cu-card card-margin">
			<view class="cu-item">
				<view class="flex justify-between">
					<view class="cu-tag radius bg-olive">已完成</view>
					<view class="flex align-center text-left margin-left-xl text-gray" style="width: 100%;">2020-02-02 10:00</view>
					<view class="cu-tag radius bg-green">正常</view>
				</view>
				<view class="flex">
					<image class="margin" src="../../static/tabbar/device_activate.png" style="width: 100upx; height: 100upx;"></image>
					<view class="margin-top-sm">
						<view>设备编码: AND19493</view>
						<view>设 备 名: xx设备</view>
						<view>施工人员: 李四</view>
					</view>
				</view>
				<view class="flex justify-end">
					<button class="cu-btn line-blue margin-right-xs margin-bottom-sm">详情</button>
					<button class="cu-btn line-orange margin-bottom-sm margin-right-xs">重装</button>
				</view>
			</view>
		</view>
		
		<!-- 过滤 modal -->
		<view class="cu-modal" :class="modalName=='FilterModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">条件筛选</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
		
				<form>
					<view class="cu-form-group">
						<view class="title">设备编码</view>
						<input class="text-left" placeholder="输入设备编码" name="input"></input>
					</view>
				</form>
		
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmSearch">查询</button>
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
			BackPage() {
				uni.navigateBack({
					delta: 1
				});
			},
			onConfirmSearch(){
				
			}
		}
	}
</script>

<style>

</style>
