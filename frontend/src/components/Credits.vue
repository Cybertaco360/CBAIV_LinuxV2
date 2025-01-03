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
                    @click="emits('close-credits')"
                    variant="outline"
                >
                    <LucideX class="h-6 w-6" color="white"/>
                </Button>
            </div>
            <div class="text-center justify-between w-max">
                    <h2 class="text-xl font-semibold glow">Credits</h2>
            </div>
            <CardContent>
                <div class="grid grid-cols-2 gap-4" style="width: 500px;">
                    <p class="text-white glow text-left">
                    Goldy Yan (Cybertaco360)
                    </p>
                    <p class="text-right">
                    Main Developer
                    </p>
                    <p class="text-white glow text-left">
                        Da66en
                    </p>
                    <p class="text-right">
                        Original Library Creator
                    </p>
                </div>
            </CardContent>
        </Card>
    </div>
</template>
<script setup lang="ts">
import Card from './ui/card/Card.vue';
import Button from './ui/button/Button.vue';
import {LucideX} from 'lucide-vue-next';
const emits = defineEmits(['close-credits'])
</script>