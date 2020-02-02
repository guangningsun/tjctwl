<template>
	<view>

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
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
    .mytabbar{
        z-index: 9999;
    }
</style>
