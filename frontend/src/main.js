import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

// Import your CSS files
import './assets/base.css'
import './assets/main.css'
import './assets/index.css'

function sleep(seconds) {
    return new Promise((resolve) => setTimeout(resolve, seconds * 1000))
}

async function setup() {
    console.log('Performing really heavy frontend setup task...')
    await sleep(3) // Simulate a heavy task
    console.log('Frontend setup task complete!')
    return
}

// Function to handle splash screen removal
function removeSplashScreen() {
    console.log('Removing splash screen...')
    const splashScreen = document.getElementById('splash-screen')
    const appElement = document.getElementById('app')

    if (splashScreen) {
        splashScreen.style.opacity = '0' // Trigger fade-out effect
        setTimeout(() => {
            console.log('Splash screen removed from DOM.')
            splashScreen.remove() // Remove the splash screen
            if (appElement) {
                appElement.style.display = 'flex' // Show the Vue app
                console.log('App element made visible.')
            }
        }, 500) // Match fade-out duration
    } else {
        console.error('Splash screen element not found.')
    }
}

window.addEventListener('DOMContentLoaded', async () => {
    console.log('DOMContentLoaded event fired.')
    await setup() // Ensure setup is complete
    removeSplashScreen() // Fade out and remove splash screen
})

const app = createApp(App)

app.use(createPinia())

app.mount('#app')
