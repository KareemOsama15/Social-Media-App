import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UpdatePost = ({ postId, onClose }) => {
  const [postContent, setPostContent] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    fetchPost();
  }, []);

  const fetchPost = async () => {
    try {
      setIsLoading(true);
      const response = await axios.get(`http://127.0.0.1:8000/api/posts/id/update/${postId}/`);
      setPostContent(response.data.content);
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching post:', error);
      setIsLoading(false);
    }
  };

  const handleInputChange = (event) => {
    setPostContent(event.target.value);
  };

  const handleUpdatePost = async () => {
    try {
      setIsLoading(true);
      await axios.put(`http://127.0.0.1:8000/api/posts/${postId}/`, { content: postContent });
      setIsLoading(false);
      onClose(); // Close the update form after successful update
    } catch (error) {
      console.error('Error updating post:', error);
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="relative">
      <div className="fixed top-0 left-0 w-full h-full bg-gray-800 opacity-50 z-50"></div>
      <div className="flex items-center justify-center m-auto relative">
        <div className="absolute top-1/2 transform -translate-y-1/2 bg-white p-8 rounded-lg w-full md:w-1/2 lg:w-1/3 z-50">
          <h3 className="text-center font-bold mb-3">Edit Post</h3>
          <hr className="my-4"></hr>
          <textarea
            className="w-full h-40 border border-gray-300 rounded-md px-3 py-2 mb-4"
            placeholder="Enter post content..."
            value={postContent}
            onChange={handleInputChange}
          />
          <div className="flex justify-center space-x-2">
            <button
              className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
              onClick={handleUpdatePost}
            >
              Update Post
            </button>
            <button
              className="bg-gray-200 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-300"
              onClick={onClose}
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UpdatePost;
