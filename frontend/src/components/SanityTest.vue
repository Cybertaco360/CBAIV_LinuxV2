<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { Skeleton } from '@/components/ui/skeleton'
import { Button } from '@/components/ui/button'
import { ref } from 'vue'
import { Zap, LucideX } from 'lucide-vue-next'
import {
    Table,
    TableBody,
    TableCell,
    TableCaption,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'

const data = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchData = async () => {
    data.value = null
    loading.value = true
    error.value = null
    try {
        const response = await fetch('http://127.0.0.1:5000/api/sanity_test')
        const result = await response.json()
        if (response.ok) {
            data.value = result
            error.value = false
        } else {
            data.value = [{ Time: 0, Voltage: 'Sanity test unperformed' }]
            error.value = true
        }
    } catch (err) {
        data.value = [{ Time: 0, Voltage: 'Flask Failure' + err }]
        error.value = true
        console.error(err)
    } finally {
        loading.value = false
    }
}
const emits = defineEmits(['close-sanity'])
function handleCloseSanity() {
    emits('close-sanity')
}
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
                    <Button v-if="loading" class="flex-none" disabled>
                        <div class="h-6 w-6">...</div>
                    </Button>
                    <Button
                        v-else-if="!loading && !error"
                        @click="fetchData"
                        class="text-black"
                    >
                        <Zap class="h-6 w-6" /> Discharge
                    </Button>
                    <Button
                        v-else-if="!loading && error"
                        @click="fetchData"
                        variant="destructive"
                    >
                        <LucideX class="h-6 w-6" />
                    </Button>
                    <!-- Add 'ml-auto' to right-align this button -->
                    <Button class="ml-auto" @click="handleCloseSanity">
                        <LucideX class="h-6 w-6" />
                    </Button>
                </div>

                <Skeleton v-if="loading" class="h-10 w-full mb-4"></Skeleton>
                <Table>
                    <TableCaption>Sanity Test Results (No Graph).</TableCaption>
                    <TableHeader>
                        <TableRow>
                            <TableHead class="w-[100px]">
                                Time (Seconds)
                            </TableHead>
                            <TableHead class="text-right">
                                Voltage (V)
                            </TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        <TableRow v-for="i in data" :key="i.time">
                            <TableCell class="font-medium text-white">
                                {{ i.Time }}
                            </TableCell>
                            <TableCell class="text-right">
                                {{ i.Voltage }}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </CardContent>
        </Card>
    </div>
</template>
