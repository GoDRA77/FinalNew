const baseAxiosConfig = {
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
}

const apiConfig = {
  login: {
    ...baseAxiosConfig,
    url: 'http://85.209.9.201/api/v1/auth/login/',
    method: 'post'
  },
  register: {
    ...baseAxiosConfig,
    url: 'http://85.209.9.201/api/v1/auth/register/',
    method: 'post'
  }
}

export default apiConfig
