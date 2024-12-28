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
const display_test_json = ref(true)
const emits = defineEmits(['display-test-json', 'display-sanity-test'])
function handleDisplayTestJson() {
    display_test_json.value = !display_test_json.value
    emits('display-test-json')
}
function handleDisplaySanityTest() {
    emits('display-sanity-test')
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
                <MenubarItem>
                    Export <MenubarShortcut>Ctrl+O</MenubarShortcut>
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem>
                    Help <MenubarShortcut>Ctrl-H</MenubarShortcut>
                </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
        <MenubarMenu>
            <MenubarTrigger>Edit</MenubarTrigger>
            <MenubarContent>
                <MenubarItem>
                    Undo <MenubarShortcut>⌘Z</MenubarShortcut>
                </MenubarItem>
                <MenubarItem>
                    Redo <MenubarShortcut>⇧⌘Z</MenubarShortcut>
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem>Cut</MenubarItem>
                <MenubarItem>Copy</MenubarItem>
                <MenubarItem>Paste</MenubarItem>
            </MenubarContent>
        </MenubarMenu>
        <MenubarMenu>
            <MenubarTrigger>Debug</MenubarTrigger>
            <MenubarContent>
                <MenubarCheckboxItem
                    v-if="display_test_json"
                    @click="handleDisplayTestJson"
                    >Display Test JSON</MenubarCheckboxItem
                >
                <MenubarCheckboxItem
                    v-else
                    checked
                    @click="handleDisplayTestJson"
                    >Display Test JSON</MenubarCheckboxItem
                >
                <MenubarSeparator />
                <MenubarItem inset @click="handleDisplaySanityTest">
                    Sanity Test
                </MenubarItem>
                <MenubarItem disabled inset>
                    Force Reload <MenubarShortcut>⇧⌘R</MenubarShortcut>
                </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset> Toggle Fullscreen </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset> Hide Sidebar </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
        <MenubarMenu>
            <MenubarTrigger>Extra</MenubarTrigger>
            <MenubarContent>
                <MenubarRadioGroup value="extras">
                    <MenubarRadioItem value="music"> Music </MenubarRadioItem>
                    <MenubarRadioItem value="benoit"> Repository </MenubarRadioItem>
                    <MenubarRadioItem value="Luis"> Credits </MenubarRadioItem>
                </MenubarRadioGroup>
                <MenubarSeparator />
                <MenubarItem inset> Edit... </MenubarItem>
                <MenubarSeparator />
                <MenubarItem inset> Add Profile... </MenubarItem>
            </MenubarContent>
        </MenubarMenu>
    </Menubar>
</template>
<!--

<Button variant="icon">
            <img src="../assets/CBAStudioIcon.png" alt="logo" class="h-10 w-10" />
        </Button>

-->
