import React, { useState } from "react";
import axios from "axios";

export default function Login(){
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const login = async () => {
    try {
      const res = await axios.post("http://localhost:8000/api/auth/token/", { username: email, password });
      const token = res.data.access;
      localStorage.setItem("token", token);
      window.location.href = "/";
    } catch(e){
      alert("Đăng nhập thất bại");
    }
  }
  return (
    <div>
      <h2>Đăng nhập</h2>
      <div><input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} /></div>
      <div><input placeholder="Mật khẩu" type="password" value={password} onChange={e=>setPassword(e.target.value)} /></div>
      <button onClick={login}>Đăng nhập</button>
    </div>
  )
}
