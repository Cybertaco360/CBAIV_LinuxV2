<template>
    <div
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
    >
        <Card
            class="border border-gray-200 shadow-2xl bg-black p-8 flex flex-col items-center gap-6 rounded-lg w-2/3"
        >
            <div class="flex w-full">
                <Button
                    class="ml-0"
                    @click="handleCloseConfirmation"
                    variant="outline"
                >
                    <LucideX class="h-6 w-6" />
                </Button>
            </div>
            <CardContent>
                <div class="flex items-center justify-between">
                    <h2 class="text-xl font-semibold">Test Confirmation</h2>
                </div>
                <p class="text-gray-600 mt-2 mb-2">
                    Are you sure you want to start the test? Current
                    configuration below:
                </p>
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead class="w-[100px]"> Key </TableHead>
                            <TableHead class="text-right"> Value </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="(value, key) in configuration">
                            <TableCell class="font-medium text-white">
                                {{ key }}
                            </TableCell>
                            <TableCell class="text-right text-white">
                                {{ value }}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
                <div class="flex w-full justify-center">
                    <Button @click="handleStartTest" variant="outline"
                        ><p class="glow">Start Test</p></Button
                    >
                </div>
            </CardContent>
        </Card>
    </div>
</template>
<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { LucideX } from 'lucide-vue-next'
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'
const emits = defineEmits(['start-test', 'close-confirmation'])
function handleCloseConfirmation() {
    emits('close-confirmation')
}
function handleStartTest() {
    emits('close-confirmation')
    emits('start-test')
}
const props = defineProps({
    configuration: Object,
})
</script>
<style lang="css">
.glow {
    color: #ffffff;
    text-shadow:
        0 0 10px #ffffff,
        0 0 20px #e9e9e9,
        0 0 30px #999999;
    white-space: nowrap;
    z-index: 1;
}
</style>
