<template>
    <Card class="border-8">
        <CardContent>
            <div class="flex justify-center">
                <div class="grid grid-cols-6 gap-4 items-center w-max">
                    <div v-for="value in colors" class="flex">
                        <button @click="emits('colorOneUpdate', value)">
                            <div
                                class="w-5 h-5 rounded border-2 border-gray-500 ml-auto mr-auto"
                                :style="{ backgroundColor: value }"
                            ></div>
                            <div class="text-sm">{{ value }}</div>
                        </button>
                    </div>
                </div>
                <div class="flex ml-auto mr-auto">
                    <div class="text-xl text-gray-500 ml-auto ml-32">
                        Goldygo Yany's Legendary Super Palette
                    </div>
                </div>
                <div class="grid grid-cols-6 gap-4 items-center w-max ml-auto">
                    <div v-for="value in colors" class="flex">
                        <button @click="emits('colorTwoUpdate', value)">
                            <div
                                class="w-5 h-5 rounded border-2 border-gray-500 ml-auto mr-auto"
                                :style="{ backgroundColor: value }"
                            ></div>
                            <div class="text-sm">{{ value }}</div>
                        </button>
                    </div>
                </div>
            </div>
        </CardContent>
    </Card>
</template>
<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { ref, defineEmits } from 'vue'
const emits = defineEmits(['colorOneUpdate', 'colorTwoUpdate'])

const colors = ref([
    '#000000',
    '#FFFFFF',
    '#FF0000',
    '#00FF00',
    '#0000FF',
    '#FFFF00',
    '#FF00FF',
    '#00FFFF',
    '#C0C0C0',
    '#808080',
    '#800000',
    '#808000',
    '#008000',
    '#800080',
    '#008080',
    '#000080',
    '#FFA500',
    '#A52A2A',
    '#8B0000',
    '#FFD700',
    '#4B0082',
    '#7CFC00',
    '#DC143C',
    '#00BFFF',
    '#FF1493',
    '#2E8B57',
    '#ADFF2F',
    '#5F9EA0',
    '#4682B4',
    '#6A5ACD',
])
</script>
