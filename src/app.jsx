import {RouterProvider} from 'react-router-dom'
import {router} from '@/app/index.js'
import {useDispatch} from 'react-redux'
import {useEffect} from 'react'
import {userActions} from '@/entities/auth/viewer/index.js'

const App = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(userActions.initAuthData())
  }, [dispatch])

  return <RouterProvider router={router} />
}

export default App
