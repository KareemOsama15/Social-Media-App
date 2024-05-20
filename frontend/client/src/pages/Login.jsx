import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import RefreshToken from './RefreshToken';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/login/', { email, password })
      .then(result => {
        console.log(result);
        if (result.data.tokens) {
          const { refresh, access } = result.data.tokens;
          localStorage.setItem('refreshToken', refresh);
          localStorage.setItem('accessToken', access);
          navigate('/home');
        } else {
          setErrorMessage(result.data.error || 'Invalid email or password');
        }
      })
      .catch(err => {
        console.error(err);
        setErrorMessage('Invalid email or password');
      });
  };

  return (
    <>
    <RefreshToken/>
      <div className='flex justify-center items-center' style={{height:"100vh"}}>
        <div className='container'>
          <div className='grid grid-cols-1 md:grid-cols-2 gap-4'>
            <div className=' p-5'>
              <img className='w-full' src='https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg' alt='facebook' />
              <h5 className='text-center  p-5 '>Facebook enables you to communicate with people and share what you want with them.</h5>
            </div>
            <div className='bg-white rounded-lg p-5'>
              <form className='py-5' onSubmit={handleSubmit}>
                <input
                  type='email'
                  value={email}
                  placeholder='Email or phone'
                  className='w-full border rounded-lg p-2 mb-3'
                  onChange={(e) => setEmail(e.target.value)}
                />
                <input
                  type='password'
                  value={password}
                  placeholder='Password'
                  className='w-full border rounded-lg p-2 mb-3'
                  onChange={(e) => setPassword(e.target.value)}
                />
                {errorMessage && <div className="text-red-600 mt-3">{errorMessage}</div>}
                <button type='submit' className='w-full bg-blue-500 text-white rounded-lg py-2 mb-3'>
                  Login
                </button>
                
                <Link to='' className='block text-sm text-blue-700 mb-3'>Did you forget the password?</Link>
                <hr className='mb-3' />
                <Link to='SignUP' className='w-full bg-green-500 text-white rounded-lg py-2 mb-3 inline-block text-center'>Create New Account</Link>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
