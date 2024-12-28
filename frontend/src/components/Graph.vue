<script setup lang="ts">
import { AreaChart } from '@/components/ui/chart-area'
const props = defineProps({
    data: { type: Array, required: true },
    colors: { type: Array, required: false },
})
</script>

<template>
    <AreaChart
        :data="data"
        index="time"
        :categories="['Voltage', 'Predicted Voltage']"
        :colors="colors"
    />
</template>
