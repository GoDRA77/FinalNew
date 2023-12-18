import React from 'react'
import ReactDOM from 'react-dom/client'
import {MantineProvider} from '@mantine/core'
import App from '@/app.jsx'
import {StoreProvider} from '@/app/config/store'

ReactDOM.createRoot(document.getElementById('root')).render(
  <MantineProvider>
    <StoreProvider>
      <App />
    </StoreProvider>
  </MantineProvider>
)
