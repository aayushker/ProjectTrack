import axios from 'axios';

const API = axios.create({ baseURL: 'http://127.0.0.1:8000' });

export const fetchProjects = () => API.get('/projects/');
export const acceptProject = (id: any) => API.post(`/projects/${id}/accept/`);
export const updateProgress = (id: any, data: any) => API.put(`/progress/${id}/update/`, data);
