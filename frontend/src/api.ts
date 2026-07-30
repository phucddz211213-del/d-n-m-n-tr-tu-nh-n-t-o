import axios from "axios";
const API = axios.create({ baseURL: "http://localhost:8000/api/" });

export function setAuth(token: string){
  API.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

export default API;
