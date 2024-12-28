<template>
    <div
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
    >
        <Card
            class="border border-gray-200 shadow-2xl bg-black p-8 flex flex-col items-center gap-6 rounded-lg"
        >
            <Button variant="outline" @click="closeConnect">X</Button>
            <CardContent>
                <transition name="fade" mode="out-in">
                    <button
                        v-if="!loading && !data"
                        key="button"
                        @click="fetchData"
                        class="relative flex items-center justify-center w-24 h-24 rounded-full bg-gray-200 text-gray-600 hover:bg-gray-300 transition-colors focus:outline-none focus:ring-4 focus:ring-blue-500/50"
                    >
                        <Skeleton class="absolute w-full h-full rounded-full" />
                        <LucideLoader2 class="w-8 h-8 text-gray-500" />
                    </button>

                    <div
                        v-else-if="loading"
                        key="connecting"
                        class="flex items-center justify-center w-24 h-24 rounded-full bg-blue-500 text-black animate-pulse"
                    >
                        <LucideLoader2 class="w-12 h-12 animate-spin" />
                    </div>

                    <div
                        v-else-if="data && !data.error"
                        key="connected"
                        class="flex items-center justify-center w-24 h-24 rounded-full bg-green-500 text-black"
                    >
                        <LucideCheck class="w-12 h-12" />
                    </div>

                    <div
                        v-else-if="data && data.error"
                        key="error"
                        class="flex items-center justify-center w-24 h-24 rounded-full bg-red-500 text-black"
                    >
                        <LucideX class="w-12 h-12" />
                    </div>
                </transition>

                <transition name="fade" mode="out-in">
                    <p
                        key="message"
                        v-if="loading"
                        class="mt-4 text-center text-lg font-medium text-gray-700"
                    >
                        Connecting…
                    </p>
                    <p
                        key="success"
                        v-else-if="data && !data.error"
                        class="mt-4 text-center text-lg font-semibold text-green-600"
                    >
                        {{ data.message }}
                    </p>
                    <p
                        key="error"
                        v-else-if="data && data.error"
                        class="mt-4 text-center text-lg font-medium text-red-600"
                    >
                        {{ data.message }}
                    </p>
                </transition>

                <transition name="fade" mode="out-in">
                    <button
                        v-if="data && data.error"
                        key="retry-button"
                        @click="fetchData"
                        class="mt-4 px-6 py-2 bg-red-500 text-black font-semibold rounded-lg hover:bg-red-300 transition-colors"
                    >
                        Retry
                    </button>
                </transition>
            </CardContent>
        </Card>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Card, CardContent } from '@/components/ui/card'
import { Skeleton } from '@/components/ui/skeleton'
import { LucideCheck, LucideLoader2, LucideX } from 'lucide-vue-next'
import { Button } from '@/components/ui/button'

const data = ref(null)
const loading = ref(false)
const error = ref(null)
const emits = defineEmits(['close-connect'])
function closeConnect() {
    emits('close-connect')
}
const fetchData = async () => {
    loading.value = true
    error.value = null
    data.value = null

    try {
        const response = await fetch('http://127.0.0.1:5000/api/connect')
        const result = await response.json()
        if (!response.ok) {
            data.value = {
                message: result.message || 'Something went wrong.',
                error: true,
            }
        } else {
            data.value = {
                message: result.message || 'Connection successful',
                error: false,
            }
        }
    } catch (err) {
        error.value = 'Failed to fetch data from Flask.'
        console.error(err)
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.animate-spin {
    animation: spin 1s linear infinite;
}

.animate-pulse {
    animation: pulse 1.5s infinite;
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

@keyframes pulse {
    0%,
    100% {
        opacity: 1;
    }
    50% {
        opacity: 0.8;
    }
}
</style>
