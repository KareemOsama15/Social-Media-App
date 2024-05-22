import React from 'react';
import { FaFacebook,FaHome,FaVideo,FaShoppingBag,FaUsers, FaGamepad  } from 'react-icons/fa';
import {Link} from 'react-router-dom'
const Nav = () => {
  return (
 
    <>
    <nav className='bg-white shadow-md flex items-center justify-between py-5 px-6'>
      {/* facebook icon */}
        <div className='flex '>
        <FaFacebook className='text-blue-600 w-10 h-10'></FaFacebook>
        <input 
        type='text'
          placeholder='Search Facebook'
          className='bg-gray-200 py-2 px-8 rounded-full  ms-2  focus:outline-none'
          />
        </div>
        {/* search bar */}
        <div>

         
        </div>
        {/* Navigation Links */}
      
        <div className='flex items-center space-x-20 '>
          <Link to='home' className='hover:text-blue-500'><FaHome className='text-blue-600 w-7 h-7'></FaHome></Link>
         <Link to="video" className='hover:text-blue-500'><FaVideo className='text-blue-600 w-7 h-7'></FaVideo></Link>
         <Link to="marketplace" className='hover:text-blue-500'><FaShoppingBag className='text-blue-600 w-7 h-7'></FaShoppingBag></Link>
         <Link to="group" className='hover:text-blue-500'><FaUsers  className='text-blue-600 w-7 h-7'></FaUsers></Link>
         <Link to="gaming" className='hover:text-blue-500'> < FaGamepad className='text-blue-600 w-7 h-7'></FaGamepad></Link>
        </div>
        <div className='flex items-center space-x-8 bg-danger'>
        <Link to='menu' className='hover:text-blue-500'>Menu</Link>
         <Link to="messenger" className='hover:text-blue-500'>Messenger</Link>
         <Link to="notifications" className='hover:text-blue-500'>Notifications</Link>
         <Link to="account" className='hover:text-blue-500'>Account</Link>
        </div>
    </nav>
    
    </>
  );
};

export default Nav;

