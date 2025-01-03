<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { LucideX } from 'lucide-vue-next'
import { ScrollArea } from '@/components/ui/scroll-area'
import {
    Table,
    TableBody,
    TableCell,
    TableCaption,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'
const props = defineProps({
    data: { type: Array, required: true },
})
const emits = defineEmits(['close'])

</script>

<template>
    <div
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
    >
        \
        <Card
            class="border border-gray-200 shadow-2xl bg-black p-8 flex flex-col items-center gap-6 rounded-lg w-2/3"
        >
            <CardContent class="w-full">
                <div class="flex w-full">
                    <Button class="ml-auto" @click="emits('close')">
                        <LucideX class="h-6 w-6" />
                    </Button>
                </div>
                <ScrollArea class="border h-72">
                <Table>
                    <TableCaption>Current Raw Graphing Data Results.</TableCaption>
                    <TableHeader>
                        <TableRow>
                            <TableHead class="w-[100px]">
                                Time (Seconds)
                            </TableHead>
                            <TableHead class="text-center">
                                Voltage (V)
                            </TableHead>
                            <TableHead class="text-right">
                                Predicted_Voltage (V)
                            </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="i in data" :key="i.time">
                            <TableCell class="font-medium text-white">
                                {{ i.time }}
                            </TableCell>
                            <TableCell class="text-center">
                                {{ i.Voltage }}
                            </TableCell>
                            <TableCell class="text-right">
                                {{ i["Predicted Voltage"] }}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </ScrollArea>
            </CardContent>
        </Card>
    </div>
</template>
