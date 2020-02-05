<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">版本信息</block>
		</cu-custom>

		<view class="cu-card margin-top-xl">
			<view class="cu-item shadow shadow-lg shadow-blur bg-white text-black padding">
				<view class="flex justify-center margin-top margin-bottom">
					<image src="../../static/logo.png" style="width: 100upx; height: 100upx;"></image>
				</view>
				<view class="flex justify-center margin-top margin-bottom">
					XXXX
				</view>
				<view class="flex justify-center">
					V1.0.0
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
