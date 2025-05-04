import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '^/api*': {
<<<<<<< HEAD
        target: 'http://localhost:8080/',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: "app/static",
    emptyOutDir: true,
=======
        target: 'http://localhost:5001/',
        changeOrigin: true
      }
    }
>>>>>>> 7dcaeba (Initial commit with updated ProfileDetailView button styles)
  }
})
