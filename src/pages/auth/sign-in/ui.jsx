import {PageTemplate} from '@/widgets/page-template'
import {Center} from '@mantine/core'
import {LoginForm} from '@/features/auth/email-password-auth/index.js'

export function LoginPage() {
  return (
    <PageTemplate>
      <Center>
        <div
          style={{
            maxWidth: '1280px',
            width: '100%',
            minHeight: '80vh',
            display: 'flex',
            justifyContent: 'center',
            flexDirection: 'column'
          }}
        >
          <LoginForm />
        </div>
      </Center>
    </PageTemplate>
  )
}
