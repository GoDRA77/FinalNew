import {createSlice} from '@reduxjs/toolkit'

const initialState = {
  username: '',
  password: '',
  isLoading: false,
  error: false
}

export const loginSlice = createSlice({
  name: 'login',
  initialState,
  reducers: {
    setUsername: (state, action) => {
      state.username = action.payload
    },
    setPassword: (state, action) => {
      state.password = action.payload
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload
    }
  }
})

export const {actions: loginActions} = loginSlice
export const {reducer: loginReducer} = loginSlice
