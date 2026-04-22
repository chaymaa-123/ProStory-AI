import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  const userId = localStorage.getItem('user_id')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  if (userId) {
    config.headers['x_user_id'] = userId
  }
  return config
})

// Experience API functions
export const experienceApi = {
  create: (data: any) => api.post('/experience', data),
  getById: (id: string) => api.get(`/experience/${id}`),
  update: (id: string, data: any) => api.put(`/experience/${id}`, data),
  delete: (id: string) => api.delete(`/experience/${id}`),
  listMy: (params?: { skip?: number; limit?: number }) => api.get('/experience/mes-experiences', { params }),
  feed: (params?: { skip?: number; limit?: number }) => api.get('/experience/feed', { params }),
}

export default api

