import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import Login from "./pages/Login";
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
       
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/SignUP" element={<SignUp />} />
        <Route path="/Home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}
