import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Nav from "./pages/Nav";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import Login from "./pages/Login";
// import RefreshToken from "./pages/RefreshToken";

export default function App() {
  return (
    <div className="App" style={{ backgroundColor: '#f0f2f5',height:"100%" }}>
    <BrowserRouter>
    <Nav/>
        
      <Routes>
      {/* <Route path="/refresh" element={<RefreshToken />} /> */}
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/SignUP" element={<SignUp />} />
        <Route path="/Home" element={<Home />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}
