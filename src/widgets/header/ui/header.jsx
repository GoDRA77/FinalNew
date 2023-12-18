import {createStyles, Header, Group, Burger, Container, Button, Transition, Paper} from '@mantine/core'
import {useDisclosure} from '@mantine/hooks'
import {NavLink} from 'react-router-dom'
import {useSelector, useDispatch} from 'react-redux'
import {getUserAuthData, userActions} from '@/entities/auth/viewer/index.js'

const HEADER_HEIGHT = 56

const useStyles = createStyles(theme => ({
  header: {
    backgroundColor: '#131514',
    borderBottom: 0,
    margin: 0
  },

  dropdown: {
    position: 'absolute',
    top: HEADER_HEIGHT,
    left: 0,
    right: 0,
    zIndex: 0,
    borderTopRightRadius: 0,
    borderTopLeftRadius: 0,
    borderTopWidth: 0,
    overflow: 'hidden',
    backgroundColor: '#131514',

    [theme.fn.largerThan('sm')]: {
      display: 'none'
    }
  },

  inner: {
    height: 56,
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center'
  },

  links: {
    [theme.fn.smallerThan('sm')]: {
      display: 'none'
    }
  },

  linksMobile: {
    display: 'none'
  },

  burger: {
    [theme.fn.largerThan('sm')]: {
      display: 'none'
    }
  },

  link: {
    display: 'block',
    lineHeight: 1,
    padding: '8px 12px',
    borderRadius: theme.radius.sm,
    textDecoration: 'none',
    color: theme.white,
    fontSize: theme.fontSizes.sm,
    fontWeight: 500,

    '&:hover': {
      backgroundColor: theme.fn.lighten(
        theme.fn.variant({variant: 'filled', color: theme.primaryColor}).background,
        0.1
      )
    }
  },
  linkLabel: {
    marginRight: 5
  }
}))

export function HeaderMenu() {
  const links = [{link: '/', label: 'Домой'}]
  const [opened, {toggle}] = useDisclosure(false)
  const {classes} = useStyles()
  const authData = useSelector(getUserAuthData)
  const dispatch = useDispatch()

  console.log(authData)

  const items = links.map(link => {
    return (
      <NavLink key={link.label} to={link.link} className={classes.link}>
        {link.label}
      </NavLink>
    )
  })

  async function onLogout() {
    await dispatch(userActions.logout())
  }

  return (
    <Header height={56} className={classes.header} mb={4}>
      <Container>
        <div className={classes.inner}>
          <Group spacing={5} className={classes.links}>
            {items}
          </Group>
          <Group className={classes.hiddenMobile}>
            {!authData && (
              <>
                <Button variant="default">
                  <NavLink to="/login">Войти</NavLink>
                </Button>
                <Button>
                  <NavLink to="/register">Регистрация</NavLink>
                </Button>
              </>
            )}

            {authData && (
              <>
                <Button>
                  <NavLink to="/profile">Профиль</NavLink>
                </Button>
                <Button onClick={onLogout} variant="default">
                  Выйти
                </Button>
              </>
            )}
          </Group>
          <Burger opened={opened} onClick={toggle} className={classes.burger} size="sm" color="#fff" />
          <Transition transition="pop-top-right" duration={200} mounted={opened}>
            {styles => (
              <Paper className={classes.dropdown} withBorder style={styles}>
                {items}
              </Paper>
            )}
          </Transition>
        </div>
      </Container>
    </Header>
  )
}
