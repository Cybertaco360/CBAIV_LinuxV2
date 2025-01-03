<script setup lang="ts">
import {
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator,
} from '@/components/ui/command'

import { useMagicKeys } from '@vueuse/core'
import { ref, watch, defineExpose } from 'vue'
import {
    BatteryFull,
    PlugZap,
    Book,
    Github,
    Music,
    FileUser,
} from 'lucide-vue-next'

const open = ref(false)

const { Meta_M, Ctrl_M } = useMagicKeys({
    passive: false,
    onEventFired(e) {
        if (e.key === 'm' && (e.metaKey || e.ctrlKey)) e.preventDefault()
    },
})

watch([Meta_M, Ctrl_M], (v) => {
    if (v[0] || v[1]) handleOpenChange()
})

function handleOpenChange() {
    open.value = !open.value
}

const emits = defineEmits(['launch-test', 'launch-connect', 'launch-credits'])

function launchTest() {
    emits('launch-test')
    handleOpenChange()
}
function launchConnect() {
    emits('launch-connect')
    handleOpenChange()
}
function launchCredits() {
    emits('launch-credits')
    handleOpenChange()
}
defineExpose({ handleOpenChange })
</script>

<template>
    <div>
        <CommandDialog v-model:open="open">
            <CommandInput placeholder="Type a command or search..." />
            <CommandList>
                <CommandEmpty>No results found.</CommandEmpty>
                <CommandGroup heading="Primary Functions">
                    <CommandItem value="batterytest" @click="launchTest">
                        <BatteryFull />
                        Battery Test
                    </CommandItem>
                    <CommandItem value="connect" @click="launchConnect">
                        <PlugZap />
                        Connect
                    </CommandItem>
                    <CommandItem value="manual" disabled>
                        <Book />
                        Manual
                    </CommandItem>
                </CommandGroup>
                <CommandSeparator />
                <CommandGroup heading="Other">
                    <a
                        href="https://github.com/Cybertaco360/LightCBA"
                        target="_blank"
                    >
                        <CommandItem value="repository">
                            <Github />
                            Repository
                        </CommandItem>
                    </a>
                    <CommandItem value="music" disabled>
                        <Music />
                        Music
                    </CommandItem>
                    <CommandItem value="credits" @click="launchCredits">
                        <FileUser />
                        Credits
                    </CommandItem>
                </CommandGroup>
            </CommandList>
        </CommandDialog>
    </div>
</template>
<style lang="css" scoped>
a {
    all: unset;
}
</style>
