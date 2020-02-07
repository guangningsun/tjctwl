<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">关于我们</block>
		</cu-custom>

		<view class="cu-card margin-top-xl">
			<view class="cu-item shadow shadow-lg shadow-blur bg-white text-black padding">
				<view class="flex justify-between">
					<view class="radius">
						<view class="text-gl">XXXX公司</view>
						<view class="text-sm margin-top-sm">XXXX Co., LTD.</view>
					</view>
					<view class="radius">
						<image src="../../static/logo.png" style="width: 100upx; height: 100upx;"></image>
					</view>
				</view>
				<view>
					<view class="padding-top-sm">地址：XXXXX</view>
					<view class="padding-top-sm">电话：XXXXX</view>
					<view class="padding-top-sm">网站：XXXXX</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
