import {createBrowserRouter} from 'react-router-dom'
import {HomePage, LoginPage, RegisterPage, ProfilePage} from '@/pages'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <HomePage />
  },
  {
    path: '/login',
    element: <LoginPage />
  },
  {
    path: '/register',
    element: <RegisterPage />
  },
  {
    path: '/profile',
    element: <ProfilePage />
  }
])
