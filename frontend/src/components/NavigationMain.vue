<script setup lang="ts">
import {
    Menubar,
    MenubarCheckboxItem,
    MenubarContent,
    MenubarItem,
    MenubarMenu,
    MenubarRadioGroup,
    MenubarRadioItem,
    MenubarSeparator,
    MenubarShortcut,
    MenubarTrigger,
} from '@/components/ui/menubar'
import { ref } from 'vue'
import {
    Github,
    Music,
    FileUser,
    Braces,
    Ghost,
    RefreshCcwDot,
    Maximize,
    ChevronsLeftRightEllipsis,
} from 'lucide-vue-next'
const display_test_json = ref(true)
const emits = defineEmits(['display-test-json', 'display-sanity-test', 'display-graphing-data', 'display-export'])
function handleDisplayTestJson() {
    display_test_json.value = !display_test_json.value
    emits('display-test-json')
}
function handleDisplaySanityTest() {
    emits('display-sanity-test')
}
function handleDisplayExport() {
    emits('display-export')
}
const props = defineProps({
    intest: Boolean,
})
</script>

<template>
    <Menubar>
        <Button variant="icon">
            <img
                src="../assets/CBAStudioIcon.png"
                alt="logo"
                class="h-10 w-10"
            />
        </Button>
        <MenubarMenu>
            <MenubarTrigger>File</MenubarTrigger>
            <MenubarContent>
                <MenubarItem v-if="!intest">
                    Import <MenubarShortcut>Ctrl+I</MenubarShortcut>
                </MenubarItem>
                <MenubarItem v-else disabled>
                    Import <MenubarShortcut>Ctrl+I</MenubarShortcut>
                </MenubarItem>
                <MenubarItem @click="handleDisplayExport">
                    Export <MenubarShortcut>Ctrl+O</MenubarShortcut>
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem disabled>
                    Help <MenubarShortcut>Ctrl-H</MenubarShortcut>
                </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
        <MenubarMenu>
            <MenubarTrigger>Debug</MenubarTrigger>
            <MenubarContent>
                <MenubarCheckboxItem
                    v-if="display_test_json"
                    @click="handleDisplayTestJson"
                    ><Braces /> Display Test JSON</MenubarCheckboxItem
                >
                <MenubarCheckboxItem
                    v-else
                    checked
                    @click="handleDisplayTestJson"
                    ><Braces /> Hide Test JSON</MenubarCheckboxItem
                >
                <MenubarSeparator />
                <MenubarItem inset @click="handleDisplaySanityTest">
                    <Ghost /> Sanity Test
                </MenubarItem>
                <MenubarItem disabled inset>
                    <RefreshCcwDot /> Force Reload
                    <MenubarShortcut>⇧⌘R</MenubarShortcut>
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset>
                    <Maximize></Maximize> Toggle Fullscreen
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset @click="emits('display-graphing-data')">
                    <ChevronsLeftRightEllipsis></ChevronsLeftRightEllipsis>
                    Display GraphingData
                </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
        <MenubarMenu>
            <MenubarTrigger>Extra</MenubarTrigger>
            <MenubarContent>
                <MenubarRadioGroup value="extras">
                    <MenubarRadioItem value="music" disabled>
                        <Music></Music>Music
                    </MenubarRadioItem>
                    <a
                        href="https://github.com/Cybertaco360/LightCBA"
                        target="_blank"
                    >
                        <MenubarRadioItem>
                            <Github />Repository
                        </MenubarRadioItem>
                    </a>
                    <MenubarRadioItem value="Luis">
                        <FileUser />Credits
                    </MenubarRadioItem>
                </MenubarRadioGroup>
                <MenubarSeparator />
                <MenubarItem inset> Edit... </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset> Add Profile... </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
    </Menubar>
</template>
<style lang="css" scoped>
a {
    all: unset;
}
</style>
