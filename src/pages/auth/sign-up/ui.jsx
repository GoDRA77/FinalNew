import {PageTemplate} from '@/widgets/page-template'
import {Center} from '@mantine/core'
import {RegisterForm} from '@/features/auth/email-password-auth/index.js'

export function RegisterPage() {
  return (
    <PageTemplate>
      <Center>
        <RegisterForm />
      </Center>
    </PageTemplate>
  )
}
