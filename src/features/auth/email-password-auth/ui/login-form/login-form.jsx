import {useDispatch, useSelector} from 'react-redux'
import {memo, useCallback, useState} from 'react'
import {loginActions} from '../../model/slice/loginSlice.js'
import {getLoginState} from '@/features/auth/email-password-auth/model/selectors/getLoginState.js'
import {loginByUsername} from '../../model/services/loginByUsername'
import {Paper, TextInput, PasswordInput, Checkbox, Button, Title, Text} from '@mantine/core'
import classes from './login-form.module.css'
import {NavLink} from 'react-router-dom'

export const LoginForm = memo(() => {
  const dispatch = useDispatch()
  const {username, password, error, isLoading} = useSelector(getLoginState)

  const [errors, setErrors] = useState({
    username: '',
    password: ''
  })

  const onChangeUsername = useCallback(
    value => {
      dispatch(loginActions.setUsername(value))

      if (value.length < 3) {
        setErrors(prevErrors => ({...prevErrors, username: 'Логин должен содержать не менее 3 символов'}))
      } else {
        setErrors(prevErrors => ({...prevErrors, username: ''}))
      }
    },
    [dispatch]
  )

  const onChangePassword = useCallback(
    value => {
      dispatch(loginActions.setPassword(value))

      // Ваша логика валидации для пароля
      /* const isLengthValid = value.length >= 8
      const hasNumber = /\d/.test(value)
      const hasUppercase = /[A-Z]/.test(value)

      if (!isLengthValid) {
        setErrors(prevErrors => ({...prevErrors, password: 'Пароль должен содержать не менее 8 символов'}))
      } else if (!hasNumber) {
        setErrors(prevErrors => ({...prevErrors, password: 'Пароль должен содержать хотя бы одну цифру'}))
      } else if (!hasUppercase) {
        setErrors(prevErrors => ({
          ...prevErrors,
          password: 'Пароль должен содержать хотя бы одну букву в верхнем регистре'
        }))
      } else {
        setErrors(prevErrors => ({...prevErrors, password: ''}))
      }*/
    },
    [dispatch]
  )

  console.log(username, password, error, isLoading)

  const onLoginClick = useCallback(() => {
    if (!username || !password || errors.username || errors.password) return
    dispatch(loginByUsername({username, password}))
  }, [dispatch, password, username, errors])

  return (
    <div className={classes.wrapper}>
      <Paper style={{maxWidth: '400px'}} className={classes.form} radius={0} p={30}>
        <Title order={2} className={classes.title} ta="center" mt="md" mb={50}>
          Добро пожаловать!
        </Title>

        <TextInput
          name="username"
          label="Логин"
          placeholder="Введите логин"
          required
          error={errors.username}
          onChange={event => onChangeUsername(event.currentTarget.value)}
          value={username}
        />
        <PasswordInput
          name="password"
          label="Пароль"
          placeholder="Введите пароль"
          required
          error={errors.password}
          mt="md"
          onChange={event => onChangePassword(event.currentTarget.value)}
          value={password}
        />
        <Checkbox label="Запомнить меня" mt="xl" size="md" />
        <Button fullWidth mt="xl" size="md" onClick={onLoginClick} disabled={isLoading}>
          Войти
        </Button>

        <Text ta="center" mt="md">
          У вас нету аккаунта?{' '}
          <Text fw={600} onClick={event => event.preventDefault()}>
            <NavLink to="/register"> Создать аккаунт </NavLink>
          </Text>
        </Text>
      </Paper>
    </div>
  )
})
