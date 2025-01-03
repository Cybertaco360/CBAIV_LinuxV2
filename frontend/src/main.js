import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

// Prism.js for syntax highlighting
import 'prismjs'

// Import your CSS files
import './assets/base.css'
import './assets/main.css'
import './assets/index.css'

function sleep(seconds) {
    return new Promise((resolve) => setTimeout(resolve, seconds * 1000))
}

async function setup() {
    await sleep(8) // Simulate a heavy task
    return
}

// Function to handle splash screen removal
function removeSplashScreen() {
    const splashScreen = document.getElementById('splash-screen')
    const appElement = document.getElementById('app')

    if (splashScreen) {
        splashScreen.style.opacity = '0' // Trigger fade-out effect
        setTimeout(() => {
            console.log('Splash screen removed from DOM.')
            splashScreen.remove() // Remove the splash screen
            if (appElement) {
                appElement.style.display = 'flex' // Show the Vue app
            }
        }, 500) // Match fade-out duration
    }
}

window.addEventListener('DOMContentLoaded', async () => {
    await setup() // Ensure setup is complete
    removeSplashScreen() // Fade out and remove splash screen
})

const app = createApp(App)

app.use(createPinia())

app.mount('#app')
