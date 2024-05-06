import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import Login from "./pages/SignIn";
export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path="/SignIN" element={<SignIn />} /> */}
        <Route path="/SignIN" element={<Login />} />
        <Route path="/SignUP" element={<SignUp />} />
        <Route path="/Home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}
