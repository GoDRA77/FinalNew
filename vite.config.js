import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react'
import * as path from 'path'
import eslint from 'vite-plugin-eslint'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react({fastRefresh: false}), eslint()],
  server: {
    port: 5173
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})
