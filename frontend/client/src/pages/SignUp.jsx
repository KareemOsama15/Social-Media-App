import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
export default function SignUp() {
  const [formData, setFormData] = useState({});
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData, //to keep the prev data
      [e.target.id]: e.target.value,
    });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const res = await fetch("/api/sign-up/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await res.json();
      console.log(data);
      setLoading(false);
      if (data.success === false) {
        setError(true);
        return;
      }
      navigate("/SignIN");
      setError(false);
    } catch (error) {
      setLoading(false);
      setError(true);
    }
  };
  return (
    <div className="p-4 max-w-lg m-auto">
      <h1 className="text-center text-3xl font-semibold mt-36 my-10">
        Sign Up
      </h1>
      <p className="text-red-700 mt-5 w-38 text-center mb-10">
        {error && "Something went wrong!"}
      </p>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 ">
        <input
          type="text"
          placeholder="username"
          className="border p-3 rounded-lg"
          id="username"
          onChange={handleChange}
        />
        <input
          type="email"
          placeholder="email"
          className="border p-3 rounded-lg"
          id="email"
          onChange={handleChange}
        />
        <input
          type="password"
          placeholder="password"
          className="border p-3 rounded-lg"
          id="password"
          onChange={handleChange}
        />
        <button
          disabled={loading}
          className="bg-slate-500 text-white p-3 rounded-lg hover:opacity-75 disabled:opacity-80"
        >
          {loading ? "loading....." : "Sign Up"}
        </button>
      </form>
      <div className="flex gap-2 w-48 m-auto my-5">
        <p>Have an account?</p>
        <Link to="/SignIN">
          <span className="text-blue-500">Sign In</span>
        </Link>
      </div>
    </div>
  );
}
