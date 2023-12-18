import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
  Input
} from '@mantine/core'
import classes from './register-form.module.css'
import {NavLink} from 'react-router-dom'
import {IconAt} from '@tabler/icons'
import {useId} from '@mantine/hooks'

export function RegisterForm() {
  const idEmail = useId()
  const idPhone = useId()
  return (
    <Container size={420} my={40}>
      <Title ta="center" className={classes.title}>
        Регистрация
      </Title>
      <Text c="dimmed" size="sm" ta="center" mt={5}>
        У вас уже есть аккаунт?{' '}
        <Anchor size="sm" component="button">
          <NavLink to="/login">Войти</NavLink>
        </Anchor>
      </Text>

      <Paper withBorder shadow="md" p={30} mt={30} radius="md">
        <TextInput label="Логин" placeholder="Ваш логин" required />
        <Input.Wrapper id={idEmail} label="Ваш email" required>
          <Input id={idEmail} label="Email" placeholder="Email" icon={<IconAt size={16} required />} />
        </Input.Wrapper>
        <Input.Wrapper id={idPhone} label="Ваш телефон" required>
          <Input type="number" id={idPhone} label="Телефон" placeholder="Email" />
        </Input.Wrapper>
        <TextInput label="Имя" placeholder="Имя" required />
        <TextInput label="Фамилия" placeholder="Фамилия" required />
        <PasswordInput label="Пароль" placeholder="Ваш пароль" required mt="md" />
        <PasswordInput label="Повторить пароль" placeholder="Ваш пароль" required mt="md" />
        <Group justify="space-between" mt="lg">
          <Checkbox label="Подтверждение на регистрацию" />
        </Group>
        <Button fullWidth mt="xl">
          Зарегистрироваться
        </Button>
      </Paper>
    </Container>
  )
}
