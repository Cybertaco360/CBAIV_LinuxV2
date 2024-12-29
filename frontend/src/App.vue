<template>
    <NavigationMain
        class="fixed top-0 left-0"
        @display-test-json="display_test_json = !display_test_json"
        @display-sanity-test="showSanity = true"
        :intest="testing"
    ></NavigationMain>
    <div
        v-if="display_test_json"
        class="fixed bottom-0 left-0 p-4 bg-zinc-950 text-gray-500 z-50"
    >
        <p>
            {{ configuration }}
        </p>
    </div>
    <div class="fixed top-0 right-0">
        <DropdownMenu>
            <DropdownMenuTrigger as-child>
                <Button variant="outline">
                    <Icon
                        icon="radix-icons:moon"
                        class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
                    />
                    <Icon
                        icon="radix-icons:sun"
                        class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
                    />
                    <span class="sr-only">Toggle theme</span>
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
                <DropdownMenuItem @click="mode = 'light'">
                    Light
                </DropdownMenuItem>
                <DropdownMenuItem @click="mode = 'dark'">
                    Dark
                </DropdownMenuItem>
                <DropdownMenuItem @click="mode = 'auto'">
                    System
                </DropdownMenuItem>
            </DropdownMenuContent>
        </DropdownMenu>
    </div>
    <div class="flex w-max h-full">
        <Graph
            :data="graphingdata"
            style="height: 500px; width: 1500px; margin-left: -350px"
            :colors="colors"
        ></Graph>
        <div class="h-full" style="width: 350px">
            <Card class="h-full">
                <CardHeader class="flex flex-row items-start bg-muted/50">
                    <div class="grid gap-0.5">
                        <CardTitle
                            class="group flex items-center gap-5 text-xl"
                        >
                            Current Test Information
                        </CardTitle>
                        <CardDescription class="w-max">
                          <span>
                            Date: {{ batteryTestResult['Date'] }}
                          </span>
                        </CardDescription>
                        <CardDescription>
                          <span>
                            Battery: {{ batteryTestResult['Battery'] }}
                          </span>
                        </CardDescription>
                    </div>
                    <div class="ml-auto flex items-center gap-1">
                        <DropdownMenu>
                            <DropdownMenuTrigger as-child>
                                <Button
                                    size="icon"
                                    variant="outline"
                                    class="h-8 w-8"
                                >
                                    <EllipsisVertical class="h-3.5 w-3.5" />
                                    <span class="sr-only">More</span>
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end">
                                <DropdownMenuItem>Export</DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
                    </div>
                </CardHeader>
                <CardContent class="p-6 text-sm">
                    <div class="grid gap-3">
                        <div class="font-semibold">Test Details</div>
                        <ul class="grid gap-3">
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground">
                                    Initial Voltage
                                </span>
                                <span
                                    >{{
                                        batteryTestResult['Initial Voltage']
                                    }}V</span
                                >
                            </li>
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground">
                                    Peak Voltage
                                </span>
                                <span
                                    >{{
                                        batteryTestResult['Peak Voltage']
                                    }}V</span
                                >
                            </li>
                        </ul>
                        <Separator class="my-2" />
                        <ul class="grid gap-3">
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground"
                                    >Initial Drop Voltage</span
                                >
                                <span
                                    >{{
                                        batteryTestResult[
                                            'Initial Drop Voltage'
                                        ]
                                    }}V</span
                                >
                            </li>
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground"
                                    >Cutoff Voltage</span
                                >
                                <span
                                    >{{
                                        batteryTestResult['Cutoff Voltage']
                                    }}V</span
                                >
                            </li>
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground"
                                    >Current:</span
                                >
                                <span
                                    >{{
                                        batteryTestResult['Current']
                                    }}A</span
                                >
                            </li>
                            <li class="flex items-center justify-between">
                                <span class="text-muted-foreground">Time</span>
                                <span>{{ batteryTestResult['Time'] }}</span>
                            </li>
                            <li
                                class="flex items-center justify-between font-semibold"
                            >
                                <span class="text-muted-foreground"
                                    >Final Capacity</span
                                >
                                <span
                                    >{{
                                        batteryTestResult['Final Capacity(Ah)']
                                    }}
                                    Ah</span
                                >
                            </li>
                            <li
                                class="flex items-center justify-between font-semibold"
                            >
                                <span class="text-muted-foreground"
                                    >Capacity% (Battery Quality)</span
                                >
                                <span
                                    >{{
                                        batteryTestResult[
                                            'Capacity% (Battery Quality)'
                                        ]
                                    }}%</span
                                >
                            </li>
                            <li class="mt-5 text-center" v-if="!testing">
                                <Button
                                    class="bg-red-700 text-white hover:bg-red-500"
                                    @click="confirmation = true"
                                    ><Zap />Discharge Test With Current
                                    Configuration</Button
                                >
                            </li>
                            <li class="mt-5 text-center" v-else>
                                <Button
                                    class="bg-red-500 text-white hover:bg-red-500"
                                    disabled
                                    ><Zap />Test Currently Running...</Button
                                >
                            </li>
                            <li class="mt-5 text-center" v-if="!testing">
                                <Button
                                    class="bg-red-700 text-white hover:bg-red-500"
                                    disabled
                                    ><ShieldAlert />No Test Running
                                    </Button
                                >
                            </li>
                            <li class="mt-5 text-center" v-else>
                                <Button
                                    class="bg-red-500 text-white hover:bg-red-500"
                                    @click="emergencyStop()"
                                    ><ShieldAlert />Stop Current Test</Button
                                >
                            </li>
                        </ul>
                    </div>
                </CardContent>
                <CardFooter
                    class="flex flex-row items-center border-t bg-muted/50 px-6 py-3 mt-5"
                >
                    <div class="text-xs text-muted-foreground">
                        Current Time:
                        <time dateTime="2023-11-23">{{ currentTime }}</time>
                    </div>
                    <Pagination class="ml-auto mr-0 w-auto">
                        <PaginationList class="gap-1">
                            <PaginationPrev variant="outline" class="h-6 w-6" />
                            <PaginationNext variant="outline" class="h-6 w-6" />
                        </PaginationList>
                    </Pagination>
                </CardFooter>
            </Card>
        </div>
    </div>
    <div class="w-full fixed bottom-0 left-0">
        <ColorPalette @colorOneUpdate="colorOneUpdate" @colorTwoUpdate="colorTwoUpdate"/>
    </div>
    <TestCommand
        v-if="showCommand"
        style="position: fixed; align-self: center"
        :toggle="showCommand"
        :hashmap="configuration"
        @close-modal="showCommand = false"
        @update-hashmap="updateHashmap"
    />
    <Connecting v-if="showConnect" @close-connect="showConnect = false" />
    <SanityTest
        v-if="showSanity"
        @close-sanity="showSanity = false"
    ></SanityTest>
    <TestConfirmation
        v-if="confirmation"
        :configuration="configuration"
        @start-test="batteryFullTest()"
        @close-confirmation="confirmation = false"
    >
    </TestConfirmation>
    <AllCommands
        ref="allCommands"
        @launch-test="showCommand = true"
        @launch-connect="showConnect = true"
    ></AllCommands>
    <Toaster richColors/>
</template>
<!-- PLEASE STOP TRYING TO USE OPTIONS API IN THE SETUP-->
<script setup lang="ts">
import TestCommand from '@/components/TestCommand.vue'
import { Button } from '@/components/ui/button'
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { Icon } from '@iconify/vue'
import { useColorMode } from '@vueuse/core'
import Graph from '@/components/Graph.vue'
import { ref, onMounted, watch, reactive } from 'vue'
import AllCommands from '@/components/AllCommands.vue'
import { EllipsisVertical, Zap, ShieldAlert } from 'lucide-vue-next'
import CardDescription from '@/components/ui/card/CardDescription.vue'
import Connecting from '@/components/Connecting.vue'
import NavigationMain from '@/components/NavigationMain.vue'
import SanityTest from '@/components/SanityTest.vue'
import regression from 'regression'
import TestConfirmation from '@/components/TestConfirmation.vue'
import { toast } from 'vue-sonner'
import { Toaster } from '@/components/ui/sonner'
import ColorPalette from './components/ColorPalette.vue'
const mode = useColorMode()
const showCommand = ref(false)
const configuration = ref({ dataPrecision: 1000 })
const showConnect = ref(false)
const display_test_json = ref(false)
function updateHashmap({ key, value }) {
    configuration.value[key] = value
}
const colors = ref(['#0F0', '#F00'])
function colorOneUpdate(color: string='') {
    colors.value[0] = color
}
function colorTwoUpdate(color: string='') {
    colors.value[1] = color
}
const allCommands = ref(null)
const showSanity = ref(false)
const confirmation = ref(false)
const testing = ref(false)
let collectingInterval: NodeJS.Timeout | null = null
let initialdropfound = false
const batteryTestResult = reactive({
    "Date": 'November 23, 2023',
    "Battery": 'YM-25-01',
    'Initial Voltage': 1,
    'Peak Voltage': 2,
    'Initial Drop Voltage': 3,
    'Cutoff Voltage': 4,
    'Time': 5,
    'Current': 6,
    'Final Capacity(Ah)': 6,
    'Capacity% (Battery Quality)': 7,
})
const graphingdata = reactive([
    {
        time: '1',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '2',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '3',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '4',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '5',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '6',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
    {
        time: '7',
        'Predicted Voltage': (Math.random()+2)*100,
        Voltage: (Math.random()+2)*100,
    },
])
onMounted(() => {
    window.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'p') {
            e.preventDefault()
            showCommand.value = !showCommand.value
        }
    })
})
async function batteryFullTest() {
    console.log('Starting test with configuration:', configuration.value)
    const response = await fetch('http://127.0.0.1:5000/api/start_test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(configuration.value),
    })
    const result = await response.json()
    if (response.ok) {
      this.testing = true
      graphingdata.splice(0, graphingdata.length)
      toast.success('Test Started', {
        description: 'Test has started successfully.',
      })
    } else {
        console.error('Failed to start test');
        toast.error('Test Failed', {
        description: 'Check physical connections and try again.',
        action: {
          label: 'Try Again',
          onClick: () => batteryFullTest(),
        },
      })
      this.testing = false
    }
    Object.assign(batteryTestResult,{
        "Date": '',
        "Battery": result['Battery'],
        'Initial Voltage': result['Initial Voltage'],
        'Peak Voltage': 0,
        'Initial Drop Voltage': 0,
        'Cutoff Voltage': result['Cutoff Voltage'],
        "Time": 0,
        'Current': result['Current'],
        'Final Capacity(Ah)': 0,
        'Capacity% (Battery Quality)': 0,
    })
    var setDate = new Date()
    batteryTestResult['Date'] = `${String(setDate.getMonth() + 1).padStart(2, '0')}/` +
                   `${String(setDate.getDate()).padStart(2, '0')}/` +
                   `${setDate.getFullYear()} ` +
                   `${String(setDate.getHours() % 12 || 12).padStart(2, '0')}:` +
                   `${String(setDate.getMinutes()).padStart(2, '0')}:` +
                   `${String(setDate.getSeconds()).padStart(2, '0')} ` +
                   `${setDate.getHours() >= 12 ? 'PM' : 'AM'}`;
    console.log(this.currentTime)
}
watch(testing, (newTestingState) => {
    if (newTestingState) {
        DataCollection()
    } else {
        stopDataCollection()
    }
})
function DataCollection() {
    const precision = configuration.value.dataPrecision
    collectingInterval = setInterval(async() => {
      try {
            const response = await fetch('http://127.0.0.1:5000/api/data_collection')
            if (response.ok) {
                const data = await response.json()
                console.log(data)
                if (data['Status'] == 'Running'){
                graphingdata.push({time: `${data['Time']*precision/1000}`, 'Predicted Voltage': data['Predicted Voltage'], Voltage: data['Voltage']})
                if (initialdropfound == false && data['Drop Voltage Detected'] !== null) {
                    initialdropfound = true
                    Object.assign(batteryTestResult, {
                        'Initial Drop Voltage': data['Drop Voltage Detected'],
                    })
                }
                } else {
                    Object.assign(batteryTestResult, {
                        'Peak Voltage': data['Peak Voltage'],
                        'Time': data['End Time'],
                        'Final Capacity(Ah)': data['End Time']/3600*batteryTestResult['Current'],
                        'Capacity% (Battery Quality)': data['Final Capacity(Ah)']/batteryTestResult['Current'],
                    })
                    fullTestCompletion()
                }
            } else {
                console.error('Failed to fetch data:', response.statusText)
                toast.error('Backend connection failed')
                testing.value = false
                stopDataCollection()
            }
        } catch (error) {
            console.error('Error fetching data:', error)
            toast.error('Backend connection error')
            testing.value = false
            stopDataCollection()
        }
    }, precision)
}
function stopDataCollection() {
    if (collectingInterval){
        clearInterval(collectingInterval)
        collectingInterval = null
    }
}
function fullTestCompletion() {
    console.log('Test completed')
    testing.value = false
    stopDataCollection()
    toast.success('Test Completed', {
        description: 'Test has completed successfully.',
    })
}
const emergencyResult = ref(null)
async function emergencyStop() {
    console.log('Emergency stop')
    this.testing = false
    stopDataCollection()
    toast.error('Test Stopped', {
        description: 'Test has been stopped.',
    })
    const response = await fetch('http://127.0.0.1:5000/api/emergency')
    this.emergencyResult = await response.json()['message']
    toast.success(emergencyResult.value)
}
onMounted(() => {
    stopDataCollection()
})
</script>
<!-- OPTIONS API AND DATA IN HERE PLEASE-->
<script lang="ts">

export default {
    data() {
        return {
            currentTime: '',
        }
    },
    methods: {
        updateTime() {
          const now = new Date();
this.currentTime = `${String(now.getMonth() + 1).padStart(2, '0')}/` +
                   `${String(now.getDate()).padStart(2, '0')}/` +
                   `${now.getFullYear()} ` +
                   `${String(now.getHours() % 12 || 12).padStart(2, '0')}:` +
                   `${String(now.getMinutes()).padStart(2, '0')}:` +
                   `${String(now.getSeconds()).padStart(2, '0')} ` +
                   `${now.getHours() >= 12 ? 'PM' : 'AM'}`;
        },
    },
    mounted() {
        this.updateTime()
        this.timeInterval = setInterval(this.updateTime, 1000)
    },
    beforeDestroy() {
        clearInterval(this.timeInterval)
    },
}
</script>