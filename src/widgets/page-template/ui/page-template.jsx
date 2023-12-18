import React from 'react'
import {HeaderMenu} from '@/widgets/header'

export const PageTemplate = ({children}) => {
  return (
    <div>
      <HeaderMenu />
      {children}
    </div>
  )
}
