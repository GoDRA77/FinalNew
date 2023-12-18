import {createSlice} from '@reduxjs/toolkit'

const initialState = {
  username: '',
  password: '',
  passwordConfirmation: '',
  email: '',
  firstName: '',
  lastName: '',
  dateOfBirth: null,
  gender: '',
  country: '',
  region: '',
  phoneNumber: '',
  agreedToTerms: false,
  isLoading: false,
  error: false
}

export const registrationSlice = createSlice({
  name: 'registration',
  initialState,
  reducers: {
    setUsername: (state, action) => {
      state.username = action.payload
    },
    setPassword: (state, action) => {
      state.password = action.payload
    },
    setPasswordConfirmation: (state, action) => {
      state.passwordConfirmation = action.payload
    },
    setEmail: (state, action) => {
      state.email = action.payload
    },
    setFirstName: (state, action) => {
      state.firstName = action.payload
    },
    setLastName: (state, action) => {
      state.lastName = action.payload
    },
    setDateOfBirth: (state, action) => {
      state.dateOfBirth = action.payload
    },
    setGender: (state, action) => {
      state.gender = action.payload
    },
    setCountry: (state, action) => {
      state.country = action.payload
    },
    setRegion: (state, action) => {
      state.region = action.payload
    },
    setPhoneNumber: (state, action) => {
      state.phoneNumber = action.payload
    },
    setAgreedToTerms: (state, action) => {
      state.agreedToTerms = action.payload
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload
    }
  }
})

export const {actions: registerActions} = registrationSlice
export const {reducer: registerReducer} = registrationSlice
