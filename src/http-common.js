import axios from "axios";
export default axios.create({
  baseURL: "https://drf-disease-gfedr.run.goorm.io/",
  headers: {
    'Accept': 'application/json',
    "Content-type": "application/json"
  }
});