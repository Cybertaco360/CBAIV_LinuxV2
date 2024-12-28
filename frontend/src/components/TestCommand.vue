<script setup lang="ts">
import { Card, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from '@/components/ui/select'
import {
    Stepper,
    StepperDescription,
    StepperItem,
    StepperSeparator,
    StepperTitle,
    StepperTrigger,
} from '@/components/ui/stepper'
import { toTypedSchema } from '@vee-validate/zod'
import {
    Dot,
    BatteryMedium,
    ChartLine,
    BatteryCharging,
    ListCheck,
} from 'lucide-vue-next'
import { h, ref } from 'vue'
import * as z from 'zod'
defineProps({
    toggle: {
        type: Boolean,
        required: true,
    },
    hashmap: {
        type: Object,
        required: true,
    },
})
const emit = defineEmits(['update-hashmap', 'close-modal'])
const formSchema = [
    z.object({
        current: z.number(),
        cutoff: z.number(),
        name: z.string(),
    }),
    z.object({
        dataPrecision: z.number(),
        regressionAmount: z.number(),
    }),
    z.object({
        'Battery Type': z.union([
            z.literal('Alkaline 9V'),
            z.literal('Zinc-Carbon 9V'),
            z.literal('Other'),
        ]),
    }),
]
const stepIndex = ref(1)
const steps = [
    {
        step: 1,
        title: 'Test Details',
        description: 'Provide the Current and Voltage Cutoff',
        icon: BatteryMedium,
    },
    {
        step: 2,
        title: 'Graph Data',
        description: 'Provide the Data Precision and Regression Level',
        icon: ChartLine,
    },
    {
        step: 3,
        title: 'Battery Type',
        description: 'Define  the Battery Type',
        icon: BatteryCharging,
    },
    {
        step: 4,
        title: 'Summary and Connection Checking',
        description:
            'Check battery test configuration check and connection checking',
        icon: ListCheck,
    },
]

function onSubmit(values: any) {
    Object.entries(values).forEach(([key, value]) => {
        emit('update-hashmap', { key, value })
    })
    emit('close-modal')
}
function close() {
    emit('close-modal')
}
</script>
<template>
    <div
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50"
    >
        <Card class="w-auto">
            <CardContent>
                <Button @click="close" variant="outline">x</Button>
                <Form
                    v-slot="{ meta, values, validate }"
                    as=""
                    keep-values
                    :validation-schema="
                        toTypedSchema(formSchema[stepIndex - 1])
                    "
                >
                    <div class="w-500 h-min">
                        <h1 style="margin-left: 40%">
                            <b>Battery Test Configuration Edit</b>
                        </h1>
                    </div>
                    <Stepper
                        v-slot="{
                            isNextDisabled,
                            isPrevDisabled,
                            nextStep,
                            prevStep,
                        }"
                        v-model="stepIndex"
                        class="block w-full"
                    >
                        <form
                            @submit="
                                (e) => {
                                    e.preventDefault()
                                    validate()

                                    if (
                                        stepIndex === steps.length &&
                                        meta.valid
                                    ) {
                                        onSubmit(values)
                                    }
                                }
                            "
                        >
                            <div class="flex w-full flex-start gap-2">
                                <StepperItem
                                    v-for="step in steps"
                                    :key="step.step"
                                    v-slot="{ state }"
                                    class="relative flex w-full flex-col items-center justify-center"
                                    :step="step.step"
                                >
                                    <StepperSeparator
                                        v-if="
                                            step.step !==
                                            steps[steps.length - 1].step
                                        "
                                        class="absolute left-[calc(50%+20px)] right-[calc(-50%+10px)] top-5 block h-0.5 shrink-0 rounded-full bg-muted group-data-[state=completed]:bg-primary"
                                    />

                                    <StepperTrigger as-child>
                                        <Button
                                            :variant="
                                                state === 'completed' ||
                                                state === 'active'
                                                    ? 'default'
                                                    : 'outline'
                                            "
                                            size="icon"
                                            class="z-10 rounded-full shrink-0"
                                            :class="[
                                                state === 'active' &&
                                                    'ring-2 ring-ring ring-offset-2 ring-offset-background',
                                            ]"
                                            :disabled="
                                                state !== 'completed' &&
                                                !meta.valid
                                            "
                                        >
                                            <component
                                                :is="step.icon"
                                                v-if="
                                                    state === 'completed' ||
                                                    state === 'active'
                                                "
                                                class="w-4 h-4"
                                            />
                                            <Dot v-if="state === 'inactive'" />
                                        </Button>
                                    </StepperTrigger>

                                    <div
                                        class="mt-5 flex flex-col items-center text-center"
                                    >
                                        <StepperTitle
                                            :class="[
                                                state === 'active' &&
                                                    'text-primary',
                                            ]"
                                            class="text-sm font-semibold transition lg:text-base"
                                        >
                                            {{ step.title }}
                                        </StepperTitle>
                                        <StepperDescription
                                            :class="[
                                                state === 'active' &&
                                                    'text-primary',
                                            ]"
                                            class="sr-only text-xs text-muted-foreground transition md:not-sr-only lg:text-sm"
                                        >
                                            {{ step.description }}
                                        </StepperDescription>
                                    </div>
                                </StepperItem>
                            </div>
                            <div class="flex flex-col gap-4 mt-4">
                                <template v-if="stepIndex === 1">
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="name"
                                    >
                                        <FormItem>
                                            <FormLabel>Battery Name</FormLabel>
                                            <FormControl>
                                                <Input
                                                    type="string"
                                                    v-bind="componentField"
                                                    placeholder="ex. YM-25-01 or 6F22-01"
                                                />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="current"
                                    >
                                        <FormItem>
                                            <FormLabel
                                                >Current/Capacity(A)</FormLabel
                                            >
                                            <FormControl>
                                                <Input
                                                    type="number"
                                                    v-bind="componentField"
                                                />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>

                                    <FormField
                                        v-slot="{ componentField }"
                                        name="cutoff"
                                    >
                                        <FormItem>
                                            <FormLabel
                                                >Cutoff Voltage(V)</FormLabel
                                            >
                                            <FormControl>
                                                <Input
                                                    type="number"
                                                    v-bind="componentField"
                                                />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                </template>

                                <template v-if="stepIndex === 2">
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="dataPrecision"
                                    >
                                        <FormItem>
                                            <FormLabel>Precision(ms)</FormLabel>
                                            <FormControl>
                                                <Input
                                                    type="number"
                                                    v-bind="componentField"
                                                />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="regressionAmount"
                                    >
                                        <FormItem>
                                            <FormLabel
                                                >Regression Level
                                                (INTEGER)</FormLabel
                                            >
                                            <FormControl>
                                                <Input
                                                    type="number"
                                                    v-bind="componentField"
                                                    placeholder="Recommended: 2-3"
                                                />
                                            </FormControl>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                </template>

                                <template v-if="stepIndex === 3">
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="Battery Type"
                                    >
                                        <FormItem>
                                            <FormLabel>Battery Type</FormLabel>

                                            <Select v-bind="componentField">
                                                <FormControl>
                                                    <SelectTrigger>
                                                        <SelectValue
                                                            placeholder="Select Battery Type"
                                                        />
                                                    </SelectTrigger>
                                                </FormControl>
                                                <SelectContent>
                                                    <SelectGroup>
                                                        <SelectItem
                                                            value="Alkaline 9V"
                                                        >
                                                            Alkaline 9V
                                                        </SelectItem>
                                                        <SelectItem
                                                            value="Zinc-Carbon 9V"
                                                        >
                                                            Zinc-Carbon 9V
                                                        </SelectItem>
                                                        <SelectItem
                                                            value="Other"
                                                        >
                                                            Other
                                                        </SelectItem>
                                                    </SelectGroup>
                                                </SelectContent>
                                            </Select>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                </template>

                                <template v-if="stepIndex === 4">
                                    <FormField
                                        v-slot="{ componentField }"
                                        name="Checkup"
                                    >
                                        <FormItem>
                                            <FormLabel>Checkup</FormLabel>

                                            <div
                                                class="flex items-center space-x-2"
                                            >
                                                <Checkbox value="true" required />
                                                <label
                                                    for="terms"
                                                    class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                                                >
                                                    Accept terms and conditions
                                                </label>
                                            </div>
                                            <FormMessage />
                                        </FormItem>
                                    </FormField>
                                </template>
                            </div>

                            <div class="flex items-center justify-between mt-4">
                                <Button
                                    :disabled="isPrevDisabled"
                                    variant="outline"
                                    size="sm"
                                    @click="prevStep()"
                                >
                                    Back
                                </Button>
                                <div class="flex items-center gap-3">
                                    <Button
                                        v-if="stepIndex !== 4"
                                        :type="meta.valid ? 'button' : 'submit'"
                                        :disabled="isNextDisabled"
                                        size="sm"
                                        @click="meta.valid && nextStep()"
                                    >
                                        Next
                                    </Button>
                                    <Button
                                        v-if="stepIndex === 4"
                                        size="sm"
                                        type="submit"
                                    >
                                        Submit
                                    </Button>
                                </div>
                            </div>
                        </form>
                    </Stepper>
                </Form>
            </CardContent>
        </Card>
    </div>
</template>