import React, { useEffect, useState } from "react";
import API from "../api";

export default function Transactions(){
  const [items, setItems] = useState<any[]>([]);
  useEffect(()=>{ API.get("transactions/").then(r=>setItems(r.data)).catch(()=>{}); }, []);
  return (
    <div>
      <h2>Giao dịch</h2>
      <table border={1} cellPadding={6}>
        <thead><tr><th>ID</th><th>Ngày</th><th>Danh mục</th><th>Số tiền</th><th>Ghi chú</th></tr></thead>
        <tbody>
          {items.map((t:any)=>(<tr key={t.id}><td>{t.id}</td><td>{t.date}</td><td>{t.category}</td><td>{t.amount}</td><td>{t.note}</td></tr>))}
        </tbody>
      </table>
    </div>
  )
}
