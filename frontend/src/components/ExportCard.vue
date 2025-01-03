<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { ref, onUpdated, onMounted, watch, nextTick } from 'vue'
import { Download, LucideX } from 'lucide-vue-next'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
} from '@/components/ui/select'
import CardDescription from './ui/card/CardDescription.vue'
import Prism from 'prismjs'
import 'prismjs/themes/prism-funky.css'
import 'prismjs/components/prism-json'
import 'prismjs/components/prism-csv'
import 'prismjs/components/prism-xml-doc'
const emits = defineEmits(['export-data', 'close-export', 'update-filetype'])
const props = defineProps({
    filetype: {
        type: String,
        required: true,
    },
})
const data = ref(props.filetype)
function completeDataExport() {
    emits('export-data')
    emits('close-export')
}
watch(data, (newValue) => {
    console.log('Selected format:', newValue)
    emits('update-filetype', newValue)
    nextTick(() => {
        Prism.highlightAll()
    })
})
onMounted(() => {
    watch(data, () => {
        nextTick(() => {
            Prism.highlightAll()
        })
    })
})
</script>

<template>
    <div
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
    >
        <Card
            class="border border-gray-200 shadow-2xl bg-black p-8 flex flex-col items-center gap-6 rounded-lg w-2/3"
        >
            <CardContent class="w-full">
                <div class="flex w-full">
                    <Button @click="completeDataExport" class="text-black">
                        <Download class="h-6 w-6" /> Export
                    </Button>
                    <!-- Add 'ml-auto' to right-align this button -->
                    <Button class="ml-auto" @click="emits('close-export')">
                        <LucideX class="h-6 w-6" />
                    </Button>
                </div>
                <Card>
                    <CardDescription>
                        Raw Data Export Example Preview ({{ data }})
                    </CardDescription>
                    <div v-if="data === 'json'">
                        <pre>
    <code class="language-json">
    {
        {
        "time": '1',
        "Predicted Voltage": 9.33453,
        "Voltage": 9.23434,
        },
        {
        "time": '2',
        "Predicted Voltage": 9.11111,
        "Voltage": 9.21134,
        },
        {
        "time": '3',
        "Predicted Voltage": 8.94301,
        "Voltage": 9.14032,
        },
        {
        "time": '4',
        "Predicted Voltage": 8.93883,
        "Voltage": 8.93433,
        },
    }
    </code></pre>
                    </div>
                    <div v-else-if="data === 'csv'">
                        <pre>
    <code class="language-csv">
    Time, Predicted Voltage, Voltage
    1, 9.33453, 9.23434
    2, 9.11111, 9.21134
    3, 8.94301, 9.14032
    4, 8.93883, 8.93433
    </code></pre>
                    </div>
                    <div v-else-if="data === 'xml'">
                        <pre>
    <code class="language-XML">
        {{ 
        `
    <S T="1" V="13.092" C="40" Tp="999.9" />
    <S T="2" V="12.619" C="40" Tp="999.9" />
    <S T="3" V="12.329" C="40" Tp="999.9" />
    <S T="4" V="12.25" C="40" Tp="999.9" />
    <S T="5" V="12.192" C="40" Tp="999.9" />
        `}}
    </code></pre>
                    </div>
                </Card>
                <div class="mt-3" />
                Export Data Type:
                <Select v-model="data" class="w-full">
                    <SelectTrigger class="w-[240px]">
                        <SelectValue placeholder="Select a Export File Type" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectGroup>
                            <SelectLabel>Export files</SelectLabel>
                            <SelectItem value="json"> JSON </SelectItem>
                            <SelectItem value="csv"> CSV </SelectItem>
                            <SelectLabel
                                >Backwards Compatible Formats</SelectLabel
                            >
                            <SelectItem value="xml" disabled>
                                XML/BT2 (Not Available)
                            </SelectItem>
                            
                        </SelectGroup>
                    </SelectContent>
                </Select>
            </CardContent>
        </Card>
    </div>
</template>
<style lang="css" scoped>
a {
    all: unset;
}
</style>