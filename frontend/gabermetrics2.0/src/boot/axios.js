import { boot } from 'quasar/wrappers'
import axios from 'axios'

// Create an Axios instance
const api = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Flask backend URL
})

export default boot(({ app }) => {
  // Make Axios available globally in the app
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
})

export { api }

