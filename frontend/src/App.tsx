import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import AIReports from "./pages/AIReports";

export default function App(){
  return (
    <div style={{padding:20}}>
      <header>
        <h1>Quản lý chi tiêu AI</h1>
        <nav>
          <Link to="/">Dashboard</Link> | <Link to="/transactions">Giao dịch</Link> | <Link to="/reports">Báo cáo AI</Link> | <Link to="/login">Đăng nhập</Link>
        </nav>
      </header>
      <main style={{marginTop:20}}>
        <Routes>
          <Route path="/" element={<Dashboard/>} />
          <Route path="/transactions" element={<Transactions/>} />
          <Route path="/reports" element={<AIReports/>} />
          <Route path="/login" element={<Login/>} />
        </Routes>
      </main>
    </div>
  );
}
