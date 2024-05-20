import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaTimes,FaHeart,FaComment,FaShare } from 'react-icons/fa';
const ListAllPost = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        if (token) {
          const config = {
            headers: {
              "Authorization":`Bearer ${token}`
            }
          }
        // http://127.0.0.1:8000/api/posts/
        const response = await axios.get(' https://jsonplaceholder.typicode.com/posts', config);
        setPosts(response.data);
      }} catch (error) {
        console.error('Error fetching posts:', error);
      }
    };

    fetchPosts();
  }, []);

  return (
    <>
      <h2>All Posts</h2>
      <div className=' space-y-4  w-full md:w-1/2 p-2  m-auto rounded-md '>
        {posts.map((post) => (
          <div key={post.id} className=' bg-white rounded-lg' >
            <div className="flex justify-end p-3 text-gray-500" >
            <FaTimes />
            </div>
            <div className='flex p-5'>
           <img
            src="https://cdn.pixabay.com/photo/2014/04/02/17/07/user-307993__340.png"
            alt="img-user"
            className="rounded-full w-16 h-16 mr-4"
          />
          <h1 className='mt-5'>Asmaa Elsobahy</h1>
          
        <hr></hr>
        </div>
        <h2 className='mb-4'>{post.title}</h2>

        <div className='py-3 px-8 flex justify-between'>

<div className='flex ms-5' >
  <FaHeart className='text-gray-500 w-6 h-6 mr-2'/>
<h4>Like</h4>
</div>

<div className='flex ms-5' >
  <FaComment className='text-gray-500 w-6 h-6 mr-2'/>
<h4>Comment</h4>
</div>
<div className='flex ms-5' >
  <FaShare className='text-gray-500 w-6 h-6 mr-2'/>
<h4>Share</h4>
</div>

</div>
            
            {post.image && <img src={post.image} alt="Post" />}
           
            <hr />
          </div>
        ))}
      </div>
     
    </>
  );
};

export default ListAllPost;
