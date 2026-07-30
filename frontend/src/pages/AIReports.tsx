import React, { useState } from "react";
import API from "../api";

export default function AIReports(){
  const [month, setMonth] = useState("");
  const [result, setResult] = useState("");
  const run = async () => {
    try{
      const r = await API.post("ai/report/", { month });
      setResult(r.data.report);
    }catch(e:any){
      setResult(e.response?.data?.detail || "Lỗi");
    }
  }
  return (
    <div>
      <h2>Báo cáo AI</h2>
      <div>
        <input placeholder="YYYY-MM" value={month} onChange={e=>setMonth(e.target.value)} />
        <button onClick={run}>Chạy báo cáo</button>
      </div>
      <pre>{result}</pre>
    </div>
  )
}
