import React, { useEffect, useState } from "react";
import API, { setAuth } from "../api";

export default function Dashboard(){
  const [summary, setSummary] = useState<any>(null);
  useEffect(()=>{
    const token = localStorage.getItem("token");
    if(token) setAuth(token);
    API.get("transactions/?page=1").then(r=> setSummary(r.data)).catch(()=> {});
  }, []);
  return (
    <div>
      <h2>Dashboard</h2>
      <p>Giao diện demo — bạn có thể mở rộng charts và báo cáo.</p>
      <pre>{JSON.stringify(summary, null, 2)}</pre>
    </div>
  )
}
