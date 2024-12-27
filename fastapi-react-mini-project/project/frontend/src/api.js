import axios from "axios";

// Create instance of axios with the base URL
const api = axios.create({
  // All API calls made from React components automatically use this base URL.
  baseURL: "http://localhost:8000"
});

export default api;
