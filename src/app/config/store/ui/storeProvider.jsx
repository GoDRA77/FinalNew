import {Provider} from 'react-redux'
import {createReduxStore} from '@/app/config/store'
export const StoreProvider = props => {
  const {children, initialState} = props

  const store = createReduxStore(initialState)

  return <Provider store={store}>{children}</Provider>
}
