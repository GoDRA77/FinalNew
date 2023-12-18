import {configureStore} from '@reduxjs/toolkit'
import {userReducer} from '@/entities/auth/viewer'
import {loginReducer, registerReducer} from '@/features/auth/email-password-auth'

export function createReduxStore(initialState) {
  const rootReducers = {
    user: userReducer,
    loginForm: loginReducer,
    registerForm: registerReducer
  }

  return configureStore({
    reducer: rootReducers,
    preloadedState: initialState
  })
}
